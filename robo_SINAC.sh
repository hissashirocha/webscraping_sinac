#!/bin/bash

START=$(date +%s)

python3 download_SINAC.py
if [[ $? = 0 ]]; then


    rename 's/inac/inac-AC/' 'EstatisticasSinac.csv'
    rename 's/\(1\)/-AL/' 'EstatisticasSinac(1).csv'
    rename 's/\(2\)/-AM/' 'EstatisticasSinac(2).csv'
    rename 's/\(3\)/-AP/' 'EstatisticasSinac(3).csv'
    rename 's/\(4\)/-BA/' 'EstatisticasSinac(4).csv'
    rename 's/\(5\)/-CE/' 'EstatisticasSinac(5).csv'
    rename 's/\(6\)/-DF/' 'EstatisticasSinac(6).csv'
    rename 's/\(7\)/-ES/' 'EstatisticasSinac(7).csv'
    rename 's/\(8\)/-GO/' 'EstatisticasSinac(8).csv'
    rename 's/\(9\)/-MA/' 'EstatisticasSinac(9).csv'
    rename 's/\(10\)/-MG/' 'EstatisticasSinac(10).csv'
    rename 's/\(11\)/-MS/' 'EstatisticasSinac(11).csv'
    rename 's/\(12\)/-MT/' 'EstatisticasSinac(12).csv'
    rename 's/\(13\)/-PA/' 'EstatisticasSinac(13).csv'
    rename 's/\(14\)/-PB/' 'EstatisticasSinac(14).csv'
    rename 's/\(15\)/-PE/' 'EstatisticasSinac(15).csv'
    rename 's/\(16\)/-PI/' 'EstatisticasSinac(16).csv'
    rename 's/\(17\)/-PR/' 'EstatisticasSinac(17).csv'
    rename 's/\(18\)/-RJ/' 'EstatisticasSinac(18).csv'
    rename 's/\(19\)/-RN/' 'EstatisticasSinac(19).csv'
    rename 's/\(20\)/-RO/' 'EstatisticasSinac(20).csv'
    rename 's/\(21\)/-RR/' 'EstatisticasSinac(21).csv'
    rename 's/\(22\)/-RS/' 'EstatisticasSinac(22).csv'
    rename 's/\(23\)/-SC/' 'EstatisticasSinac(23).csv'
    rename 's/\(24\)/-SE/' 'EstatisticasSinac(24).csv'
    rename 's/\(25\)/-SP/' 'EstatisticasSinac(25).csv'
    rename 's/\(26\)/-TO/' 'EstatisticasSinac(26).csv'

    for i in *.csv
    do
    echo "    Processando $i"

    sed -i -e '/Total/d' $i

    awk '
    BEGIN {FS=OFS=","}
    NF--' $i > temp
    #mv temp $i

    awk '

    {
        if (match($0, /\-[^0-9]/))
        {
            split($0,a,"-");
            print a[1] " " a[2] "-" a[3];
        } else
            print $0;
    }' temp > $i


    sed -i -e 's/\-/\,/' $i
    sed -i -e s/"'"/" "/g $i

    x=$(echo ${i%%.*} | cut -c19-20)
    awk -F ',' '{$1=val FS $1;}1' OFS=',' val=$x $i > temp
    mv temp $i

    data=$(sed -n 1p data_ref.txt)
    awk -F ',' '{$1=val FS $1;}1' OFS=',' val=$data $i > temp
    mv temp $i

    done

    DATA=$(date +%Y%m%d)
    cat *.csv >> EstatisticasSinacFinal.txt
    rm *.csv
    rm data_ref.txt

else
    "Deu erro no download/montagem do arquivo!"
fi

python3 readSINAC_insertDB.py
if  [[ $? = 0 ]]; then
    echo "Carregou no banco"
else
    "Deu erro na insercao no banco! Erro: $?"
fi

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "Tempo de Execucao: $DIFF minutos." >> LOG_${DATA}.txt
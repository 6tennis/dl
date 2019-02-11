#!/bin/bash
time=$1
if [ -z $1 ]; then 
    time=180
fi
echo "create slow chart (${time}s)"
echo 'name,star,element,weapon,str,condition,comment,dps' > www/$1/slow_data.csv
python adv/addis.py -2      $1 | tee -a www/$1/slow_data.csv
python adv/ieyasu.py -2     $1 | tee -a www/$1/slow_data.csv
python adv/sinoa.py -2      $1 | tee -a www/$1/slow_data.csv
python adv/ezelith.py -2    $1 | tee -a www/$1/slow_data.csv
python adv/sazanka.py -2    $1 | tee -a www/$1/slow_data.csv
python adv/botan.py -2      $1 | tee -a www/$1/slow_data.csv
#!/bin/bash

for a in 1 2 3
do
    echo "$a"
done

hello="A B   C    D"
echo $hello
echo "$hello"


echo "Press y to continue"
read yn
if [ "$yn">"y" ]; then
        echo "script is running..."
else
        echo "STOP!"
fi

n1=10
n2=12
if [ "${n1}" -gt "${n2}" ];then
echo ${n1}
elif [ "${n1}"="${n2}" ];then
echo ${n1}
else
echo ${n2}
fi

path="./"
filename="test.txt"
if [ -e ${filename} ]
then
    echo $filename
    if [ -s ${filename} ]
    then
    ls -al ${filename}
    fi
fi

a=`ls -la test.txt | awk '{print $5}'`  
if [ $a -lt 100 ]  
then  
       echo "data file size $a ok"  
else  
       echo "no"  
fi  

sum=0
for i in $(ls -l|awk '{print $5}')
do
if [ $i -ne 0 ]
then 
    #sum=$(($sum+$i));
    ((sum+=$i));
fi
echo "all files size: $sum"
done

# + - * % arithmetic expansion.
echo $(($sum+100))
let "sum +=1"
echo $sum

echo "generate 10 random numbers"
MAXCOUNT=10
cnt=0;

while [ "$cnt" -lt "$MAXCOUNT" ] 
do
echo number[$cnt]=$RANDOM
let "cnt+=1"
done

awk -FK '{sum+=$1} END{print "sum="int($sum/1024)}' ./proc.out
awk -FK '{sum+=$1} END{print "sum="sum}' ./proc.out
ls -l | awk 'BEGIN{sum=0}{sum+=$5} END{print "sum="sum}'

for a in 1 2 3 4 5 6 7 8 9 10
do
echo -n "$a"
done

echo 

############## function ##############
func_1()
{
    echo "\"func1\" is called"
    arg="value2"
    val=10.5
    func_2 ${arg} $1 ${val}
}

echo "declare \"func2\"."
func_2()
{
    echo "\"func2\" is called, parameter \"$1\" \"$2\", $3"
}

func_1 "val_1"

################ if test ##############
if test -e file_1.txt
then
    echo "file_1.txt exists"
else
    echo "file_1.txt doesn't exist"
fi

echo "done"
exit 0

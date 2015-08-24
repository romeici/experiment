#!/bin/bash

startAddr=0x$(hexdump vxWorks.bin | awk 'NR==1{print $1}') 
echo $startAddr 

size=0x$(hexdump vxWorks.bin | awk 'NR==1{print $4$5}')  
echo $size

echo $(($size+1))
dd if=vxWorks.bin of=data.bin bs=1 count=$(($size)) skip=$(($startAddr))     

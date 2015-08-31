#!/usr/bin/env python3
# -*-encoding:utf-8 -*-
#file.py

import binascii  
import struct  
import zlib

f = open('test.jpg', 'rb')
f.seek(0x100)
buf=f.read()
f.close()
print([i for i in buf])


f1 = open("for_read.txt")             # 返回一个文件对象 
line = f1.readline()             # 调用文件的 readline()方法 
while line: 
    print(line, ' ')
    line = f1.readline()
	
f1.close

fb = open("vxWorks.bin","rb")             # bin文件处理 
data=fb.read(4)
test=hex(data[0])
print(data)
print(int(test,16))
print(test)
b=bin(data[0])
c=oct(data[0])
print(int(b,2),int(c,8))
fb.seek(len(data))
other=fb.read(1024)
vx_com = zlib.compress(other)
fb.seek(0)
print(fb.read(4))
fb.close

print(type(data),data)
addr,=struct.unpack('i', bytes(data))
print(addr)
print(hex(addr))
addr_cp=int(hex(addr),16)
print(addr_cp)

#
a=input("enter a number: ")
x = int(input("enter 0x number: "), 16)
b=int(a)+5
print('%s,0x%x,0x%x' % (a,b,x))
print(type(a),type(b),type(x))
print(type(a) is 'int')
print(hex(x))

stream=struct.pack('LL',x,b)
print(stream)

fw = open("fw.bin","wb")
fw.write(stream)
fw.seek(len(stream))
print(list(map(lambda x:x+16,other)))
fw.write(bytearray(map(lambda x:x&0xFF,other)))
fw.write(vx_com)
vx_decom=zlib.decompress(vx_com)
print((other == vx_decom))
print(other)
print(vx_decom)
fw.close

hl=lambda x,y=0xff:x&y
print(hl(0x3254))
#coding:utf-8

'''


@author: Rocky
'''
#from __main__ import socket

if __name__ == '__main__':
    import socket,sys
    port = 12345
    host = input('输入服务器ip:')
    data = input('输入要发送的信息:')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((host,port))
    except:
        print('连接错误!')
    s.send(data.encode('utf-8'));
    s.shutdown(1);
    print('发送完成')
    while 1:
        buf = s.recv(4096)
        if not len(buf):
            break;
        sys.stdout.write(buf.decode('utf-8'))
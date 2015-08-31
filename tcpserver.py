#coding:utf-8
'''
Created on 2015��8��12��

@author: Rocky
'''
#from test.test_codecs import coding_checker

if __name__ == '__main__':
    import socket, traceback
    
    
    host = '';
    port = 12345;
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
    s.bind((host, port));
    s.listen(1);
    
    while 1:
        try:
            clientsock,clientaddr = s.accept();
        except KeyboardInterrupt:
            raise
        
        except:
            traceback.print_exc();
            continue;
        
        try:
            print("连接来自：",clientsock.getpeername())
            while 1:
                data = clientsock.recv(4096);
                if not len(data):
                    break;
                print(clientsock.getpeername()[0])
                print(':')
                print(str(data))
                clientsock.sendall(data);
                clientsock.sendall("\n I get it! \n".encode('utf-8'));
                t = input('input the word:')
                clientsock.sendall(t.encode('utf-8'));
        except (KeyboardInterrupt , SystemExit):
            raise;
        except:
            traceback.print_exc();
            
        try:
            clientsock.close();
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc();
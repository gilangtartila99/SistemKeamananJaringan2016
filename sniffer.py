import socket
import sys

def receiveData(s):
        data = ''
        try:
                data = s.recvfrom(65565)
        except timeout:
                data = ''
        except:
                print "An error happened."
                sys.exc_info()
        return data[0]

HOST = socket.gethostbyname(socket.gethostname())

s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print s.recvfrom(65565)

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

import socket
import struct
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

data = receiveData(s)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])

version_ihl = unpackedData[0]
version = version_ihl >> 4
ihl = version_ihl & 0xF
     
iph_length = ihl * 4
     
ttl = unpackedData[5]
protocol = unpackedData[6]
s_addr = socket.inet_ntoa(unpackedData[8]);
d_addr = socket.inet_ntoa(unpackedData[9]);

print 'Version : ' + str(version) + ', IP Header Length : ' + str(ihl) + ', TTL : ' + str(ttl) + ', Protocol : ' + str(protocol) + ', Source Address : ' + str(s_addr) + ', Destination Address : ' + str(d_addr)

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

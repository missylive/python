#!/usr/bin/python from scapy.all import *
ip = IP(src="10.0.2.4", dst="10.0.2.6") 
tcp = TCP(sport=22, dport=39752, flags="0x012", seq=415058523, ack=3729252217)
pkt = ip/tcp 
ls(pkt) 
send(pkt,verbose=0)

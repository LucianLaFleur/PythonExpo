#!/usr/bin/env python

#uses python 2 syntax, may need adjustment for python3+

#rename the import for easier calls down the line
import scapy.all as scapy
import optparse
import re



def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Specify target IP or range")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("No target specified, use [--t] then specify a target")
    # if not "10.0.2.\d?\d(\/)?\d?\d?"
    x = re.search(r"\d\d.\d.\d.\d?\d(\/)?\d?\d?", options.target)
    if x:
        print("searching targeted areas....")
    else:
        print("Problem encountered: Check target formatting [ex: 10.0.2.1/24 ]")
    # print(re.search(r"10.0.2.\d?\d(\/)?\d?\d?", options.target))
    return options

#discovers clients on the same network using ARP protocol
def scan(ip):
    # make an ARP request
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # broadcast to all clients with full-f's
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # SRP lets us send a custom Ether part
    # catch both returned values in simul-assigned vars, set timeout to
    # move on if no response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for e in answered_list:
        client_dict = {"ip":e[1].psrc, "mac": e[1].hwsrc}
        clients_list.append(client_dict)
        # print(e[1].psrc + "\t\t" + e[1].hwsrc)
        # print("---------------------------")
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\t\t >>^UwU^<<\n -----------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
# scan_result = scan("10.0.2.1/24")
print_result(scan_result)

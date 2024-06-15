import numpy as np
import scapy.all as scapy

def load_ngram(path):
    result = []
    for pkt in scapy.rdpcap(path):
        if pkt.haslayer(scapy.DNSQR):
            query = pkt[scapy.DNSQR].qname.decode()
            result.append(query)
    return result

def load_ts(path):
    result = []
    for pkt in scapy.rdpcap(path):
        if pkt.haslayer(scapy.DNSQR):
            # query = pkt[scapy.DNSQR].qname.decode()
            # # query = query.split('.')
            # # query = '.'.join(query[:len(query) - 1])
            # data_attack.append(query)
            # Get src from ethernet
            result.append({
                'time': float(pkt.time),
                'query': pkt[scapy.DNSQR].qname.decode(),
                'src': pkt[scapy.Ether].src,
                'len': pkt[scapy.UDP].len,
            })
    return result
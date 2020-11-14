#!/usr/bin/env python3
import socket
from IPy import IP


def scan(target):
    # Get the ip of a url
    converted_ip = check_ip(target)

    print('\n' + '[-_0 Scanning Target]' + str(target))

    # Scan ports of target
    for port in range(1, 500):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        # If target is an ip return the ip
        IP(ip)
        return ip
    except ValueError:
        # If target is URL return its ip
        return socket.gethostbyname(ip)


def get_banner(s):
    # Determine services if any
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' +
                  str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


def run():
    # UI for port scanner
    targets = input(
        '[+] Enter Target/s to Scan (separate targets with a comma): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)


if __name__ == "__main__":
    run()

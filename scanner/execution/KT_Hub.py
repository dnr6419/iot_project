import requests
import socket
import csv
path = './result.csv'
port = 8877

def get_ip_list():
    ip_list = []
    try:
        with open(path,'r') as f:
            read = csv.DictReader(f)
            for c in read:
                if (c['state'] == 'open'):
                    if c['port'] == '8877':
                        ip_list.append(c['host'])
        return list(set(ip_list))
    except FileNotFoundError:
        print('[-] Scan frist !!')


def find_kthub():
    ip_list = get_ip_list()
    arr = []
    for ip in ip_list:
        if is_kthub(ip) == 1:
            arr.append(ip)
    for ip in arr:
        print(f"[*] KThub device ip is : {ip}\n")


def is_kthub(ip):
    url = f'http://{ip}:{port}/'
    try:
        res = requests.get(url=url)
        answer = res.text
        if '/goform/mcr_verifyLoginPasswd' not in answer:
            print("[-] Not! KThub")
            return 0
        print(f"[+] The device which has ip({ip}) is kthub")
        print(f'[+] URL is {url}')
        return 1
    except Exception as e:
        print("[-] Another error is happened!",e)
        return 0

#find_kthub()

import requests as r
import socket
import csv
import nmap
path = './result.csv'
port = 3000

def get_ip_list():
    ip_list = []
    with open(path,'r') as f:
        read = csv.DictReader(f)
        for c in read:
            if (c['state'] == 'open'):
                if c['port'] == '3000':
                    ip_list.append(c['host'])
    return list(set(ip_list))

def find_webOS():
    ip_list = get_ip_list()
    arr = []
    for ip in ip_list:
        if is_webOS(ip) == 1:
            arr.append(ip)
    for ip in arr:
        print("webOS device ip is : {}".format(ip))

def is_webOS(ip):
    # check the port number 8222
    url = 'http://{}:{}/'.format(ip,port)
    #print("url : {}".format(url))
    try:
        res = r.get(url=url)
        if 'Hello world' in res.text:
            ns = nmap.PortScanner()
            res = ns.scan(hosts=ip, ports='1-3000', arguments='-sT') #SYN Open Scan
            port_list = list(res['scan'][ip]['tcp'].keys())
            #print(port_list)
            flag = False
            url_list = []
            for p in port_list:
                url = 'http://{}:{}/'.format(ip,p)
                res = r.get(url=url)
                if "webOS" in res.text:
                    flag = True
                    url_list.append(url)
            if flag:
                print("[+] This device is webOS if you want to look more info about {}".format(ip))
                print("[+] here to click the urls")
                for u in url_list:
                    print(u)
                return 1
        return 0
    except Exception as e:
        print("another error is happened!",e)
        return 0

#find_webOS()

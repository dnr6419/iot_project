import nmap
import sys, os
import csv
import requests
from datetime import datetime
import time
from pprint import pprint


def Scan(hosts,ports,arguments):
    #Banner Time
    print('-'*50)
    print(f"Scanning started at: {str(datetime.now())}")
    print('-'*50)

    try:
        # initialize the port scanner
        ns = nmap.PortScanner()
        port = ['22','443','8877']
        # scan ports in range
        res = ns.scan(hosts='192.168.0.19', ports='1-3000', arguments='-sT T4') #SYN Open Scan
        #pprint(res)

        # run a loop to print all the found result about the ports
        for host in ns.all_hosts(): #host ip ex) 192.168.123.123
            print('\n-------------------Scan Result--------------------')
            print(f'[*] Host : {host}')
            print(f'[*] State : {ns[host].state()}')
            for proto in ns[host].all_protocols(): #host protocol check tcp or udp ex) ['tcp']
                print(f'[*] Protocol : {proto}')
                print('-'*50)

                lport = ns[host][proto].keys() #host's tcp / udp protocol value(port) ex) [22,23,443....]
                #lport.sort()
                for port in lport:
                    if ns[host][proto][port]["state"] == 'open':
                        print(f'[+] port : {port}\t\tstate : {ns[host][proto][port]["state"]}')
                        webservice_check(host,port)
                save_csv(ns)
    except KeyboardInterrupt:
            print("\n[-] Error: KeyboardInterrupt, Exit Program.")


def save_csv(ns):
    with open('result.csv','w') as f:
        f.writelines(ns.csv().replace(';',','))


def read_csv():
    with open('result.csv','r',encoding='utf-8') as f:
        content = csv.DictReader(f)
        return content
        

def webservice_check(host,port):
    try:
        response = requests.head(url=f'http://{host}:{port}',timeout=10)
        status = response.status_code
        if status == 200:      #web service check
            requests.encoding='euc-kr'
            print(f'[+] Running Web Service : http://{host}:{port}')
    except requests.exceptions.ConnectionError:
        print(f'[-] A Connection Error occurred : http://{host}:{port}')
    except requests.exceptions.Timeout as e:
        print('[-] Status : 408 ',e)
    except requests.exceptions.TooManyRedirects as e:
        print('[-] Status : 429 ',e)
    except requests.exceptions.RequestException as e:
        print('[-] Status : 999 ',e)


def main():
    Scan()


if __name__ == '__main__':
    start = time.time()
    main()
    print("time :", time.time() - start)
    #read_csv()
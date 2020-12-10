import requests
import socket
import csv
import json
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET

path = './result.csv'
# check the argument
port = 80 
url = "http://192.168.123.120"

def view_xml(url):
    url = f'{url}/description.xml'
    try:
        res = requests.get(url=url)
        answer = res.text
        tree= ET.ElementTree(ET.fromstring(answer))
        note = tree.getroot()
        print(note.getchildren())
        #res = note.getchildren()[2].getchildren()
        for i in res:
            #print("{} : {}".format(i.tag.split("}")[1],i.text))
            print(f'{i.tag.split("}")[1]} : {i.text}')
    except Exception as e:
        print("[-] Another error is happened!",e)


def get_ip_list():
    ip_list = []
    with open(path,'r') as f:
        read = csv.DictReader(f)
        for c in read:
            if (c['state'] == 'open'):
                if c['port'] == str(port):
                    ip_list.append(c['host'])
    return list(set(ip_list))


def find_phillips():
    ip_list = get_ip_list()
    arr = []
    flag = False
    for ip in ip_list:
        if is_phillips(ip) == 1:
            flag = True
            arr.append(ip)
    for ip in arr:
        print(f"[+] phillips device ip is : {ip}")
    if flag == False:
        print("[+] No phillips devices in here!")
    return ip


def is_phillips(ip):
    url = f'http://{ip}:{port}/'
    try:
        res = requests.get(url=url)
        answer = res.text
        if 'hue personal wireless lighting' not in answer: # check 
            # print("[+] Not! phillips({})".format(ip))
            return 0
        print(f"[+] The device which has ip({ip}) is phillips")
        print(f'[+] URL is {url}')
        return 1
    except Exception as e:
        #print("[-] Another error is happened!",e)
        return 0 


def find_vuln():
    url = "{}/{}".format(url,"/licenses/packages.json")
    res = r.get(url=url)
    uboot_arr = "uboot-envtools" # check version 
    j = json.loads(res.text)
    for idx in range(len(j)):
        if 'uboot' in j[idx]['Package']:
            print(f"[+] package of uboot : {j[idx]['Package']}")
            print(f"[+] version : {j[idx]['Version']}")

#find_phillips()
#find_vuln(url)
#view_xml(url)
#res = get_ip_list()
#print(res)
import sys, os
import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings('ignore')

def get_ip_list():
    ip_list = []
    try:
        with open('result.csv','r') as f:
            res = csv.DictReader(f)
            for line in res:
                if (line['host'] == '192.168.0.1'):
                        ip_list.append(line['host'])
        return list(set(ip_list))
    except FileNotFoundError:
        print('[-] Scan frist !!')


def dlink_nework_test(dlink_ip):
    try:
        #dlink_ip = get_ip_list()[0]
        #print(dlink_ip)
        response = requests.head(url=f'http://{dlink_ip}',timeout=10)
        status = response.status_code
        if status == 200:      #web service check
            requests.encoding='euc-kr'
            dlink_admin_page_check(dlink_ip)
    except requests.exceptions.ConnectionError:
        print('[-] Need to connect D-Link Router, The web page does not D-link Admin page !')
    except requests.exceptions.Timeout as e:
        print('[-] Status : 408 ',e)
    except requests.exceptions.TooManyRedirects as e:
        print('[-] Status : 429 ',e)
    except requests.exceptions.RequestException as e:
        print('[-] Status : 999 ',e)


def dlink_admin_page_check(dlink_ip,port):

    phantom_path = '/home/dnr6419/tool/dlink/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
    my_url = f"http://{dlink_ip}:{port}/info/Login.html"

    driver = webdriver.PhantomJS(phantom_path)
    driver.get(my_url)
    time.sleep(1)

    model = driver.find_element_by_xpath('//*[@id="modelName"]')
    hardware_version = driver.find_element_by_xpath('//*[@id="HWversion"]')
    firmware_version = driver.find_element_by_xpath('//*[@id="FWversion"]')

    print("model_name : {}".format(model.text))
    print("hardware_version : {}".format(hardware_version.text))
    print("firmware_version : {}".format(firmware_version.text))
    if "dir-822" in model.text:
        return 1
    return 0

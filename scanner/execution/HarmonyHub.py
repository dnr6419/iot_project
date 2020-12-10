import requests
import socket
import csv

path = './result.csv'

def get_ip_list():
    ip_list = []
    with open(path,'r') as f:
        read = csv.DictReader(f)
        for c in read:
            if (c['state'] == 'open'):
                if c['port'] == '8088' or c['port'] == '8222':
                    ip_list.append(c['host'])
    return list(set(ip_list))


def find_logitech():
    ip_list = get_ip_list()
    arr = []
    for ip in ip_list:
        if is_logitech(ip) == 1:
            arr.append(ip)
    for ip in arr:
        print(f"Logitech device ip is : {ip}")


def is_logitech(ip):
    # check the port number 8222
    url = f'http://{ip}:8222/'
    try:
        res = requests.get(url=url)
        answer = res.text
        if '[]' not in answer:
            print("not! logitech")
            return 0
        location = (ip, 8088)
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = a_socket.connect_ex(location)
        if result_of_check != 0:
            print("not! logitech")
            return 0
        a_socket.close()
        print(f"The device which has ip({ip}) is logitech harmony hub")
        return 1
    except Exception as e:
        print("another error is happened!",e)

# find_logitech()

#def api_command():
#    # 
#    arr = 'http://192.168.123.131:8222/api/connect.discoveryinfo?get'
#
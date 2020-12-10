import os
import sys
import threading
import time
from db_update import *

def sys_nmap(option,ip_band,port_band):
    command = f"nmap {option} {ip_band} -p{port_band} --open 1> ./tmp"
    #print(command) nmap -v -sT -T4 192.168.123.0/24 -p8222,3000,8877,80,443,30000 --open 1> ./tmp
    os.system(command)
    # real time save the files (tmp)

def tmp2db(ori): ## Discovered open port 80/tcp on 192.168.123.110        
    ori_parsing = ori.split("\n")
    for line in ori_parsing:
        ap = []
        if "Discovered open port" in line: # open port insert to db
            arr = line.split(" ") 
            [ap.append([arr[-1],arr[1],arr[3].split("/")[0]]) for i in range(len(arr))]
            checkRootine(ap)

def read_tmp(t):
    idx = 0
    while(True):
        if t.is_alive(): # is scan over
            time.sleep(3)
            f = open('./tmp','r') # 
            s = int(os.stat('./tmp').st_size)
            #print(f"[+] size is {s}")
            f.seek(idx)
            ori = f.read(s-idx)
            tmp = len(ori)
            if tmp == idx:
                continue # skip the same results
            else:
                if ori: # ori parsing and open port finding!
                    tmp2db(ori)
            idx += tmp
            f.close()
        else:
            f = open('./tmp','r') # 
            s = int(os.stat('./tmp').st_size)
            f.seek(idx)
            ori = f.read(s-idx) 
            tmp = len(ori)
            if tmp != idx:
                if ori: # ori parsing and open port finding!
                    tmp2db(ori)
            break
    print("========================================")
    print("over! delete the tmp file")
    #os.system("rm -rf ./tmp")

if __name__ == '__main__':
    option = "-v -sT -T4"
    ip_band = "192.168.123.0/24"
    port_band = '8222,3000,8877,80,443,30000'
    # this is initial scanning 
    # t1 = threading.Thread(target=getHtml, args=('http://google.com',))
    try:
        t = threading.Thread(target=sys_nmap,args=(option,ip_band,port_band))
        t.start()
        read_tmp(t)
    except Exception as e:
        print(f"error {e}")
    #realTimeScan()
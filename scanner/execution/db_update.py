import nmap
import psycopg2
#from DlinkRouter import *
from HarmonyHub import *
from KT_Hub import *
from Phillps_Hue import *
from webOS import *
from netaddr import IPNetwork

## db connect setting
host = 'db'
dbname = 'hello_django_prod'
user = 'hello_django'
password = 'hello_django'
db_port = '5432'

# insert or udpate
def executeQuery(query,flag):
    #print(f"[+] query : {query}")
    conn_string = f"host={host} port={db_port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    if flag: # is select
        result = cur.fetchall() 
        cur.close()
        return result
    cur.close()

def update_DB(ip,port,device):
    print(f"[+] update_DB executed!! ({ip} , {port} , {device})")
    select = f"select * from net_scan_t_r where ip = '{ip}'" # 해당 ip주소가 db에 기록해 두었는지 확인
    r = executeQuery(select,1) # select 질의문은 응답값이 있으니 1 처리를 하고 응답값을 r에 받아온다.
    str_port = str(port)
    #print(f"r = {r}") #[(41, '192.168.123.110', '80,443', 'Unknown', datetime.datetime(2020, 12, 9, 15, 35, 59, 856612, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=540, name=None)))]
    if r != []: # 중복되는지 체크 (r이 설저되어 있다면 동일 ip가 db에 저장되어 있음을 의미한다.)
        if str(port) in r[0][2]: # 중복되는 port 번호는 current_timestamp만 바꾸도록 진행
            str_port = r[0][2]
            delete = f"DELETE FROM net_scan_t_r WHERE ip = '{ip}'"
            executeQuery(delete,0)
        else: # 중복되지 않은 port 번호는 str_port에 추가해서 db에 저장한다.
            str_port += "," + str(r[0][2])
            delete = f"DELETE FROM net_scan_t_r WHERE ip = '{ip}'"
            executeQuery(delete,0)     
        if r[0][3] != 'Unknown':
            device = r[0][3] # 식별된 device는 unknown을 할 필요가 없다. 
    insert = f"insert into net_scan_t_r(ip,port,device,cdate) values('{ip}','{str_port}','{device}',current_timestamp)"
    executeQuery(insert,0)


#ap = initial_scan(ip_band,port_band,arguments)
#ap = [['192.168.123.129', 'open', '8222'], ['192.168.123.111', 'open', '8877'], ['192.168.123.115', 'open', '80'], ['192.168.123.121', 'open', '80'], ['192.168.123.125', 'open', '80'], ['192.168.123.128', 'open', '80'], ['192.168.123.254', 'open', '80'], ['192.168.123.104', 'open', '443'], ['192.168.123.112', 'open', '443'], ['192.168.123.117', 'open', '443'], ['192.168.123.121', 'open', '443'], ['192.168.123.128', 'open', '443']]
def checkRootine(ap):
    for idx in ap:
        host = idx[0]
        port = idx[2] # str type
        if int(port) == 3000:
            if is_webOS(host):
                ip = host
                port = 3000
                device = 'webOS'
                update_DB(ip,port,device)
                continue
        # is kthub
        if int(port) == 8877:
            if is_kthub(host):
                ip = host
                port = 8877
                device = 'KThub'
                update_DB(ip,port,device)
                continue
        # is logitech
        if int(port) == 8222:
            if is_logitech(host):
                ip = host
                port = 8222
                device = 'logitech'
                update_DB(ip,port,device)
                continue
        # if phillips
        if int(port) == 80:
            if is_phillips(host):
                ip = host
                port = 80
                device = 'phillips'
                update_DB(ip,port,device)
                continue
        ip = host
        device = 'Unknown'
        update_DB(ip,port,device)
    #print("finished")


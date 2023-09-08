import csv
from datetime import datetime
import os
import time




srv=input("Set logfile name: ") or "check"
dst=input("Set destination IP addr to check: ") or "8.8.8.8"
print("Working...\n(Ctrl+C) to stop.\n")


def statuscheck(addr):    
    try:
        if os.name == "nt":
            st=os.popen("ping -n 1 "+addr).read()
            time.sleep(0.1)    
            st=str(st)
            
        elif os.name == "posix":
            st=os.popen("ping -c 1 "+addr).read()
            time.sleep(0.1)    
            st=str(st)
            
        else:
            print("Not supported your operating system.")
            raise SystemExit
        
    except:return False
    
    if 'ttl' in st or 'TTL' in st: 
        return True
    
    else: return False


def logger():
    with open(f"{srv}_ping_log_{dst}.csv", 'a', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now().strftime('%D'),datetime.now().strftime('%H:%M:%S'),1])
        
    with open(f"{srv}_ping_log_{dst}.txt", "a", encoding='utf-8') as log:            
        log.writelines(f"{datetime.now().strftime('%D %H:%M:%S')} >> Ping Failed!!! (addr: {dst})\n")


if __name__ == '__main__':
    while(True):
        time.sleep(0.5)      
        if not statuscheck(dst):
            logger()

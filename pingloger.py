from datetime import datetime
import os
import time


srv=input("Set logfile name: ") or "check"
dst=input("Set destination IP addr to check: ") or "8.8.8.8"
print("Working...\n(Ctrl+C) to stop.\n")

def statuscheck(addr):    
    try:
        st=os.popen("ping -c 1 "+addr).read()
        time.sleep(0.1)    
        st=str(st)
    except:return False
    if 'ttl' in st: 
        return True
    else: return False


while(True):
    time.sleep(0.5)
    if not statuscheck(dst):
        with open(f"{srv}_ping_log.txt","a") as log:
            
            log.writelines(f"{datetime.now().strftime('%D %H:%M:%S')} >> Ping Failed!!!\n")
    


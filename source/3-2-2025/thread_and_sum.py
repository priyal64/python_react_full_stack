import threading

def process(data):
    print("threads running")
    d=sum(data)
    print("the sum is: ",d)
    
data_c=[
    list(range(0,10)),
    list(range(10)),
    list(range(2,3))
]
threads=[]
for c in data_c:
    t=threading.Thread(target=process(c))
    threads.append(t)
    t.start()
for c in threads:
    c.join()
print(" task completed!!!")
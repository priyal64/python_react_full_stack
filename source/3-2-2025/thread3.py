import threading
import time

def odd():
    lis=[]
    for i in range(10):
        if i%2==1:
            lis.append(i)
    print(lis)

def even():
    lis=[]
    for i in range(10):
        if i%2==0:
            lis.append(i)
    print(lis)



thread=threading.Thread(target=odd)
t2=threading.Thread(target=even)
thread.start()
thread.join()
print("now even numbers thread is working ")
t2.start()
t2.join()
print("i executed both threads together")
import threading 
import time
import queue

def producer(item):
    for i in range(5):
        time.sleep(1)
        q.put(i)
        print("Produced:",i)

def consumer(q):
    while(True):
        i=q.get()
        if i is None:
            break
        print("consumed:",i)

q=queue.Queue()
pr=threading.Thread(target=producer,args=(q,))
co=threading.Thread(target=consumer,args=(q,))

pr.start()
co.start()

pr.join()
q.put(None) #if i dont write this the thread(consumer thread will never stop nor the main thread will execute)
co.join()
print("Thread communication completed")


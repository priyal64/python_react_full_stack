import threading
import time
# it wont work simultaneously
# it work one after the other


def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(1)
        print(f"{threading.current_thread().name} has released the lock")

lock=threading.Lock()
thread1=threading.Thread(target=task,args=(lock,))
thread2=threading.Thread(target=task,args=(lock,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("main thread")

import threading
import time

def single_task():
    print("2nd Task started...")
    time.sleep(2) #this function's thread sleeps for 2 seconds
    print("2nd or sub task completed")
# time.sleep(2)  #main thread will sleep for 2 seconds

thread=threading.Thread(target=single_task)
thread.start()
thread.join()

print("main thread execution completed")

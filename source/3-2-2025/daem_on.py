import threading
import time

def daemon_task():
    while True:
        print("daemon thread is running!")
        time.sleep(1)


da=threading.Thread(target=daemon_task,daemon=True)
da.start()

# time.sleep(5)
print("main thread exiting")
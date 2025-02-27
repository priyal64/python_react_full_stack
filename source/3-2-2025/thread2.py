import threading
import time

print("Train is moving! from station 1(at the same time xyz calls his friend to get the medicine...)")

def medicine_purchase():
    print("purchased medicine...")
    time.sleep(2)
    print("friend reaches station 2 and gives the medicine" )

thread=threading.Thread(target=medicine_purchase)
thread.start()

# thread.join() #if i dont join what happens?
# print("xyz gets medicine and train moves")
print("waiting for medicine and train moves")
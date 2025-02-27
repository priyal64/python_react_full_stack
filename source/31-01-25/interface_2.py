from abc import ABC,abstractmethod
class mail(ABC):
    def send(self):
        pass
class email(mail):
    def send(self):
        print(" i am implementing email ")

class sms(mail):
    def send(self):
        print(" i am sending message from sms")

class whatsapp(mail):
    def send(self):
        print(" i  am sending from whatsapp")

print("example of interface")
obj1=email()
obj1.send()

obj2=sms()
obj2.send()

obj3=whatsapp()
obj3.send()
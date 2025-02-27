class customers:
    def __init__(self,nid,name):
        self.name=name
        self.nid=nid
        # self.customer_table=[id,name]
        # self.last_name=input("enter last name: ")
        # self.__email=input("enter your mail id: ")
        # self.__phone_number=input("enter phone number: ")
        # self.address=input("please enter in format like street city state then pincode: ")
class orders:
    def __init__(self,oid,order_name):
        self.oid=oid
        self.order_name=order_name
        # self.order_table=[oid,order_name]

transaction={}
customer_table=[]
order_table=[]
transaction['customerid']="orders_placed"
while(True):
    n=int(input("enter 1 for details otherwise enter 2 for stop"))
    if n==1:
        name=input("enter name of customer :")
        nid=int(input("enter id of customer: "))
        customer_table.append([name,nid])
        obj=customers(name,nid)
        order_name=input("please enter one order at a time: ")
        oid=int(input("enter order number: "))
        obj2=orders(oid,order_name)
        order_table.append([oid,order_name])
        transaction[nid]=order_name

    elif n==2:
        break


for x in transaction:
    print(x, transaction[x])
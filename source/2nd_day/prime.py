# prime number
import math
def is_prime(x):
  if(x%2==0):
    return False
  
  for i in range(3,int(x**0.5)+1,2):
    if x%i==0:
      return False
  return True

def is_prim1(x):
   if x%2==0:
      return False
   else:
    i=3
    while i<=int(x**0.5):
        if x%i==0:return False
        i+=2
    return True
def main1():
    x=int(input("enter a value"))
    if is_prime(x):
        print("yes it is a prime")
    else:
        print("Not a prime number")


def main():
    n=int(input("enter a range :"))
    if(n>=2):
        x={2}
        
        for i in range(3,n+1):
            if is_prim1(i):
                x.add(i)
        print(x)
    else:
       print("there is no prime number less than 2")

def main2():
    
    while True:
       n=int(input("enter upper limit: "))
       b=int(input("enter lower limit: "))
       if(b<=n and n>=0 and b>=0):
          break
       else:
          print("enter a valid range")
    while b<=n:
        if is_prim1(b):
           print(b)
        b+=1
   
    


    
# main()
# main1()
main2()
# i=0
# for i in range(0,22,2):
#    print(i)
# prime number
import math
from cmath import inf

# prime function
def is_prime(x):
  if(x%2==0):
    return False
  
  for i in range(3,int(x**0.5)+1,2):
    if x%i==0:
      return False
  return True


def get_small_big(x):
   small=+inf
   big=-inf
   for i in range(len(x)):
    if x[i]<small:
       small=x[i]
    if x[i]>big:
       big=x[i]
   return small,big

def main():
    n=int(input("enter a range :"))
    if(n>=2):
        x=[2]
        for i in range(3,n+1):
            if is_prime(i):
                x.append(i)
        # small,big=get_small_big(x)
        print("the smallest prime number in range is: ",x[0])
        print("the largest prime number in range is: ",x[len(x)-1])
    else:
       print("there is no prime number less than 2")

# def main2():
    
#     while True:
#        n=int(input("enter upper limit: "))
#        b=int(input("enter lower limit: "))
#        if(b<=n and n>=0 and b>=0):
#           break
#        else:
#           print("enter a valid range")
#     while b<=n:
#         if is_prime(b):
#            print(b)
#         b+=1
   
    

# def main1():
#     x=int(input("enter a value"))
#     if is_prime(x):
#         print("yes it is a prime")
#     else:
#         print("Not a prime number")


    
# main()
main()
# main2()
# i=0
# for i in range(0,22,2):
#    print(i)

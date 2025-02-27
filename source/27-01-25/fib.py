# 1 1 2 3 5 8 11
#  fibonacci series
def fib(n):
    x=[]
    a=0
    b=1
    c=a+b
    x.append(a)
    x.append(b)
    x.append(c)
    c
    while(a<n):
        
        a=b
        b=c
        c=a+b
        x.append(c)
    return x

def main():
    n=int(input("enter the number : "))

    x=fib(n)
    print("the fibonacci series till n is: ",x)

main()
    


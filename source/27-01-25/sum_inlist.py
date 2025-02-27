# get the sum
def get_sum(x):
    n=len(x)
    s=0
    for i in range(n):
        s+=x[i]
    
    return s

#  get_input
def get_input(n):
    a=[]
    print("please enter n values: ")
    for i in range(n):
        ans=int(input())
        a.append(ans)
    return a


def main():
    n=int(input("enter n value: "))
    x=get_input(n)
    ans=get_sum(x)
    print("the sum of n elements is :",ans)

main()

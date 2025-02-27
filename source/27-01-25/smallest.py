# find smallest and largest number in the array
from cmath import inf
# function for both small and large number
def small(list_a):
    n=len(list_a)
    ans=+inf
    ans2=-inf
    for i in range(n):
        if list_a[i]<ans:
            ans=list_a[i]
        if list_a[i]>ans2:
            ans2=list_a[i]

    return ans,ans2

#  get input
def get_input(n):
    print("please enter n values: ")
    list_a=[]
    for i in range(n):
        ans=int(input())
        list_a.append(ans)

    return list_a

def main():
    n=int(input("please enter the size of array: "))
    list_a=get_input(n)
    
    ans,ans2=small(list_a)
    print("the smallest number in the list is :",ans)
    # print(ans)
    print("the largest is : ",ans2)

main()

    
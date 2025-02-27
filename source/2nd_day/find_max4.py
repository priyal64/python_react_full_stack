# display
def display(data):
    print("the ans is",data)

# find max
def get_max(d1,d2):
    if d1>d2:
        return d1
    elif d2>d1:
        return d2
    else:
        return d1

# get input
def get_input():
    x=float(input("enter number : "))
    return x
def main():
    s=""
    x1=get_input()
    x2=get_input()
    ans1=get_max(x1,x2)
    if ans1==x1:
        s="a"
    else:
        s="b"

        
    x3=get_input()
    ans2=get_max(x3,ans1)
    if ans2==x3:
        s="c"
    
    x4=get_input()
    ans3=get_max(x4,ans2)
    if ans3==x4:
        s="d"
    
    display(ans3)
    print("the max number is ",s)

main()

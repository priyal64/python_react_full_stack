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
    x=float(input("enter number"))
    return x
def main():
    x1=get_input()
    x2=get_input()
    x3=get_input()
    ans1=get_max(x1,x2)
    ans2=get_max(x3,ans1)
    display(ans2)

main()

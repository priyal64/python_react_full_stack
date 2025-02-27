import dis

# dis for checking internal things

# multiplyd
def mult(a,b):
    return int(a)*int(b)

def get_input():
    a=input("enter the number")
    return a

def display(a):
    print("ans is :",a)

def display_for():
    for i in range(11):
        print(i)
def main():
    # a=int(get_input())
    # b=int(get_input())
    # ans=int(mult(a,b))
    # display(ans)
    # dis.dis(mult)
    display_for()
    dis.dis(display_for)
    


main()
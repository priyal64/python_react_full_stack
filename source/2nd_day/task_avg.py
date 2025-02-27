# get the input
def get_input():
    num=input("enter number: ")
    return num
    
# display the number
def display(data):
    print("the ans is:",data)
# calcualte addition
def add(d1,d2):
    return float(d1)+float(d2)
# calculate division
def division(d1):
    return float(d1/2)
# calculating average
def calculate_average(data1,data2):
    a=add(data1,data2)
    ans=division(a)
    return ans

# calling all functions into one 
def main():
    x1=int(get_input())
    x2=int(get_input())
    x3=int(get_input())
    x4=int(get_input())
    avg1=float(calculate_average(x1,x2))
    avg2=float(calculate_average(x3,x4))
    avg=float(calculate_average(avg1,avg2))
    display(avg)
main()

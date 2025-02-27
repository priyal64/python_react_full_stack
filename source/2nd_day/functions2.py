# for display
def display(data):
    print("ans is: ",data)

# for computing area
def compute_area(length,width):
    area=int(length)*int(width)
    return area
 
# for input
def get_input():
    length=input("enter length")
    width=input("enter width")
    return length,width

# calling all functions
length,width=get_input()
area=compute_area(length,width)
display(area)
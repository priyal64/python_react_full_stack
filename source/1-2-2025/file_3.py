

# with open("example.csv","r") as file:
#     c=file.read()
#     print(c)

with open("example.csv","w") as file:
    rows=[]
    while(True):
        row=""
        n=int(input(" if you want to insert"))
        if n==1:
            print("enter 3 elements name,age,course")
            a=input("enter name: ")
            b=int(input("Enter age: "))
            c=input("enter course: ")
            row=str(a+","+str(b)+","+c)
            file.writelines(row)
        else:
            break
        
    c=file.read()
    print(c)
    # Traceback (most recent call last):
#   File "C:\Users\priya\OneDrive\Documents\capgemini\source\1-2-2025\file_3.py", line 22, in <module>
#     c=file.read()
#       ^^^^^^^^^^^
#  file.write(rows)
# TypeError: write() argument must be str, not list

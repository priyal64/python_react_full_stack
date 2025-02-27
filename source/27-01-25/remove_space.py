# splitt function
def splitting(str):
    list_a=[]
    n=len(str)
    s=""
    for i in range(n):
        if(str[i]!=" "):
            s+=str[i]
        elif(str[i]==" "):
            if(s!=""):
                list_a.append(s)
            s=""
        
    list_a.append(s)    
    print(list_a)
    return list_a
        
# check whether the words are palindrome or not
def is_pal(x):
    n=len(x)
    bo_ol=0
    j=-1
    for i in range(int(n/2)+1):
        if x[i]==x[j]:
            # statement
            bo_ol=1
            j-=1

        else:
            return False
    return True

def check(list_a):
    c=0
    for ch in list_a:
        if(is_pal(ch)):
            c+=1
    return c

        
def main():
    str=input(" enter sentence with spaces :")
    list_a=splitting(str)
    c=check(list_a)
    print(" the number of palindrome in the sentence is: ",c)

main()


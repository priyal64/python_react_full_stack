# palindrome function

def is_pal(x):
    n=len(x)
    bo_ol=0
    for i in range(int(n/2)+1):
        if x[i]==x[n-i-1]:
            # statement
            bo_ol=1

        else:
            return False
    return True

def main():
    s=input("please enter string: ")
    # if i dnot convert it to list then also the code is same
    if is_pal(list(s)): 
        print("yes the given string is palindrome")
    else:
        print("no the string is not palindrome")


main()
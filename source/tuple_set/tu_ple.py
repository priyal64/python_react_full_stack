def main():
    t1=()
    print("the empty tuple is:",t1)

    t2=(0,)
    print("one item in the tuple ",t2)

    t3=(0,'p',12,"abcd")
    print("tuple can add any item in it: ",t3)

    t4="abcd",1,232,'a'
    print("without brackets also we can initialize the tuple: ",t4)

    t5=(1,(2,3,4),5)
    print("nested tuples :",t5)

    t6=tuple('abcd')
    print("using tuple function: ",t6)

    # accessing using index
    print("value at indexed 2:",t3[2])

    print("value at indexed 1,2 in nested tuple: ",t5[1][2])

    print("using slicing operator: ",t3[0:2])
    print("using len function :",len(t6))

    print("values printing using for loop: ")
    for i in t5:
        print(i)
    t7=(1,2,3,4,5)
    print([x**2 for x in t7])
    # print("the values in t7:",t7)

    # t7.copy()
    # print("we cannot copy the whole tuple using copy: ",t7.copy())

main()
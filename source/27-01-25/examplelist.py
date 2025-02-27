# an empty list
l1=[]
print("1. An empty list: ",l1)

#  list with 4 items
l2=[0,1,2,3]
print("2. list is initialized with some values and size: ",l2)

# nested list
l3=['abc',['def','ghi']]
print("3. the given list is nested list: ",l3)

# contains list from  string
l4=list('piyal')
print("4. the given list is formed from a string :",l4)

# using range
l5=list(range(-1,5))
print("5.the list formed from a range(-1 to -5): ",l5)

# accessing an element using index
l6=[1,2,3,4,5,6]
print("6. the value at index 5 is :",l6[5])

# accessing an element from a nested list by index
l7=['x',[1,2,3,4],'y']
print("7. the value at index l[1][2] in nested list is: ",l7[1][2])

# slicing operator
l8=[1,2,3,4,4,5,6]
print("8.slicing from index 2 to 6: ",l8[2:7])
# using len function

print("9. len of list is : ",len(l8))


# all slicing and index access in nested list
l9=[1,2,[4,5,6,7],[10,30]]
print("10. the element at l[2][2]:",l9[2][2])
print("11. the element at l[1]: ",l9[1])
print("12. slicing the sublist l9[2][1:3]: ",l9[2][1:3])
print()
print()
# summary 
print("l1: ", l1)
print("l2: ",  l2)
print("l3 : ",  l3)
print("l4 :", l4)
print("l5 :", l5)
print("l6 :", l6)
print("l7 :", l7)
print("l8 :", l8)
print("l9 :", l9)
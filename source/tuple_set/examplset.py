# set1.union(set2) or set1|set2
# set1.intersection(s2) or set1&set2
# set1.difference(set2) or set1-set2
# set1.symmetric_difference(set2) or set1^set2

s0={}
print("the empty set: ",s0)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.add(6)
print("set after adding value: ",s1)

s1.remove(6)
print( "set after removing value: ",s1)
print("the set is: ",s1)
s3=s1.union(s2)
print("the union of both sets are: ",s3)

s3=s1.intersection(s2)
print("the intersection of both sets are: ",s3)

s3=s1.difference(s2)
print("the difference between them is :",s3)

s3=s1.symmetric_difference(s2)
print("the symmetric difference between them is: ",s3)

a=['abcd','pqrs','1234','pqrs','xyz','abcd']
s4=list(set(a))
print("the list after removing duplicates: ",s4)
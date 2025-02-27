
# 1
nums=[10,202,20,30,40]

# ans=[]
# for x in nums:
#     if x<202:
#         ans.append(x)
# or
ans=[x for x in nums if x<202]
print(ans)


# 2
# One line print
#Single-line method
for x in range(1, 5):  
    print(x) # 1 2 3 4  
#Single line way  
print(*range(1, 5)) # 1 2 3 4  
print(*range(1, 6)) # 1 2 3 4 5
import pandas as pd

def get_input():
    name=input("enter name of the person: ")
    dic={}
    product_list=[]
    while(True):
        n=int(input("enter 1 for giving products item else give 2: "))
        if n==1:
            product=input("enter product items")
            product_list.append(product)
        else:
            break
    dic[name]=product_list
    return dic

#def main():
n=int(input("enter how many persons data you want: "))
data={}
for i in range(n):
    dic=get_input()
    data.update(dic)
print(data)
# df=pd.DataFrame(data)
# df.to_csv('data_csv.csv',index=True)
# print(df)

# Ensure equal length 
max_length = max(len(v) for v in data.values()) if data else 0
for key in data:
    data[key] += [''] * (max_length - len(data[key]))

df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
df.to_csv('data_csv.csv', index=False)

print(df)


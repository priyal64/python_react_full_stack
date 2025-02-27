import pandas as pd

# data={
#     'name':['Alice','Bob','Charlie','David'],
#     'Age':[25,30,33,35],
#     'City':['New York','Los Angeles','chicago','Houston']

# }
data={
    'student_name':['ram','shyam','tom','mahesh','mahi'],
    'course':['maths','science','social','maths','maths'],
    'age':[17,16,17,15,16]
}

 #created csv
df=pd.DataFrame(data)
df.to_csv('from_data.csv',index=False)
print(df)
# age 
print([df[df['age']>16]])
# print(df.student_name)
# print(df.head())

# print(df.loc[0])
# groupby method and aggregate functions
print(df.groupby('course').count())

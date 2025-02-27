import pandas as pd

file=pd.read_csv('sample.csv')
# print(file) # working fine
# print(file.to_string()) # prints everything in a string

# file.to_csv('output.csv',index=False) #created csv
# json
# file.to_json('op.json') # file converted to json

# print(file['Customer Id'])

# syntax is object[columname]>value #for filtering
# file[file['Age']>30]

print(file[file['City']=='East Leonard'])

# print(file.sort_values(by='First Name',ascending=True))
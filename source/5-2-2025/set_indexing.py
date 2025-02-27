import pandas as pd

data={
    'region':['north','north','south','south','east','east'],
    'state':['Jammu','UP','Tamil Nadu','Kerala','Telangana','Andhra'],
    'year':[2021,2022,2021,2022,2021,2022],
    'profit':[95000,100000,80000,99000,90900,88000]

}

df=pd.DataFrame(data)
df.set_index(['region','profit'],inplace=True)
print(df)
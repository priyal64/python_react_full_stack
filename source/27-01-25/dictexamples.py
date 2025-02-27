# dictionary
def main():
    d1={}
    print(" the dictionary is empty: ",d1)
    d2={'name':12,'pqrs':13}
    print(" the dictionary is of size 2:",d2)

    d3={'college':{'class':203,'lab':204}}
    print(" the nested list of college is: ",d3)

    namelist=['std1','std2','std3','std4']
    rolllist=[1,2,3,4]

    d4=dict(zip(namelist,rolllist))
    print("the two list combined in dictionary are: ",d4)

    d5=dict.fromkeys(['abcd','pqrs'])
    print("the dictionary created from keys is:",d5)

    d6={'aa':2,'bb':3}
    d6.update(d5)
    print(" updated dictionary is: ",d6)

    print(d6.items())
    d7=d6.copy()
    print(" this is the copied elements from d6: ",d7)
    print("get the value from index",d6.get('aa'))
    print("only key",d6.keys())
    print("only values:",d6.values())

main()
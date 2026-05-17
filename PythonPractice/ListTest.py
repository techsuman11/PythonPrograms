#list accepts heterogeneous objects
randomList=[100,200,300,100,"A",True,30.5]
print(type(randomList))
for element in randomList:
    print(element," type: ",type(element))

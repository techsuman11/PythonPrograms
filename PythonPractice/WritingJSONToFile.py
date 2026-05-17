book={}
book["Bob"]={"name":"Bob","address":"1 Kent Street","Phone":123456}
book["Alice"]={"name":"Alice","address":"2 Kent Street","Phone":133456}
print("book dictionary: ",book)

import json

#Converting dictionary to json string
jsonString=json.dumps(book)
print("dumped json string: ",jsonString)
print("data type of dumped string jsonString object: ",type(jsonString)) #<class 'str'>

#writing the data to file
with open("book.txt","w") as f:
    f.write(jsonString)
    f.close()

#Reading the data from the file
with open("book.txt","r") as fr:
    fileContent=fr.read()
    fr.close()

print("data type of fileContent: ",type(fileContent))   #data type of fileContent:  <class 'str'>
print("fileContent: ",fileContent)

#Converts string to dictionary object
fileContentDict=json.loads(fileContent)
print("file content as dictionary: ",fileContentDict)
print("data type of fileContentDict",type(fileContentDict)) #data type of fileContentDict <class 'dict'>

BobsPhoneNumber=fileContentDict["Bob"]["Phone"] #data type of fileContentDict <class 'dict'>
print("Bobs phone number: ",BobsPhoneNumber)    #Bobs phone number:  123456

"""

Note:
The below code throws exception as the string is not a valid dictionary type

tempString="abc"
tempDict=json.loads(tempString)
print("tempDict: ",tempDict)

"""

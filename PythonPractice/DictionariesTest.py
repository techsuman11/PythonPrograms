contacts={"Suman":"+919177364637","Venkatesh":"+91900000000","Nagarjuna":"+61000000000"}
print(contacts) #{'Suman': '+919177364637', 'Venkatesh': '+91900000000', 'Nagarjuna': '+61000000000'}

#Printing using key
for personName in contacts:
    print(personName," phone number is: ",contacts[personName])

#Fetching key and value using items method
for personName,phoneNumber in contacts.items():
    print(personName," phone number is: ",phoneNumber)

#Fetching keys and converting it to list
names=contacts.keys()
print(names) #dict_keys(['Suman', 'Venkatesh', 'Nagarjuna'])
print(type(names)) #<class 'dict_keys'>
namesList=list(names)
print(namesList) #['Suman', 'Venkatesh', 'Nagarjuna']
print(type(namesList))  #<class 'list'>

phoneNumbers=contacts.values()
print(phoneNumbers) #dict_values(['+919177364637', '+91900000000', '+61000000000'])
print(type(phoneNumbers))  #<class 'dict_values'>

name="Suman"
isNamePresent=name in contacts.keys()
print(isNamePresent) #True
print("Venkat" in contacts.keys())  #False

phoneNumber="+91900000000"
isPhonePresent=phoneNumber in contacts.values()
print(isPhonePresent) #True

eachEntry=contacts.items()
print(eachEntry) #dict_items([('Suman', '+919177364637'), ('Venkatesh', '+91900000000'), ('Nagarjuna', '+61000000000')])
print(type(eachEntry)) #<class 'dict_items'>
eachEntryList=list(eachEntry)
print(eachEntryList) #[('Suman', '+919177364637'), ('Venkatesh', '+91900000000'), ('Nagarjuna', '+61000000000')]

contacts.pop("Venkatesh")
print(contacts) #{'Suman': '+919177364637', 'Nagarjuna': '+61000000000'}

contacts["Balakrishna"]="8181818181"
print(contacts) #{'Suman': '+919177364637', 'Nagarjuna': '+61000000000', 'Balakrishna': '8181818181'}

sumanPhoneNumb=contacts.get("Suman")
print(sumanPhoneNumb)  #+919177364637



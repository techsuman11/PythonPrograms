class Human:
    name=""
    age=0

    #Constructor, If we dont add any constructor, by default no arg constructor will be added
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printHuman(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def isEligibleToVote(self):
        return self.age >= 18

human1=Human("Abi",16)
print(human1.name," eligible to vote? ",human1.isEligibleToVote())

human2=Human("Ram",19)
print(human2.name," eligible to vote? ",human2.isEligibleToVote())

print(type(human1))
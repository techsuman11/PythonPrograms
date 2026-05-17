studentMarks={
    "Suman":{"Java":94,"Pega":90,"Python":70},
    "Nagarjuna":{"Java":95,"Pega":20,"Python":60},
    "Balakrishna":{"Java":96,"Pega":10,"Python":50},
}

print(studentMarks)
print(studentMarks["Suman"]) #{'Java': 94, 'Pega': 90, 'Python': 70}
print(type(studentMarks["Suman"])) #<class 'dict'>
print(studentMarks["Suman"]["Java"]) #94

studentName="Suman"
print(studentName in studentMarks) #True

subjectName="Python"
print(subjectName in studentMarks) #False

sumanMarks=studentMarks.get(studentName)
print("sumanMarks= ",sumanMarks) #sumanMarks=  {'Java': 94, 'Pega': 90, 'Python': 70}
print(studentMarks.get("ABC")) #None


for student in studentMarks:
    print("Student name: ",student)
    #print(type(student)) #<class 'str'>
    #print(studentMarks[student]) #{'Java': 96, 'Pega': 10, 'Python': 50}
    for subject in studentMarks[student]:
            print(subject," ",studentMarks[student][subject])

print("printing using items method================")
for student,marks in studentMarks.items():
    print("Student name: ",student)
    # print("Marks: ",marks) #{'Java': 94, 'Pega': 90, 'Python': 70}
    for subject,score in marks.items():
        print(subject," ",score)


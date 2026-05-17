"""
Writing content in file, and reading the file from the file,
counting the words and writing the data in new file
"""
f=open("test2.txt","w")
f.write("hello world\n")
f.write("how are you all")
f.close()

f=open("test2.txt","r")
fw=open("test3.txt","w")
for line in f: #reads line by line in the file and stores the line in line variable
    tokens=line.split()
    numberOfTokens=len(tokens)
    lineWithWordCount="words count:"+str(numberOfTokens)+" "+line
    print(lineWithWordCount)
    fw.write(lineWithWordCount)
f.close
fw.close()

# Other ways to read and write file
with open("test4.txt", "r") as f:
    print(f.read())

with open("test5.txt", "w") as f:
    f.write("hello world")


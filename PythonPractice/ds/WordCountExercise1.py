#Read poem.txt file and display word count for each word in it.
#open poem.txt file in read mode
poemFile=open("poem.txt","r")

#initiating dictionary
word_count={}
count=0
for line in poemFile:
    wordsInLine=line.split()
    for word in wordsInLine:
        if word in word_count:
            count=word_count[word]+1
            word_count[word]=count
        else:
            word_count[word]=1

print(word_count)

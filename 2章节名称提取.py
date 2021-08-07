import os, sys

text2 = open("end.doc","r",encoding="utf8")

text3 = open("Chapter名称.doc","w+",encoding="utf8")

str1 = text2.read()

a = str1.split("Chapter ")

b = len(a)


for num in range(b):
    text = "Chapter " + str(num) +".doc"
    text = open(text,"r",encoding="utf8")
    first_line = text.readline().replace(":",".").replace("?","？")
    text3.write(first_line)
        



text2.close()
text3.close()






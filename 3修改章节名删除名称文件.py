import os, sys

text2 = open("Chapter名称.doc","r",encoding="utf8")

str1 = text2.readlines()

a = len(str1)

for num in range(a):
    stra = "Chapter "+ str(num) + ".doc"
    strb = str1[num].strip() + ".doc"
    os.rename(stra,strb)
 
text2.close()

os.unlink("Chapter名称.doc")



    
    

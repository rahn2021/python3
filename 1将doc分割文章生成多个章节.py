text2 = open("end.doc","r",encoding="utf8")

str1 = text2.read()

a = str1.split("Chapter ")

b = len(a)

for num in range(b):
    text =  "Chapter " + str(num) +".doc"
    text = open(text,"w",encoding="utf8")
    text.write("Chapter " + a[num])
    text.close()





text2.close()  


text3 = open("Chapter 0.doc","r",encoding="utf8")

str2 = text3.read()

str5 = str2.replace("Chapter ","")

text3.close()

jieshao = open("Chapter 0.doc","w+",encoding="utf8")

jieshao.write(str5)

jieshao.close()

table = {ord(f):ord(t) for f,t in zip(
     u'，。！？【】（）％＃＠＆１２３４５６７８９０',
     u',.!?[]()%#@&1234567890')}
text2 = open("text2.txt","r",encoding="utf8")

end = open("end.doc","w+",encoding="utf8")

str1 = text2.read()

neirong = str1.translate(table)

a = neirong.split("\n")

b = len(a)



for num in range(b):
    num = end.write(a[num] + "\n");

text2.close()  
end.close()

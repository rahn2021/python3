#!/usr/bin/python3


text2 = open("text2.txt","r",encoding="utf8");   
end = open("end.html","w+",encoding="utf8");       
str1 = text2.read();

a = str1.strip();

b = a.split("\n");

c = len(b);
    
for num in range(c):
    num = end.write("<p>" + b[num] + "</p>");
    
    
text2.close();     
end.close();  

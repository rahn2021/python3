#!/usr/bin/python3

text1 = open("text2.txt","r",encoding="utf8");   
text2 = open("google.txt","r",encoding="utf8");
text3 = open("handex.txt","r",encoding="utf8");
text4 = open("edeg.txt","r",encoding="utf8");
end = open("end.txt","w+",encoding="utf8");      

str1 = text1.read();    
str2 = text2.read();
str3 = text3.read();    
str4 = text4.read(); 

a = str1.strip();      
b = str2.strip();
c = str3.strip();      
d = str4.strip(); 

a = a.split("\n");     
b = b.split("\n");
c = c.split("\n");     
d = d.split("\n");

str5 =len(a);
str6 =len(b);
str7 =len(c);
str8 =len(d);

print(str5)
print(str6)
print(str7)
print(str8)

for num in range(str5):
    end.write("\n\n" + a[num] 
    + "\n\ngoogle翻译-->"  + b[num] 
    + "\n\nhandex翻译-->"  + c[num] 
    + "\n\nmicrosoft翻译-->"  +d[num]);

text1.close();     
text2.close();
text3.close();     
text4.close();   
end.close() ;       



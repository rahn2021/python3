#!/usr/bin/python3


text2 = open("text2.txt","r",encoding="utf8");   
end = open("end.txt","w+",encoding="utf8");       
str1 = text2.read();

a = str1.strip();

b = a.split("\n");

print(type(b));

c = len(b);
    
for num in range(c):
    num = end.write("\n\n" + b[num]
                    .replace("apple","苹果")
                    .replace("what","什么")
                    + "\n\n");
    
    
text2.close();     
end.close();  

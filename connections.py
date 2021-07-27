#!/usr/bin/python3

text1 = open("text1.txt","r",encoding="utf8");   
text2 = open("text2.txt","r",encoding="utf8");   
end = open("end.txt","w+",encoding="utf8");      

str1 = text1.read();    
str2 = text2.read(); 	  

a = str1.strip();      
b = str2.strip();       

a = a.split("\n");     
b = b.split("\n");     

str3 =len(a);
str4 =len(b);           

print(str3);          
print(str4);           


for num in range(str3):
    end.write("\n\n"+a[num]+"\n\n" +b[num]);
    


text1.close();     
text2.close();     
end.close() ;       



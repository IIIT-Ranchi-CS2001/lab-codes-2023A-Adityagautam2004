s="Ba Ba Black Sheep"
k = len(s)
print("Length of string : ",k)
    
print("Index of e is: ",s.index("e"))    
cnt=0
for i in range(k):
    if(s[i]=='a'):
        cnt +=1
print("Number of occurence of a : ",cnt) 

print("Ta"+" "+"Ta"+s[5:])

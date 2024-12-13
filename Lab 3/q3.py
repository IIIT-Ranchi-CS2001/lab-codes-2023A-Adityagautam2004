n = int(input("Enter the number :"))
i=0
a=0
b=1
while n>=i :
    print(a, end=" ")  
    a, b = b, a + b
    i += 1 

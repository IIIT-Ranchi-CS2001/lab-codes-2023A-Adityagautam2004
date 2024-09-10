N = int(input("Inter The Number: "))
a=N
i =0 
while N > 0 :
    i+=int(N%10)
    N=N/10

print(f"{a} {i}")

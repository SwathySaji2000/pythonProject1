n=int(input("Enter the value:\t"))
fact=1
if(n==0):
    print("fact is 1:")
else:
    for i in range(1,n+1):
        fact=fact*i
print("The fact of n is",fact)
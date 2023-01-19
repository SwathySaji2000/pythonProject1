x=int(input("Enter the first list:"))
print(x)
y=int(input("Enter the second list:"))
print(y)
if(len(x)==len(y)):
    print("list are of same length")
else:
    print("list are not of same length")
if(sum(x)==sum(y)):
    print("sum of the list are of same")
else:
    print("sum are different")
print("common elements are:")
for i in list(x):
   for j in list(y):
       if(x==y):
          print(x)
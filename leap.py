a=int(input("Enter te current year"))
b=int(input("Enter the final year"))
print("Leap years are:")
for i in range(a,b):
    if i%4==0:
        print(i)


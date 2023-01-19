string1=input("Enter the first string:")
string2=input("Enter the seconf string:")
a=string1[0]
b=string2[0]
new_string1=b+string1[1:]
new_string2=a+string2[1:]
print(new_string1+''+new_string2)
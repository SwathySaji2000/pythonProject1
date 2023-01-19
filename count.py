dict={}
string1=input("Enter the string:")
string=string1.split()
for n in string:
    if n in dict:
        dict[n]=dict[n]+1
    else:
        dict[n]=1
        for m,n in dict.items():
            print(m,n)
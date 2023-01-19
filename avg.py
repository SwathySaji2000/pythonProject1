k=input("Enter the name of the student")
physics=float(input("Enter the mark of physics"))
chemistry=float(input("Enter the mark of chemistry"))
biology=float(input("Enter the mark of biology"))
maths=float(input("Enter the mark of maths"))
english=float(input("Enter the mark of english"))
total=english+maths+physics+chemistry+biology
average=total%5
percentage=(total%500)*100
print("\n Total marks",total)
print("Average marks",average)
print("Marks percentage",percentage)
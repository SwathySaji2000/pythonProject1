class time:
   def __init__(self,hour,minute,second):
    self._hour=hour
    self._minute=minute
    self._second=second
   def __add__(self,other):
     return"timeis:"+str(self._hour+other._hour)+':'+str(self._minute+other._minute)+':'+str(self._second+other._second)
h=int(input("Enter the hour:"))
m=int(input("Enter the minute:"))
s=int(input("Enter the second:"))
h1=int(input("Enter the hour:"))
m1=int(input("Enter the minute:"))
s1=int(input("Enter the second:"))
t1=time(h,m,s)
t2=time(h1,m1,s1)
print(t1+t2)

class A:   
   def __init__(self,a):
       self.a=a
   def __add__(self, o):
       return self.a+ o.a
   def __sub__(self, o):
        return self.a- o.a
ob1=A(1)
ob2=A(2)
ob3=A(5)
ob4=A(10)
ob5=A("MCA")
ob6=A (" s1")
print("sum is",ob1+ob2)
print("difference is",ob4-ob3)
print(ob5+ob6)
print(A.__add__(ob1, ob2))
print(A.__sub__(ob4, ob3))
print(A.__add__(ob5, ob6))

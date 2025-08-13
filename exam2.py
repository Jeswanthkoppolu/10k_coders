#2 output: Aclass

class A:
    def showA(self):
        print("A class")
class B(A):
    def show(self):
        print("B class")
obj=B()
obj.showA()


#3 output:class A,class B,class C

class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        super().display()
        print("class B")
class C(B):
    def display(self):
        super().display()
        print("class C")
obj=C()
obj.display()



#example
#output:classA,classC,classB

class A():
    def display(self):
        print("calss A")
class B():
    def display(self):
        print("class B")
class C(A,B):
    def dispaly(self):
        A().display()
        print("class C")
        B().display()
obj=C()
obj.dispaly()  


#4 output:100

class Base:
    def __init__(self):
        self.base_val=100
class Intermediate(Base):
    def __init__(self):
        super().__init__()
        self.inter_val=150
class Derived(Intermediate):
    def __init__(self):
        super().__init__()
        self.dev_val=200
obj=Derived()
print(obj.base_val)



#5 output:init X,init Y,init Z

class X:
    def display(self):
        print("init X")
class Y(X):
    def display(self):
        super().display()
        print("init Y")
class Z(Y):
    def display(self):
        super().display()
        print("init Z")
obj=Z()
obj.display()

#6 output:child

class parent:
    name="parent"
class child(parent):
    name="child"
obj=child
print(obj.name)


#7 output:20

class Base:
    def __init__(self):
        self.value=10
class der(Base):
    def __init__(self):
        super().__init__()
        self.value=20
obj=der()
print(obj.value)


#8 output:Arjun,101

class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
stu=student("Arjun",101)
print(stu.name)
print(stu.roll)



#9 output: classA=3,classB=2,class C=1

class A:
    def __init__(self,a):
        print("class A:",a)
class B(A):
    def __init__(self, a,b):
        super().__init__(a)
        print("class B:",b)
class C(B):
    def __init__(self, b, a,c):
        super().__init__(a, b)
        print("class C:",c)
c=C(2,3,1)

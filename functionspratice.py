#greet
def greet():
    print("hello!"+name+"welcome to 10kcoders")
name=input()    
greet()


#arithmeic operations
def arithmetic(a,b):
    c=input("enter operaters: +,-,*,/ :")
    if c=="+":
        print(f"add a and b {a+b}")
    elif c=="-":
           print(f"sub a and b {a-b}") 
    elif c=="*":
         print(f"multi a and b {a*b}")  
    elif c=="/":
         if(b!=0):
              print(f"div a and b {a/b}")
         else:
              print("can't divide")
    else:
       print("invalid operator")    
              
a=int(input()) 
b=int(input())
arithmetic(a,b)


#wish a student based on his name and branch. if branch , name didn't use then it want print "student" and "engineering"
def wish(A="student",B="engineering"):
     print(f"hello {A} hope you doing good in {B} program")
student=input()
engineering=input()
wish(student,engineering)    


# user name and age in 2035
def details(a,b):
     print(f" user name is {a} and age is {b+10} in 2035")
name=input()
age=int(input())
details(name,age)     


#display student details
def details(name,age,num,address,email,bloodgroup):
     print(f"student name:{name}")
     print(f"student age:{age}")
     print(f"student number:{num}")
     print(f"student address:{address}")
     print(f"student email:{email}")
     print(f"student blood group:{bloodgroup}")
details(name="bobby" , age=22,num=86889,address="nellore",email="bob@gmail",bloodgroup="o-")     






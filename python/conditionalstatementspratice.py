#even or odd (and) positive and negative
number=int(input("enter the number:"))
if number%2==0:
    print("given number is even")
elif  number%2!=0:
    print("given number is odd")

if number>0:
    print("given number is positive")
elif number<0:
    print("given number is negative")
else:
    print("give number is zero")  


#age group classifier
age=int(input("enter your age:"))
if age>=0 and age<= 12:
    print("kids")
elif age>=13 and age<=19:
    print("teenage")
elif age>=20 and age<=40:
    print("young")
elif age>=41 and age<=59:
    print("prime") 
else:
     print("senior citizen")


#grade evaluator
sub1=float(input("enter your marks"))
sub2=float(input("enter your marks"))
sub3=float(input("enter your marks"))
sub4=float(input("enter your marks"))
sub5=float(input("enter your marks"))
sub6=float(input("enter your marks"))

total=sub1+sub2+sub3+sub4+sub5+sub6
percantage=(total/600)*100
print("percantage:",percantage)

if percantage>=90:
    print("grade=A")
elif percantage<=89 and percantage>= 80: 
    print("grade=B")  
elif percantage<=79 and percantage>= 70: 
    print("grade=C")  
elif percantage<=69 and percantage>= 60: 
    print("grade=D")  
else:
    print("grade=E")  
                

#Triangle type checker
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a+b>c and b+c>a and c+a>b:
  if a==b==c:
    print("the triangle is Equilateral triangle")
  elif a==b or b==c or c==a:
    print("the trangle is Isosceles triangle")
  else:
    print("the triangle is Scalene triangle")


#ATM withdrawal
balance=(int(input("enter the  current balance: ")))
withdrawal=(int(input("enter amount to withdrawal:")))
if balance-withdrawal>0:
    b=balance-withdrawal
    print(f"collect your cash /remaining balance:{b}")
elif withdrawal %100!=0:
    print("enter the amount in multiples 100")    
else :
    withdrawal > balance 
    print("insufficient balance") 

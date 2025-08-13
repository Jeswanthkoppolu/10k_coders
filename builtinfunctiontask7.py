#1 convert float to integer
x=4.89
print(int(x))

#2 convert string to integer and multi with 5
x="7"
x=int(x)
y=x*5
print(y)

#3 convert integer to float
x=int(input("enter value: "))
print(float(x))

#4 convert string to float add 1
x='3.1415'
s= float(x)+1
print(s)

#5 create a complex num from img and real
a = 3.0
b = 4.5
z = complex(a, b)
print(z)  

#6 return square of complex num using complex()
a=3
b=4
z=complex(a,b)
x=z**2
print(x)


#7 round to 2 decimal place
x=6.72842
print(round(x,2))


#8 round float to nearest int
x=input("enter value: ")
y=round(float(x))
print(y)


#9 find min and max from list=[]
x=[2,5,1,9,-3,6]
print(min(x))
print(max(x))


#10 find largest of  3 numbers using max 
a=10
b=20
c=30
largest=max(a,b,c)
print(largest)


#11 find alphabetically first name from["zara","bob","alice"]
a=["zara","bob","alice"]
y=min(a)
print(y)


#12 find 2**5 using pow()
x=pow(2,5)
print(x)


#13 get base and exponent from user,return result
a=float(input("enter float value: "))
b=float(input("enter float value: "))
res=pow(a,b)
print(res)


#14 use pow (x,y,z) to find (x**y)%z with inputs x=2,y=3 ,z=5
a=2
b=3
c=5
x=pow(2,3,5)
print(x)

#15 use divmod() for 23 divisible by 5
x,y=divmod(23,5)
print(x)
print(y)


#16 write function to return quoutient and remainder
def rem(q,r):
    quoutient,remainder=divmod(q,r)
    return quoutient,remainder
a,b=rem(23,5)
print(a)
print(b)


#17convert  number to binary using repeated divmod(num,2)
num = 23
bits = []
while num > 0:
    num, remainder = divmod(num, 2)
    bits.append(str(remainder))
binary = ''.join(reversed(bits))
print(binary)


#18 print absolute value of user input number
num=float(input("enter float value: "))
print(abs(num))


# 19 get absolute difference between two value
num1=float(input("enter float value: "))
num2=float(input("enter float value: "))
print(abs(num1-num2))


#20 compute manhatta distance from (x, y )to origin
num1=10
num2=-4
num3=abs(num1)+abs(num2)
print(num3)


#21 multiply two str as int
str1="10"
str2="5"
print(int(str1)*int(str2))


#22 round pow (5 ,3)/7 to 3 decimal place explain this
x=round (pow(5,3)/7,3)
print(x)


#23 print largest absolute value from[-2,-8,3,7]
nums = [-2, -8, 3, 7]
x = max(abs(n) for n in nums)
print(x)


# 24 round float user input,then use exponent for 2
num = float(input("Enter a float number: "))
x = round(num)
y = 2 ** x
print(x)
print(y)
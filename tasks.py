#1.print digits from num with converting into string
num=1233456
if num==0:
  print(0)
else:
  digits=[]
  n=num
while n>0:
  d=n%10
  digits.append(d)
  n//=10
for i in range(len(digits)-1,-1,-1):
  print(digits[i] ,end=" ")  

#with string
numb=123456
numbstr = str(numb)
for i in range(len(numbstr)):
   print(numbstr[i],end=" ")


#2.sum of digits in given num
#witout string
num=12345
sum=0
n=abs(num)  
while n>0:
    d=n%10
    sum+=d
    n//=10
print(sum)

#with string
num = input("Enter a number: ")  
sum= 0
for ch in num:
    if ch.isdigit():  
        sum += int(ch)
print( sum)
 


#3.count digits in given number
#without string
num = int(input("Enter a number: "))
n = abs(num)  
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10 
        count += 1
print( count)

#with string
num = input("Enter a number: ")
count = 0
for i in num:
    if i.isdigit():
        count += 1
print(count)


#4.check palindrome num or not
num=input("enter number:")
if num==num[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


#6.factors for given num 
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
num = 28
print(f"Factors of {num}: {factors(num)}")

#without function
num=28
for i in range(1,num+1):
    if num % i==0:
     print(i) 


#5.check Armstrong num or not
num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = 0
for i in digits:
    total += int(i) ** power
if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#with function
def armstrong(num):
    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    return total == num
num = 153
if armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    

#7.what is neon number
def neon(num):
    square=num**2
    total=sum(int(digit)for digit in str(square))
    return total==num
num=int(input("enter number:"))
if neon(num):
    print(f"{num} is a Neon number")
else:
    print(f"{num} is not a Neon number")  
   

#without function
num = int(input("enter number:"))  
square=num**2
total=0
for i in str(square):    
  total+=int(i)
if (total==num):
    print(f"{num} is a Neon number")
else:
    print(f"{num} is not a Neon number")  
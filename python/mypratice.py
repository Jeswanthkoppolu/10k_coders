list=[1,2,3,4,5,6,7,8,9]
for i in range(len(list)):
    print(list [i])

#while loop
list1=[12,3,4,5,6,7,23,45]    
i=0
while i<len(list1):
    print(list1 [i])
    i=i+1

#nested loop
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")


for i in range(1,5):
    for j in range(1,5):
        print(i , end=" ")
    print()          


names=["bob","bar","bab","sai"] 
newlist=[x for x in names if "b" in x]        
print(newlist)

#swap 2 numbers
a="bob"
b="sai"
a,b=b,a
print(a,b)

#palindrome
palindrome="madam"
print("palindrome" if palindrome==palindrome[::-1] else "not a palindrome")

#reverse
reverse="booby"
print(reverse[::-1])

#randomnumber
import random
otp = random.randint(1000,9999)
print(otp)
enterotp=int(input())
if enterotp== otp:
    print("verified")
else:
    print("invalid")    



x=int(input("enter number:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j , end=" ")
    print()


#even or odd
a=int(input())
if a%2 == 0:
  print("even number")
else:
    print("odd number")

#print even numbers
b=int(input())
for i in range (1,b):
    if i%2==0:
     print("even numbers:",i)

#odd numbers     
b=int(input())
for i in range (1,b):
    if i%2!=0:
     print("odd numbers:",i)

#sum of numbers
numb=(input("enter numbers by space "))  
sum=list(map(int , numb.split())) 
total=0
for i in sum:
 total+=i
print(total)


#sum of numbers user input type
numb=input("enter number by space:")
numlist=numb.split()
total=sum(int(n) for n in numlist)
print(total)

  
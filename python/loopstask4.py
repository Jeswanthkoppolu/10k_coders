#Conditional statements:
#1. Check Even or Odd
num=int(input("enter number: "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")    


#2. Age Group Classifier 
age=int(input("enter your age: "))  
if(age<13):
    print("Child") 
elif (age>=13 and age<=19):
    print("Teen")
elif(age>=20):
    print("Adult")  


#3. Check if a given number is positive, negative, or zero
num=int(input("enter number: "))
if num==0:
    print("given number is zero")
elif num<=0:
    print("given number is negative")
elif num>=0:
    print("given number is positive")        
         

#4.Check if a number is divisible by both 3 and 5
num=int(input("enter number: "))
if num%3==0 and num%5==0:
    print("given number is divisible by both 3 and 5")
else:
    print("given number is not divisible by 3 and 5")  


#5.Find Largest of Two Numbers
a=int(input("enter number: "))
b=int(input("enter number: "))
if a>b:
    print(f"{a} is largest number")
elif b>a:
    print(f"{b} is largest number")    
else:
    print("both numbers are equal")    


#6. Triangle Validity Checker
side1=int(input("enter number1: "))
side2=int(input("enter number2: "))
side3=int(input("enter number3: "))
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print("The sides form a valid triangle")
else:
    print("The sides don't form a valid triangle")    


#loops
#1. Print each character of a string
str=input("enter any words: ")
for i in str:
    print(i,end=" ")


#2. Sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("The sum of the first 10 natural numbers is:", total)


#3. Print even numbers from 1 to 20
for i in range(2,21,2):
    print(i)


#4. Print elements in a list
list=["pen", "pencil", "eraser"]
for i in list:
    print(i,end=" ")


#5. Print common elements in two lists    
list1=["bob","sai","bar"]
list2=["bob","suri","surya"]
for i in list1:
    if i in list2:
        print(i,end=" ")

#6. Print all elements in a set   
set = {"apple", "banana", "cherry"}
for i in set:
    print(i,end=" ")


#7. Count how many items are in a set using a loop
set={"bob","suri","surya","sai","bar"}
count=0
for i in set:
    count+=1
print("Number of items in the set:",count)


#8. Print all keys and values in a dictionary
person = {"name": "Alice", "age": 25, "city": "Delhi"}
for i in person:
    print(i,":",person[i])


#9. Count how many values in a dictionary are greater than 50
scores = {"math": 45, "english": 55, "science": 80, "history": 40}
for i in scores:
    if scores[i]>50:
        print(i,":",scores[i])


#10. Create a new dictionary with only items where the value is even
data = {"a": 1, "b": 4, "c": 6, "d": 3}
new={}
for key, value in data.items():
    if value%2==0:
        new[key]=value
print(new)        
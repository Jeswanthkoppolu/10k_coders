#1 multiple of 3,5,or both
x=int(input("enter number: "))
if x%3==0 and x%5==0:
    print("mult by 3 & 5")
elif x%3==0:
    print("mult of 3")
elif x%5==0:
    print("mult of 5")

#2 check palindrome 
x=input("enter number: ")
if x==x[::-1]:
    print("number is palindrome")
else:
    print("not a palindrome")
    

#3 sum of all even numbre  in list  
num=input("enter number: ")
num1=list(map(int,num.split()))
count=0
for i in num1:
    if i%2==0:
     count += i
print(count)
    

#4 reverse number    
x=input("enter number: ")
print(x[::-1])


#5 fibonacci series
num=int(input("enter number: "))
a=0
b=1
while a<=num:
    print(a,end="")
    a,b=b,a+b

#another method
start=int(input("starting number: "))   
ending=int(input("ending number: "))
a,b=0,1
while a < ending:
    if a>start:
        print(a,end="") 
    a,b=b,a+b


#
a=[0]*3
a[1]=5
print(a) 

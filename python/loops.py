for i in range(2,3):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")

def mul(num):
    for x in range(1,11):
        print(f"{num} x {x}={num*x}")    
mul(5) 

#square
def sq(num):
    for i in range(num):
        print(f"{num**i*2}")
sq(2)        

# square for even and cude for odd with functions
def sq(num):
    for i in range(1,num):
        if num%2==0:
          print(i**2)
        else:  
            print(i**3)  
sq(6)

#square for even and cude for odd
num=int(input)
for i in range(1,num):
        if num%2==0:
          print(i**2)
        else:  
            print(i**3)



for i in range(1,21):
    if i%2==0 and i%3==0:
        print(f"{i} - fizzbuzz") 
    elif i%3==0:
        print(f"{i} - buzz")              
    elif i%2==0:
        print(f"{i} - fizz")   


#sum of numbers  
num=10
sum=0
for i in range(1,num+1):
   sum += i
print(sum)

#square of nartual numbers
num=10
sum=0
for i in range(1,num+1):
   sum=i*i
   print(sum)

#skip one number
for i in range(1,20,2):   
 print(i)


#dic in loop
dict={"name":"bob","age":"22","address":"nellore"}
for x in dict:
    print(x,dict[x])
    print(f"{x}:{dict[x]}")


#perfect square
for i in range(1,101):
    if int(i**0.5)**2==i: 
      print(i)    

#another method
import math
for i in range(1, 101):
    if math.isqrt(i) ** 2 == i:
        print(i)

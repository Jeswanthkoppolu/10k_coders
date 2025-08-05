def evenorodd(number):
    if (number % 2 == 0):
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

evenorodd(4)   
evenorodd(7)  


#sum of numbers using functions
def sum_numbers(num):
    total = sum(num)
    print(f"The sum is: {total}")
sum_numbers([10, 20, 30])


#leap year
def leapyear(year):
    leap="not a leap year"
    if(year%4==0 and year%100!=0 or year%400==0):
      leap="leap year"
    return(leap) 
year=(int(input()))
print(leapyear(year))


#Arbitrary Arguments, *args
def stationary(*price):
   print("total count of items:",len(price))
   print(sum(price))
stationary(1,2,4,5,67,35) 


#cheking number prime are not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int (n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#printing prime number 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


limit = int(input())
print(f"Prime numbers up to {limit} are:")
for num in range(2, limit + 1):
    if is_prime(num):
        print(num, end=' ')


#Armstrong number 

num = int(input("Enter a number: "))
original = num
temp = num
count = 0
while temp > 0:
    temp = temp // 10
    count += 1
temp = num
powers = 0
while temp > 0:
    digit = temp % 10
    powers += digit ** count
    temp = temp // 10
if powers == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")


#neon number
n = int(input("Enter a number: "))
square = n * n
sum = 0
while square > 0:
    digit = square % 10
    sum += digit
    square = square // 10
if sum == n:
    print(n, "is a Neon number.")
else:
    print(n, "is not a Neon number.")
    

#sunny number
n = int(input("Enter a number: "))
next_num = n + 1
i = 1
perfectsquare = False
while i * i <= next_num:
    if i * i == next_num:
        perfectsquare = True
        break
    i += 1
if perfectsquare:
    print(n, "is a Sunny number.")
else:
    print(n, "is not a Sunny number.")



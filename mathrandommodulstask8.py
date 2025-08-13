#1. Generate 5 random floats between 0 and 1.
import random
randomfloats = [random.random()for i in range(0,5)]
print( randomfloats)


#2. Dice roll simulator using random.randint.
import random
diceroll = random.randint(1, 6)
print( diceroll)

#3. Convert 90 degrees to radians.
import math
radians = math.radians(90)
print(radians)

#4. Factorial of a user-given number.
import math
number = int(input("Enter a number: "))
factorial = math.factorial(number)
print(f"Factorial of {number} is:", factorial)

#5. Shuffle a list of 10 integers.
import random
numbers = list(range(1, 11))
random.shuffle(numbers)
print(numbers)


#1. Lottery draw of 6 unique numbers from 1 to 49.
import random
lotterynumbers = random.sample(range(1, 50), 6)
print( sorted(lotterynumbers))

#2 Approximate using Monte Carlo.
import random
def approximatepi(numsamples=100000):
    insidecircle = 0
    for i in range(numsamples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            insidecircle += 1
    return 4 * insidecircle / numsamples

piapprox = approximatepi()
print("Approximated Pi:", piapprox)


#3 Calculate compound interest using math.pow.
import math
principal = 1000    
rate = 0.05          
times = 12
years = 5           
amount = principal * math.pow((1 + rate / times), times * years)
print("Compound Interest Total:", round(amount, 2))


#4 Trigonometry calculator using degrees.
import math
angle_deg = 30
angle_rad = math.radians(angle_deg)
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)
print(f"sin({angle_deg}) = {sin_val}")
print(f"cos({angle_deg}) = {cos_val}")
print(f"tan({angle_deg}) = {tan_val}")


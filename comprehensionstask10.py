#prefectsquare 
import math
perfectsquares = [i for i in range(1, 50) if math.isqrt(i)**2 == i]
print(perfectsquares)


#neon number
for n in range(1, 51):
    if sum([int(d) for d in str(n * n)]) == n:
        print(f"{n} is a Neon Number")

#sunny number
import math
sunnynumbers = [n for n in range(1, 101) if math.isqrt(n + 1) ** 2 == n + 1]
print(sunnynumbers)


#reversed string
str=["hi","this","is","bob"]
rev=[str[::-1] for str in str]
print(rev)
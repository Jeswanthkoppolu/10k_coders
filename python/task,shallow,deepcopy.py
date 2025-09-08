#fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
terms = 10
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=' ')

#recursive  
def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_sum(item)  
        else:
            total += item
    return total
x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
print("Total Sum:", recursive_sum(x))


#shallow copy
import copy
num = [[1, 2], [3, 4]]
a = copy.copy(num)
a[0][0] = 999
print(num)
print(a)

score_board={'score':{'runs':144,'wickets':3,'overs':15.5}}
bob=copy.copy(score_board)
jes=copy.copy(score_board)
jes['score']['runs']+=6
print(score_board)
print(bob)
print(jes)


#deepcopy
num = [[1, 2], [3, 4]]
a = copy.deepcopy(num)
a[0][0] = 999
print(num)
print(a)


pubg={'score':{'kills':0,'health':100}}
a=copy.deepcopy(pubg)
b=copy.deepcopy(pubg)
c=copy.deepcopy(pubg)
a['score']['kills']+=4
b['score']['health']-=25
print(pubg)
print(a)
print(b)
print(c)

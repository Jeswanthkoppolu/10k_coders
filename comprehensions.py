            
def armstrong(num):
    a=num
    b=num
    count=0
    while a>0:
        a=a//10
        count+=1
    a=num
    sum=0
    while a>0:
        c=a%10
        sum+=c**count
        a=a//10
    if b==sum:
        return True
    else:
        return False
armstrongnum=[i for i in range (100,1001) if armstrong(i)]
print("armstrong number from 100 to 1000:",armstrongnum)


#prime numbers
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
op=tuple(x for x in range(2,51)if is_prime(x))
print (op)



#nested loop
op=["bob","bar","sai"]
for x in op:
    rev=""
    for i in range(len(x)-1,-1,-1):
        rev+=i[x]
    print(rev)    
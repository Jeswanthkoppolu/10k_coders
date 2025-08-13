fruits=["apple","mango","banana"]
print(fruits)
print(fruits[0:-1])
fruits[1]=("pineapple")
print(fruits)


x=["harish","naresh","suresh","mahesh"]
print(id(x))
x[2]=("kiran")
print(x)
print(id(x))


data=[1,2,[4,5],[6,7],8,["something"]]
print(data[1])
print(data[2][0])
print(data[3][1])
print(data[5][0][2])


mixed=[1,2,"hi",12.5,True]
print(mixed[0],type(mixed[0]))
print(mixed[1],type(mixed[1]))
print(mixed[2],type(mixed[2]))
print(mixed[3],type(mixed[3]))
print(mixed[4],type(mixed[4]))

 


#print the second lowest number from list
students=[]  
soc=[]  
for _ in range(int(input())):
    name = input()
    score = float(input())
    soc.append(score)
    students.append([name, score])
m=sorted(students)
k=sorted(soc)

for i in k:
     if i != k[0]:
         q=i
         break 
print(q)

b=[]
for j in m:
    
     if q==j[1]:
         b.append(j[0])
for i in b:
     print(i)
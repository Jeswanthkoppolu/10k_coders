# list--->[]
#tuples---->()
#set---->{}
#dictionary--->{}

fruits=["apple","banana","orange"," "]
ids=[1,2,3,4]
prices=[125.67,256.2,450.2,116.22]
mixed=[1,2,"hi",12.5,True]
str=("hello world")

fruits[3]="pineapple"
print(id(fruits))
print(fruits)


str1="hi"
str2="gud mrng"
str3= str1+str2+"bye"
print(str3)

list=[1,2,"hi","hello","somthing",[1,2,3],5,67]
list1=list+["python"]+[12]
print(list1)

print(type(fruits))
print(type(ids))
print(type(prices))
print(type(mixed))

print(f"length of fruits collections:{len(fruits)}")
print(ids)
print(fruits[-1])
print(str[-1])

ip=[1,2,[4,5],[6,7],8,"something"]
print(ip[2][1])
print(ip[5][5])


thislist=["bob","mur","sen"]
tropical=["bar","sai"]#adding into list
thislist.extend(tropical)
print(thislist)


thislist.remove("sen")
print(thislist)
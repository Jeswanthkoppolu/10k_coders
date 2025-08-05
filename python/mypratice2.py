# #input=#Hash#to#Front
# #output=###MoveHashtoFront
# a=input()
# x=a.count("#")
# a=a.replace("#","")
# print("#"*x+a)


# #input=1 2 2 3 3 4 4
# #output=1=1 ,2=2,3=3,4=2
# num=list(map(int,input().split()))
# dup=[]
# for i in num:
#     if (i not in dup):
#         dup.append(i)
#         print("{}occurs, {}times".format(i,num.count(i)))
 

# #A function is there which tells how many dealerships there are and the total number of cars in each dealership.
# #Your job is to calculate how many tyres would be there in each dealership.
# #input=4cars,2bikes
# #output=20
# a=int(input())
# bikes,cars=list(map(int,input().split()))
# print(cars*4+bikes*2)


# #input=aabbccc
# #output=a2b2c3
# def solve(s):
#     ans=""
#     c=1 
#     for i in range(len(s)-1):
#         if(s[i]==s[i+1]):
#             c+=1
#         else:
#             if(c==1):
#                 ans+=s[i]
#             else:
#                 ans+=s[i]+str(c)
#             c=1 
#     if(c==1):
#         ans+=s[i+1]
#     else:
#         ans+=s[i+1]+str(c)
#     return ans

# s=input()
# print(solve(s))


# #factorial of number
# num=int(input("enter number: "))
# fact=1
# while num>=1:
#     fact=fact*num
#     num=num-1
# print(fact)   


#another method
num=6
fact=1
sum=0
for i in range(1,num+1):
    fact*=i
    sum+=fact
    print(f"factorial {i}={fact}")
print(f"sum of factorials ={sum}")

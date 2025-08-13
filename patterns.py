# #1
# for i in range(1,6):
#     for j in range(i):
#         print(i ,end=" ")
#     print()  

# #2
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j ,end=" ")
#     print()  
     
# #3
# str="bobby"
# for i in range(len(str)+1):
#     print(str[:i]) 

# #4
# str = "abcde"
# for i in range(len(str)):
#     print(str[i] * (i + 1))


# #other method
# for i in range(97,102):
#     str=""
#     for j in range(97,i+1):
#         str+=chr(i)
#     print(str)        

# #5
# str="abcde" 
# for i in range(len(str)+1):
#     print(str[:i])  


# #other method
# for i in range(97,102):
#     str=""
#     for j in range(97,i+1):
#         str+=chr(j)
#     print(str)    

# #6
# str="something"
# for i in range(len(str)+1):
#     print(str[:i])


# #7
# for i in range(1,6):
#    for j in range(1,i+1):
#        print(j**2,end="")
#    print()


# #8
# for i in range(1,6):
#    for j in range(i):
#        print(i**2,end="")
#    print()


#  #9
# for i in range (5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()   


# #10
# for i in range(5,0,-1):
#    for j in range(i):
#        print(i**2,end="")
#    print()


# #11
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j**2,end="")
#     print() 


# #12
# str="something"
# for i in range(len(str)+1):
#      print(str[:len(str)-i])    


# #13
# str = "abcde"
# for i in range(len(str)):
#     print(str[:len(str)-i])


# #14
# str="abcde"
# for i in range(len(str)):
#     print(str[-(i+1)]*(len(str)-i))


# #15
# lis=["hello","welome","something","hello","apple","apple"]
# dup={}
# for x in lis:
#     if (x in dup):
#        dup[x]+=1
#     else:
#         dup[x]=1   
# print(dup) 


#16
lis1="banana"
dic={}
for i in lis1:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)            
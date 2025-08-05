# #static objects
# class person:
#     name="bobby"
#     age=22
#     gender="male"

# obj1=person()
# obj2=person()
# print(obj1)
# print(obj2)    
# print(obj1.name)
# print(obj2.age)

# obj1.name="jeswanth" #updating value in obj1
# print(obj1.name)
# print(obj2.age)
# print(person().name)#does not reflect to person class also


# #example
# class person:
#     def __init__(x,name,age,gender):
#         x.name=name
#         x.age=age
#         x.gender=gender

# obj_1=person("bobby",22,"male")
# obj_2=person("jeswanth",21,"male")

# print(obj_1.name)
# print(obj_2.age)
        

# #example
class application:
    def __init__(app,name,color,category):
        app.name=name
        app.color=color     
        app.category=category
    # def purpose(self,app_name,purpose):
    #     print(f"{app_name} is used for {purpose} ")

insta=application("insta","pink","soical media")
youtube=application("youtube","red","entertainment")
swiggy=application("swiggy","orange","food")
rapido=application("rapido","yellow","travelling")

print(insta.name,insta.color,insta.category)
print(youtube.name,youtube.color,youtube.category)
print(swiggy.name,swiggy.color,swiggy.category)
print(rapido.name,rapido.color,rapido.category)

# insta.purpose("instagram","socialmedia")
# youtube.purpose("youtube","entertainment")
# swiggy.purpose("swiggy","food")
# rapido.purpose("rapido","travelling")


#example
class Application:
    def __init__(self, name, color, category):
        self.name = name
        self.color = color     
        self.category = category

    def purpose(self):
        print(f"{self.name} is used for {self.category}.")
insta = Application("Instagram","pink" "Social Media")
insta.purpose()  # Output: Instagram is used for Social Media.



# class BankAccount:
#     def __init__(acc,name,email,phn,balance):
#         acc.name=name
#         acc.email=email
#         acc.phn=phn
#         acc.balance=balance
#     def deposit(acc,dep_amt):
#         acc.balance+=dep_amt
#     def withdrawal(acc,wd_amt):
#         acc.balance-=wd_amt
#     def checkbalance(acc):
#         print(acc.balance)
# user=BankAccount("bob","bob@gmail",8688983421,15000)
# print(user.name,user.email,user.phn,user.balance)
# user.checkbalance()
# user.deposit(1000)
# user.checkbalance()
# user.withdrawal(500)
# user.checkbalance()





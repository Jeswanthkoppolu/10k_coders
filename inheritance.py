# #inheritance
# class parent():
#     def amethod(self):
#         print("i am parent class")
#     def amethod2(self):
#         print("i am parent class 2")

# class child(parent):
#     def bmethod(self):
#         print("i am child class")
#         super().amethod2()#calling method from super class using super()

# obj=child()
# obj.bmethod()
# obj.amethod()
## obj.amethod2()

# #hierarchical 
# class user():
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
# class student(user):
#     def __init__(self,name,email,enrolledcourse):
#         super().__init__(name,email)
#         self.enrolledcourse=enrolledcourse
#     def getcourse(self):
#         print(f"{self.name} is learning {self.enrolledcourse}")
#     def removecourse(self,course):
#         self.enrolledcourse.remove(course)
#         self.getcourse()
#     def addcourse(self,course):
#         self.enrolledcourse.append(course)
#         self.getcourse()
# class instructor(user):
#     def __init__(self,name,email,course_training):
#         super().__init__(name,email)
#         self.course_training=course_training
#     def getcourse(self):
#         print(f"{self.name} is teaching {self.course_training}")

# student_obj=student("bobby","bob@gmail.com",["html","css","python","sql"])
# student_obj.getcourse()
# instructor_obj=instructor("harish","har@gmail.com",["html","python"])
# instructor_obj.getcourse()
# student_obj.removecourse("html")
# student_obj.addcourse("js")


##multiple
# class parent1:
#     def p1method(self):
#         print("i am parent 1")
# class parent2:
#     def p2method(self):
#         print("i am parent 2")   
# class child(parent1,parent2):
#     def childmethod(self):
#         print("i am child")  
#         super().p1method() 
# childcls=child()
# childcls.childmethod()
# # childcls.p1method()
# childcls.p2method()




#Single Inheritance
class parentactor():
    def __init__(self,name,p_worth):
        self.p_name=name
        self.p_worth=p_worth
        print(f"{self.p_name}is the parent")
    def p_assets(self):
        print(f"{self.p_name} assest are {self.p_worth}")
class childactor(parentactor):
    def __init__(self,p_name, c_name , p_worth):
        super().__init__(p_name,p_worth)
        self.c_name=c_name
        print(f"{self.c_name} is came by the reference of {self.p_name}")
    def c_assets(self,c_worth):
        self.c_worth=c_worth
        print(f"{self.c_name} is having worth of {self.c_worth}cr")
    def total_assets(self):
        print(f"total assets of {self.c_name} is {self.p_worth+self.c_worth}")

pk=childactor("pk","ram",150)
pk.c_assets(100)
pk.total_assets()
pk.p_assets()

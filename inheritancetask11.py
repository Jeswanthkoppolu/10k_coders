 # Single inheritance (only one child)
class user():
    def __init__(self, name, email):
        self.name = name
        self.email = email

class student(user): 
    
    def __init__(self, name, email, enrolledcourse):
        super().__init__(name, email)
        self.enrolledcourse = enrolledcourse

    def getcourse(self):
        print(f"{self.name} is learning {self.enrolledcourse}")

student_obj = student("bobby", "bob@gmail.com", ["html", "css", "python", "sql"])
student_obj.getcourse()



# Multiple inheritance
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class course_info:
    def __init__(self, enrolledcourse):
        self.enrolledcourse = enrolledcourse

class student(user, course_info):  
    def __init__(self, name, email, enrolledcourse):
        user.__init__(self, name, email)
        course_info.__init__(self, enrolledcourse)

    def getcourse(self):
        print(f"{self.name} is learning {self.enrolledcourse}")

student_obj = student("bobby", "bob@gmail.com", ["html", "css", "python", "sql"])
student_obj.getcourse()




#Multilevel inheritance
class person:
    def __init__(self, name):
        self.name = name

class user(person):  
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

class student(user):  
    def __init__(self, name, email, enrolledcourse):
        super().__init__(name, email)
        self.enrolledcourse = enrolledcourse

    def getcourse(self):
        print(f"{self.name} is learning {self.enrolledcourse}")

student_obj = student("bobby", "bob@gmail.com", ["html", "css", "python"])
student_obj.getcourse()





#Hierarchical inheritance
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class student(user):
    def __init__(self, name, email, enrolledcourse):
        super().__init__(name, email)
        self.enrolledcourse = enrolledcourse

    def getcourse(self):
        print(f"{self.name} is learning {self.enrolledcourse}")

class instructor(user):
    def __init__(self, name, email, course_training):
        super().__init__(name, email)
        self.course_training = course_training

    def getcourse(self):
        print(f"{self.name} is teaching {self.course_training}")

student_obj = student("bobby", "bob@gmail.com", ["html", "css", "python"])
student_obj.getcourse()

instructor_obj = instructor("harish", "har@gmail.com", ["html", "python"])
instructor_obj.getcourse()





#encapsulation: grouping(packing) and security
#for grouping we will uses classes
#for security we have access modifiers

# only single class (no inheritance):
# 1)public-->(name)-- we can access those variable in same class, through without any restrictions.
# 2)protected-->_name --we are not suppose to acces variables outside of class, but we can access which is not recommended.
#it is just to give discipline to developers while writting the code.
# 3)private-->__name --we can't and not allowed to access variables outside of the class but we can hack using name mangling approach(eg: classname__var)


#multiple classes with inheritnce:
# 1) protected(_var)--> we can allowed to access the variables with the classes which were being inherited & allowing inheritance.
# 2) private(__var)--> as same like before in single class. 

#public access modifier/public access specific/public member:
# if we declare an attribute in one class than we can access it anywhere in the program
  

#exaple protected
class Sample:
    def __init__(self):
       self._name="bobby"#(_ )protected
obj=Sample()
print(obj._name)#output:bobby


#example private
class Sample:
    def __init__(self):
       self.__name="bobby"#(__ )private
obj=Sample()
print(obj._Sample__name)#by adding calss name with(_ ) to it we can print the given value




# example for protected inheritance 

class Parent:
    def __init__(self):
       self._user="bobby"
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._user)#it is allowed
obj=Child()




# example for private with inheritance 

class Parent:
    def __init__(self):
       self.__user="bobby"
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._Parent__user)#it is restricted to parent class only
obj=Child()



# getter and setter methods
#  gettert: it provides read-only access to private data.
#  setter: It provides write-only or update access, often with validation.
# getter 

#example
class Sample:
    def __init__(self):
       self.__name="bobby"
    def get(self):
        print(self.__name)
obj=Sample()
obj.get()

#example
class Sample:
    def __init__(self):
        self.__name="bobby"
    def get(self):
        return self.__name
obj=Sample()
print(obj.get())



 #eaxmple
class Demo:
    def __init__(self):
        self.__name="bobby"
obj=Demo()
print(obj.__dict__) ## {'_Demo__name': 'bobby'}
obj.__name="bob"
print(obj.__dict__) ## {'_Demo__name': 'bobby', '__name': 'bob'}


#exampe
class Demo:
    def __init__(self):
        self.__name="bobby"
    def set(self):
        self.__name="bob"
obj=Demo()
print(obj.__dict__)  #{'_Demo__name': 'bobby'}
obj.set()
print(obj.__dict__)  #{'_Demo__name': 'bob'}


#exaple for getter and setter
class Demo:
    def __init__(self):
        self.__name = "bobby"

    def get_name(self):      # Getter
        return self.__name

    def set_name(self, name):  # Setter
        self.__name = name

obj = Demo()
print(obj.get_name())     # Output: bobby
obj.set_name("bob")       # Changing value via setter
print(obj.get_name())     # Output: bob

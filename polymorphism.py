# polymorphism :functions with same  method name behaving differently in different classes
#example 1
class Dog:
    def speak(self):
        return "woof"
class Cat:
    def speak(self):
        return "meow"
class Tiger:
    def speak(self):
        return "Roars"
def animal_sound(animals):
    print(animals.speak())
dog=Dog()
cat=Cat()
tiger=Tiger()
animal_sound(dog)
animal_sound(cat)
animal_sound(tiger)


#exmple2
class Sending():
    def send(self,message):
        print(f"SMS sent {message}")
class Email():
    def send(self,message):
        print(f"email sent {message}")
class Notifier():
    def send(self,message):
        print(f"noifier sent {message}")
def sendingmsg(self,message):
    self.send=message
sendingmsg(Sending(),"Hi your otp 4773")
sendingmsg(Email(),"your netflix will be expire")
sendingmsg(Notifier(),"your at risk by opening this site")
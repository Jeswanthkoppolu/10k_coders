# method overriding: replacing or changing the logic of method from  
# method overriding can be applied only when inheritance happens otherwise it won"t applicable

# class vehical:
#     def speed(self):
#         print("vehical speed is normal")
# class car(vehical):
#     def speed(self):
#         print("car speed is 120kmph")
# class cycle(vehical):
#     def speed(self):
#         super().speed()
#         print("cycle speed is 30kmph")
# obj1=vehical()
# obj2=car()
# obj3=cycle()
# obj1.speed()
# obj2.speed()
# obj3.speed()


#example
class Order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get his order num {self.order_id} with standard delivery ")

class Expressorder(Order):
    def __init__(self, customer, order_id):
        super().__init__(customer, order_id)
    def deliver(self):
        print(f"{self.customer}will get his order num{self.order_id} with express delivery in one day/same day")

obj1=Order("bobby","bob123")
obj1.deliver()#output: booby will get his order num bob123 with standard delivery
print(obj1.__dict__)#ouput: {"customer":"bobby","order_id":"bob123"}
print(Expressorder.mro)#output: <built-in method mro of type object at 0x0000028AC167D150>


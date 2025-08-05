# abstraction : hides implementation details and show only the relevant functionality to user


# #example
# from abc import ABC , abstractmethod
# class Waterfilter(ABC):
#     @abstractmethod
#     def waterpasser(self):
#         pass
# class Coldwater(ABC):
#     def waterpasser(self):
#         print("clod water served")
# class Hotwater(ABC):
#     def waterpasser(self):
#         print("hot water served")
# class Normalwater(ABC):
#     def waterpasser(self):
#         print("normal water served")
# c=Coldwater()
# c.waterpasser()


#example2
from abc import ABC ,abstractmethod
class vechical(ABC):
    @abstractmethod
    def vechicalspeed(self):
        pass
class Car(ABC):
    def vechicalspeed(self):
        print("car speed is 120kmph")
class Bike(ABC):
    def vechicalspeed(self):
        print("bike speed is 60kmph")
class Bus(ABC):
    def vechicalspeed(self):
        print("bus speed is 80kmph")
c=Car()
c.vechicalspeed()



# class BankAcount:
#     def __init__(self, name, balance, passport):
#         self._name = name
#         self._balance = balance
#         self._passport = passport

    # def print_data(self):
    #     print(self.name, self.balance, self.passport)


#     def print_protected_data(self):
#         print(self._name, self._balance, self._passport)
# account = BankAcount('Bob',10000,83965922)
# account.print_protected_data()
# print(account._name)
# print(account._balance)
# print(account._passport)
        


# class A:

 
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method' 

#     def _A__private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())


# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass
# b1 = B()
# b1.method1()


# class Car:
#     def __init__(self):
#         self._Car__speed = 0

#     def set_speed(self,speed1):
#         self._Car__speed = speed1

#     def show_speed(self):
#         return self._Car__speed

# car1 = Car()
# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed()) 


# class Car:
#     def __init__(self,):
#         self.__speed = 0


#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self,speed1):
#         self.__speed = speed1

    

# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 

# from abc import abstractmethod
# from datetime import datetime
# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime("%H:%M:%S"))
# class Alarm:
#     def on(self):
#         pass
#     def off(self):
#         pass
# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включен ')
    
# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on() 

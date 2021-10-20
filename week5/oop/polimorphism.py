#1 
from abc import ABC, abstractmethod
class Pizza(ABC):
    def __init__(self,pizza, cost):
        self.pizza = pizza
        self.cost = cost

    @abstractmethod
    def add_extra(self, ingredient):
        self.ingredient = ingredient
        print(f'{self.pizza} with extra {self.ingredient} costs {self.cost}')

class DodoPizza(Pizza):
    def add_extra(self, ingredient):
        self.cost += 50
        return super().add_extra(ingredient)


# class PapaJohnes(Pizza):
#     def add_extra(self, ingredient):
#         self.cost +=70
#         return super().add_extra(ingredient)

# pizza1 = DodoPizza('Pepperoni', 500)
# pizza1.add_extra('cheese')
# pizza2 = PapaJohnes('Margarita', 400)
# pizza2.add_extra('tomatoes')


# from abc import ABC, abstractmethod
# class Pizza(ABC):
#     def __init__(self,pizza, cost):
#         self.pizza = pizza
#         self.cost = cost

#     @abstractmethod
#     def add_extra(self, ingredient):
#         self.ingredient = ingredient
#         print(f'{self.pizza} with extra {self.ingredient} costs {self.cost}')

# class DodoPizza(Pizza):
#     def add_extra(self, *ingredient):
#         self.cost += 50 * len(ingredient)
#         return super().add_extra(ingredient)

#     def late(self,time):
#         if time >= 5:
#             print(f'You get free pizza card!!!')

# class PapaJohnes(Pizza):
#     def add_extra(self, *ingredient):
#         self.cost +=70* len(ingredient)
#         return super().add_extra(ingredient)

#     def late(self,time):
#         if time >= 100:
#             print('This pizza is free!!!')
#             self.cost = 0
#         else:
#             self.cost = self.cost - (self.cost * time / 100)



# pizza1 = DodoPizza('Pepperoni', 500)
# pizza1.add_extra('cheese', 'sause', 'Pepperoni')
# pizza1.late(5)
# pizza2 = PapaJohnes('Margarita', 400)
# pizza2.add_extra('tomatoes','bazil')
# pizza2.late(30)
# print(pizza2.cost)

# for pizza in [pizza1,pizza2]:
#     pizza.late(10)

#2
# methods:
# instanse_method(self)

# class_method(ссылка на класс)
# def some_method(cls): 
#     pass

# static_method(NONE)




class King:
    @staticmethod
    def some_static_method():
        print('I am a static_method')
    
    @staticmethod
    def move():
        print('Я хожу на 1 клетку в любую сторону ')

class Queen:
    @staticmethod
    def move():
        print('Я хожу как королева')

class Horse:
    @staticmethod
    def move():
        print('Я хожу буквой "Г"')

figure1 = King()
figure1.some_static_method()
figure2 = Queen()
figure3 = Horse()

for figure in [figure1, figure2, figure3]:
    figure.move()
        
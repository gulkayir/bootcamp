# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# list_ = [a,b,c]
# for i in list_:
#     print(len(i))



class Dog:
    def voice(self):
        print('Гав')

class Cat:

    def voice(self):
        print('Мяу')
        
barsik = Cat()
rex = Dog()

def to_pet(animal):
    animal.voice()
    
to_pet(barsik) 
to_pet(rex) 


# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self,name,last_name,company,position):
#         super().__init__(name, last_name)
        
#     def get_info(self):

#         return f'{super().get_info()}я работаю в компании {self.company} на должности {self.position}'
        

# class Student(Person):
#     def __init__(self,name, last_name,study,year):
#         super().__init__(name, last_name)

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name},я учусь в {self.study} на {self.year} курсе'

# def get_human_info(human):
#     human.get_info()

# person = Person('Иван','Петров')
# employee = Employee('Иван','Петров','Рога и копыта',"директор")
# student = Student('Иван','Петров','КГТУ','3')

# print(get_human_info(employee))
# print(get_human_info(student))
# print(get_human_info(person))



# from abc import ABC, abstractmethod
 
# class Shape(ABC):
 
#     @abstractmethod
#     def get_area(self):
#         pass
 
# class Triangle(Shape):
    
#     def __init__(self,base,height):
#         self.base = base 
#         self.height = height


#     def get_area(self):
#         return f'{self.base * self.height/2}'

# class Square(Shape):
#     def __init__(self,length):
#         self.length = length

#     def get_area(self):
#         return f'{self.length **2}'
        
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         pi = 3.141592653589793 
#         return pi * (self.radius**2)


# triangle = Triangle(5,5)
# square = Square(2)
# circle = Circle(10)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())



# class OS:
#     def __init__(self,version):
#         self.version = version
        
# class Windows(OS):
#     def __init__(self,version):
#         super().__init__(version)

#     def copy(self,text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'

# class MacOS(OS):
#     def __init__(self,version):
#         super().__init__(version)
    
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'

# class Linux(OS):
#     def __init__(self,version):
#         super().__init__(version)

#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'


# win = Windows(23)
# mac = MacOS(43)
# lin = Linux(23)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса')
# )




# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def __init__(self,level,type):
#         super().__init__(level,type)

#     def write_function(self,func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'def {self.func_name}({arg}):'

#     def create_variable(self,var_name,value):
#         self.var_name = var_name
#         self.value = value
#         return f'{var_name} = {value}'

# class JavaScript(Language):
#     def __init__(self,level,type):
#         super().__init__(level,type)

#     def write_function(self,func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'function {self.func_name}({arg}){{}};'

#     def create_variable(self,var_name,value):
#         self.var_name = var_name
#         self.value = value
#         return f'let {var_name} = {value};'


# py = Python(59,56)
# js = JavaScript(687,697)

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))


#TASK 7
# class Money:
#     def __init__(self,country, symbol):
#         self.country = country
#         self.symbol = symbol
        
        
# class Dollar(Money):
#     rate = 84.80

#     def __init__(self,country, symbol):
#         super().__init__(country,symbol)
        
#     def exchange(self,amount):
#         self.amount = amount
#         return f'$ {self.amount} равен {self.amount * Dollar.rate} сомам'


# class Euro(Money):
#     rate = 98.40

#     def __init__(self,country, symbol):
#          super().__init__(country,symbol)

#     def exchange(self,amount):
#         self.amount = amount
#         return f'€ {self.amount} равен {self.amount * Euro.rate} сомам'

# d = Dollar('USA','$')
# e = Euro('Germany','€')

# print(d.exchange(100))
# print(e.exchange(80))

# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     def __init__(self,orbit):
#         super().__init__(orbit)

#     def get_age(self,earth_age):
#         self.earth_age = earth_age
#         return f'на Меркурии ваш возраст составляет {round(self.earth_age * 365/self.orbit)} лет'
        

# class Venus(Planet):
#     def __init__(self,orbit):
#         super().__init__(orbit)
        

#     def get_age(self,earth_age):
#         self.earth_age = earth_age
#         return f'на Венере ваш возраст составляет {earth_age*365*365//self.orbit} дней '
        
        

# class Jupiter(Planet):
#     def __init__(self,orbit):
#         super().__init__(orbit)

#     def get_age(self,earth_age):
#         self.earth_age = earth_age
#         return f'на Юпитере ваш возраст составляет {earth_age*365//self.orbit*365*24} часов '
        

# m = Mercury(88)
# v = Venus(225)
# j = Jupiter(12)

# print(v.get_age(20))
# print(j.get_age(20))
# print(m.get_age(20))



    
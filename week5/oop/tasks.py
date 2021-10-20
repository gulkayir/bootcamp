# class Song:
#     def __init__(self,author,title,year):
#         self.author = author
#         self.title = title
#         self.year = year
        
#     def show_author(self):
#         print(f'the author is {self.author}')
#     def show_title(self):
#         print(f'song is {self.title}')
#     def show_year(self):
#         print(f'release if {self.year}')

# song = Song('Avicii','The Nights',2014)
# song.show_author()
# song.show_title()
# song.show_year()


# class Song:
#     def __init__(self,author,title,year):
#         self.author = author
#         self.title = title
#         self.year = year
        
#     def show_author(self):
#         print(f'Атор этой песни{self.author}')
#     def show_title(self):
#         print(f'Песня называется {self.title}')
#     def show_year(self):
#         print(f'эта песня вышла в  {self.year} году')

# song = Song('Avicii','The Nights',2014)
# song.show_author()
# song.show_title()
# song.show_year()


# class Circle():
#     color = 'blue'
#     def __init__(self,radius):
#         self.radius=radius
#         self.pi = 3.14
#     def get_area(self):
#         pi = 3.14
#         return pi*(self.radius**2)
   
# circle1 = Circle(2) 

# print(round(circle1.get_area(),2))


# class Circle:
#     color = 'blue'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.radius * self.radius * Circle.pi

# circle = Circle(2) 

# print(round(circle.get_area(),2))

# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.radius * self.radius * Circle.pi

# circle = Circle(2) 
# Circle.color = 'Красный'
# circle.get_area()


# class BankAccount:

#     def __init__(self,balance):
#         self.balance = 0




#     def withdraw(self,amount):
#         self.balance = self.balance - amount
#         print(self.balance)
        
    
    
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         print(self.balance)
        


# account = BankAccount
# account.withdraw(34,564)
# account.deposit(1000)
# print(account.balance())

# class BankAccount:

#     def __init__ (self,balance):
#         self.balance = balance
        

#     def withdraw(self, amount):
#             self.balance -= amount
#             print(f'Ваш баланс: {self.balance} сом')

#     def deposit(self, amount):
#             self.balance += amount
#             print(f'Ваш баланс: {self.balance} сом')
       
# account = BankAccount(0)
# account.deposit(1000) 
# account.withdraw(500) 


# class Taxi:
#     def __init__(self,name,cost,cost_km):
#         self.name=name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.cost = km * self.cost_km
#         return f'Такси {self.name}, стоимость поездки:{self.cost}  сом'


# taxi1 = Taxi('Namba',45,10)
# taxi2 = Taxi('Yandex',50,12)
# taxi3 = Taxi('Jorgo',50,15)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))


#wrong answer
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.radius * self.radius * Circle.pi

# circle = Circle(2) 
# Circle.color = 'Красный'
# Circle.color = 'Синий'
# circle.get_area()
# print(Circle.color)

# class Taxi:
#     def init(self,name,cost,cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
        
#     def get_total_cost(self,km):
#         self.get_total_cost = self.cost + (self.cost_km * km) 
#         return f'Такси {self.name}, стоимость поездки: {self.get_total_cost} сом'

# taxi1 = Taxi('Namba',80,10)
# taxi2 = Taxi('Yandex',60,11)
# taxi3 = Taxi('Namba',112,9)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))

# task-2

# class Circle:
#     color = 'Синий'
#     pi = 3.14
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         return self.radius**2*Circle.pi

# circle = Circle(2)
# circle.color = 'Красный'
# print(circle.get_area())
# print(circle.color)
# print(isinstance(circle, Circle))


# class Phone:
#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
        
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'
            

# contact = Phone('John','Snow','+43572302')
# print(contact.get_info())

# class Salary:
#     percent = 8
#     def __init__(self,salary,experience):
#         self.salary = salary
#         self.experience = experience
        
#     def count_percent(self):
#         return (int(self.salary*Salary.percent/100*self.experience))
        
        
# obj = Salary(10000,10)
# print(obj.count_percent()) 
# class Password:
    
#     def init(self, passwd):
#         self.passwd = passwd
    
#     def str(self):
#         return '*'*len(self.passwd)

    
#     def validate(self):
#         list_ = {'@', '#', '&', '$', '%', '!', '~', '*'}
#         if not (len(self.passwd)>=8 and len(self.passwd)<15):
#             raise Exception('пароль должен быть минимум 8 символов, но меньше 15')
#         if self.passwd.isalpha():
#             raise Exception('пароль должен содержать цифры')
#         if self.passwd.isdigit():
#             raise Exception('пароль должен содержать буквы')
        
#         if not list_&set(self.passwd):
#             raise Exception("пароль должен содержать хотя бы один из символов:\n'@', '#', '&', '$', '%', '!', '~', '*'")
#         return 'Password has been saved'
    
# passwd1 =Password()
# print(passwd1.validate())
# print(passwd1)



# class Math:
    
    
#     def init(self, num):
#         self.num = int(num)
    
    
#     def get_factorial(self):
#         i = 1
#         for k in range(1, self.num+1):
#             i = i * k
#         return i
        
#     def get_sum(self):
#         k = 0
#         for i in str(self.num):
#             k = k + int(i)
#         return k
        
#     def get_mul_table(self):
#         list_ = []
#         for i in range(1,11):
#             if i == 1:
#                 list_.append(f'{self.num} x {i} = {i*self.num}')
#             else: 
#                 list_.append(f'\n{self.num} x {i} = {i*self.num}')
#         return list_


# num = Math('11')
# print(num.get_factorial())
# print(*num.get_mul_table())
# print(num.get_sum())


# class Math:
    
#     def __init__(self, num):
#         self.num = num
    
    
#     def get_factorial(self):
#         i = 1
#         for k in range(1, self.num+1):
#             i = i * k
#         return i
        
#     def get_sum(self):
#         k = 0
#         for i in str(self.num):
#             k = k + int(i)
#         return k
    
#     def get_mul_table(self):
#         for i in range (1, 11):
#             print("%d * %d = %d" % (self.num, i, self.num * i))

# num = Math(11)
# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())

# class Class1:
#     def first(self):
#         ...
#     def second(self):
#         ...
        
        
# class Class2(Class1):
#     def third(self):
#         ...
#     def fourth(self):
#         ...
        
# obj = Class2 
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()


# class A:
    
#     def method1(self):
#         print('Основной функционал')
    
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')
    
# obj = B()
# obj.method1()

# class MyString(str):
    
#     def __init__(self,string):
#         self.string = string

#     def __str__(self):
#         return self.string
        
        
#     def append(self,ba):
#         self.string = f'{self.string}{ba}'
        
#     def pop(self):
#         list_string = list(self.string)
#         string_pop = list_string.pop()
#         self.string = ''.join(list_string)
#         return string_pop
        
 
# example = MyString('String') 
# example.append('hello') 
# print(example) 
# print(example.pop())
# print(example)



# class MyDict(dict):
    
#     def __init__(self,dict):
#         self.dict=dict
    
    
#     def get(self, key):
#         return self.dict.get(key, 'Are you kidding?')
    
            
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 


# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
        
        
# class Student(Person):
    
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
        
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')
        

# obj_student = Person('Rick',21)
# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# # obj_student.display_student() 


# class ContactList(list):

#     def __init__(self,name_list):
#         self.name = name_list

        
#     def search_by_name(self,name):
#         contacts = []
#         for contact in self.name:
#             if name in contact:
#                 contacts.append(contact)
#         return contacts
    
# all_contacts= ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 
    
    
# class SmartPhones:
#     def __init___(self, name, color, memory,battery=0):
#         self.name = name
#         self.color = color
#         self.memory = memory

        
#     def __str__(self):
#         return f'{self.name}, {self.memory}'
        
#     def charge(self,battery):
#         return self.battery + 45
        
        
# class Iphone(SmartPhones):
#     def __init___(self, name, color, memory,ios):
#         super().__init__(self, name, color,memory)
#         self.ios = ios
        
#     def send_messages(self):
#             pass
# class Samsung(SmartPhones):
#     def __init___(self, name, color, memory,android):
#         super().__init__(self, name, color,memory)
#         self.android = android
        
        
        
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7.send_imessage('hello')) 
# phone = SmartPhones() 
# print(phone) 
# print(phone.charge())


# class Pig:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print(f"I am a pig named {self.name}.")

#     def make_sound(self):
#         print("Oink")


# class Cow:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print(f"I am a cow named {self.name}.")

#     def make_sound(self):
#         print("Moo")


# pig1 = Pig("Olly")
# cow1 = Cow("Daisy")

# for animal in (pig1,cow1):
#     animal.make_sound()
#     animal.info()
    # animal.make_sound()



# class Solution(object):


#     def isPalindrome(self, x):
#         self.x = x
#         if self.x == x[::-1]:
#             print(True)
#         else:
#             print(False)
# sol = Solution()
# sol.isPalindrome('121')


# class Solution(object):


#     def isPalindrome(self,x):
#         self.x = x

#         if self.x[0] == self.x[-1]:
#             return True
#         else:
#             return False

# sol = Solution()
# print(sol.isPalindrome('12')



# class Solution(object):
#     def isPalindrome(self, x):
# #         """
#         Given an integer x, return true if x is palindrome integer.
#         An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#         """


from abc import abstractmethod

class Coder:
    count_code_time = 0

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    def __init__(self,experience,languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend
    
    def coding(self,hours):
        Coder.count_code_time += hours
       


    def get_info(self):
        return f'{self.languages_backend} разработчик, уровень: {self.experience},потрачено {self.count_code_time} часов на программирование '
        
        


class Frontend(Coder):
    def __init__(self,experience,languages_frontend):
        self.experience = experience
        self.languages_frontend = languages_frontend
    
    def coding(self,hour):
        Coder.count_code_time + hour


    def get_info(self):
        return f'{self.languages_frontend} разработчик, уровень: {self.experience},потрачено {self.count_code_time} часов на программирование '
        
class FullStack(Frontend, Backend,Coder):
    def coding(self,hours):
        Coder.count_code_time + hours



a = Backend('Junior','Python')
b = Frontend('Middle','JavaScript')
c = FullStack('Senior','Python and JS')

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 

    
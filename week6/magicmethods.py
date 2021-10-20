# class Account:
#     def __init__(self,name, balance, city):
#         self.name = name 
#         self.balance = balance
#         self.city = city
#         print('Счет создан')
    
#     def __repr__(self):
#         return f'{self.name} {self.balance}'

#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print("Пока")

# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account)) 


# class MyNumber(int):
#     def __init__(self,value):
#         self.value = value

#     def __add__(self, other):
#         return f'Это сложение и результат равен: {self.value + other}'

#     def __sub__(self, other):
#         return f'Это вычитание и результат равен: {self.value - other}'

#     def __mul__(self,other):
#         return f'Это умножение и результат равен: {self.value * other}'

#     def __truediv__(self,other):
#         return f'Это деление и результат равен: {self.value / other}'


# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)  
        
# class MyList(list):
#     def __getitem__(self, idx):
#         return super().__getitem__(idx - 1)

# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])  


# class Student:
#     def __init__(self, name, class_name, **ball):
#         self. name = name 
#         self.class_name = class_name
#         self.ball = ball

#     def __gt__(self, other):
#         return self.ball.keys > other.keys
#     def __gt__(self, other):...
#     def __le__(self, other):...

#     def __ge__(self, other):...



# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# # print(obj_student1 < obj_student2)  
# # print(obj_student1 >= obj_student2)  
# # print(obj_student1 <= obj_student2)  
    

# class Word(object):
    
#     def __new__(cls, word):
#         instance = super().__new__(cls)
#         instance.word = word.replace(' ', '')
#         return instance
        
#     def __init__(self, word):
#         self.str = self.word
#         self.len = len(self.word)

#     def __gt__(self, other):
#         return self.len > other.len
#     def __lt__(self, other):
#         return self.len < other.len
#     def __ge__(self, other):
#         return self.len >= other.len
#     def __le__(self, other):
#         return self.len <= other.len
        
# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2)



# class Kopilka:
    
#     def __init__(self):
#         self.total = 0
        
#         self.coins = []
    
#     def add_moneta(self, moneta):
#         self.total += moneta
#         self.coins.append(moneta)
        
#     def __len__(self):
#         return len(self.coins)
        
#     def __getitem__(self, key):
#         return self.coins[key]
        
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)
# print(obj)
# print(len(obj)) 
# for i in obj: 
#     print(i) 


# class Anagram(str):
#     def __init__(self,word):
#         self.word = word
        
#     def __eq__(self,other):
#         if self.word == other.word[::-1]:
#             return True
#         else:
#             return False
            
#     def __mul__(self, num):
#         word = self.word * num
#         return word[::-1]
        
# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2) 
# print(word1 * 3) 




"""offlineview"""

#1 
# class Som:
#     currencies = {
#         'USD': 84.5,
#         "EUR": 101.4,
#         "RUB": 1.06,
#         "KZT": 0.2,
#         'SOM': 1
#     }

#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __add__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} сом и {other.value * curr2}som')
#         return self.value * curr1 + other.value * curr2


#     def __sub__(self,other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} сом и {other.value * curr2}som')
#         return self.value * curr1 - other.value * curr2


# a = Som(100, 'USD')
# b = Som(25, 'EUR')
# print(a - b)
# c = Som(1500, "RUB")
# d = Som(40000, "KZT")
# print(c+d)


#2 


# class Distanse:  

#     units_m= {
#         'SM':0.01,
#         'DM': 0.1,
#         'M':1,
#         "KM": 1000,
#         "MILES": 1600


    # }  
    # def __init__(self,value, unit):
    #     self.value = value
    #     self.unit = unit

    # def __gt__(self, other):
    #     dist1 = Distanse.units_m.get(self.unit)
    #     dist2 = Distanse.units_m.get(other.unit)
    #     print(f'{self.value*dist1}M and {other.value*dist2}')
    #     return self.value*dist1> other.value*dist2

#     def __eq__(self, other):
# #         dist1 = Distanse.units_m.get(self.unit)
# #         dist2 = Distanse.units_m.get(other.unit)
# #         print(f'{self.value*dist1}M and {other.value*dist2}')
# #         return self.value*dist1 == other.value*dist2

# #     def __lt__(self, other):
# #         dist1 = Distanse.units_m.get(self.unit)
# #         dist2 = Distanse.units_m.get(other.unit)
# #         print(f'{self.value*dist1}M and {other.value*dist2}')
# #         return self.value*dist1 < other.value*dist2



# # a = Distanse(7,'KM')
# # b = Distanse(5.8,'MILES')
# # print(b>a)



# #3 EXAMPLE
# # __getattr__ -> AttributeError    when you gonna call none attribute

# class PasswordvlaidationMixin:
#     def validatepassword(self, password):
#         if len(password) >= 8 and not password.isdigit() and not password.isalpha() and not password.islower():
#             self.password = password
#             print('Password created')
#             return True
#         else:
#             print('Invlaid password')
#             return False

# class Facebook(PasswordvlaidationMixin):
#     def __init__(self, username, password):
#         if self.validatepassword(password):
#             self.username = username
#             print(f'Faebook account created for {username}!')
#         else:
#             print('Facebook account NOT created')


#     def __getattr__(self, attr):
#         print('GETATTR method worked')
#         return "You don't have a Facebook account yet"
    
#     def __getattribute__(self, name: str):
#         print('GETATTRIBUTE method worked')
#         return super().__getattribute__(name)



# user = Facebook('Isobel', 'Qwerty12345')
# print(user.password)
# print(user.last_name)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __setattr__(self, name, value):
#         if name == 'lastname':
#             print('cannot create password')
#             return None
#         return super().__setattr__(name, value)


# alice = Person('Alice')
# alice.name = 'Rosalie'
# alice.lastname = 'Callen'
# print(alice.lastname)
# alice.password = 'qwerty'
# print(alice.password)

# "user.password"  in Django you cannot get the password , because it is secured

# class Product:
#     base_price = 20000
#     def __init__(self,model,year, color):
#         self.model = model
#         self.year = year
#         self.color = color
        
        
  
#     def has_garantiya(self,year):
#         if year- self.year>2:
#             return 'Ваша гарантия истекла'
#         else:
#             return'Гарантия действительна'
    


#     @classmethod
#     def change_price(cls, rate):
#         Product.base_price = Product.base_price*rate
        
        
# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010))
# print(obj.base_price) 

# class User:
#     def __init__(self, name, lastname,email):
#         self.name = name 
#         self.lastname = lastname
#         self.email = email
        
#     @staticmethod
#     def validate_email(email):
#         if "@" in email:
#             return True
#         else:
#             return False
    
#     def __str__(self):
#         if self.validate_email(self.email):
#             return f'{self.name}:{self.email}'
#         else:
#             return 'email в неправильном формате'

#     @classmethod
#     def create_user(cls,str):
#         str = str.split(',')
#         name = str[0]
#         lastname = str[1]
#         email = str[2]
#         return cls(name,lastname, email)
    
# user1 = User.create_user('John, Snow, john@email.com') 
# user2 = User.create_user('John, Snow, johnemail.com') 
# print(user1) 
# print(user2) 


# class Makers:
#     students_count = 0

#     def __init__(self,name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi
#         self.students_count +=1

#     @classmethod
#     def new_student(cls,name, language,kpi):
#         Makers.students_count +=1
#         return cls(name,language, kpi)
        

#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'

#     def set_kpi(self, kpi):
#         self.kpi = kpi
#         return kpi
    
#     def student_count(self):
#         return len(self.students_count)

# student1 = Makers.new_student('Vlad','Pyhton', 78)
# student2 = Makers.new_student('Malik', 'JavaScript',99)
# # student3 = Makers.new_student('fjsa','fdjh;')

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.students_count) 

# class Bike:
#     def __init__(self,cost,make,model,year,min_profit):
#         self.cost = cost
#         self.make = make
#         self.model= model
#         self.year = year
#         self._sale_price = None 
#         self.sold = False 
#         self.min_profit = min_profit

#     def set_cost(self,price):
#         if price > self.cost :
#             self._sale_price = price
#         elif price < self.cost :
#             self._sale_price = price + self.min_profit 


#     def service( self, service_price):
#         self._sale_price += service_price
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         return self.cost - self._sale_price 
#     @classmethod
#     def get_default_bike(cls):
#         cost = 10000
#         make = 'Author'
#         model ='Basic ASL'
#         year = 2020
#         min_profit = 2000
#         return cls(cost,make,model,year,min_profit)
# bike = Bike.get_default_bike()    
# bike.set_cost(6000) 
# bike.service(300)
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 


# class MoneyFmt:
#     def __init__(self,amount):
#         self.amount = amount


#     def update(self,new):
#         self.amount = new
    
#     def __repr__(self):
#         return f'{ self.amount}'

        
#     @staticmethod
#     def dollarize(float_num):
#         if float_num >0:
#             return '$' + format(float_num, ',.2f')
#         else:
#             return '-$' + format(abs(float_num), ',.2f')
#     def __str__(self):
#         return self.dollarize(float_num=self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))
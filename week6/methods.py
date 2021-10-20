# class Category:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f'Category: {self.name}'


# iphone = Category('iPhone')
# samsung = Category('Samsung')
# nokia = Category('Nokia')
# xiaomi = Category('Xiaomi')

# class Condition:
#     def __init__(self,condition):
#         self.condition = condition

#     def __str__(self):
#         return f'Condition:{self.condition}'

# new = Condition('NEW')
# used = Condition('USED')
# repared = Condition('REPARED')


# class Phone:
#     def __init__(self,category, model,price, condition):
#         self.category = category
#         self.model = model
#         self.price = price
#         self.condition = condition

#     @classmethod
#     def create_iphone(cls,model, price, condition):
#         return cls(
#             category=iphone,
#             model=model, 
#             price=price, 
#             condition=condition
#             )

#     @classmethod
#     def create_samsung(cls,model, price, condition):
#         return cls(
#             category=samsung,
#             model=model, 
#             price=price, 
#             condition=condition
#             )
    
#     @classmethod
#     def create_nokia(cls,model, price, condition):
#         return cls(
#             category=nokia,
#             model=model, 
#             price=price, 
#             condition=condition
#             )
    
#     @classmethod
#     def create_xiaomi(cls,model, price, condition):
#         return cls(
#             category=xiaomi,
#             model=model, 
#             price=price, 
#             condition=condition
#             )


#     @property
#     def title(self):
#         return f'{self.category}, {self.model}, {self.price}, {self.condition}'



#     @staticmethod
#     def sale(percent, price):
#         x = price* percent/100
#         return x

#     def sale_price(self,percent,code):
#         sale = self.sale(percent,self.price)
#         if code.lower() == 'Makers':
#             self.price -= sale
        


#     def __repr__(self):
#         return self.title


# p1 = Phone.create_iphone('SE',78000,new)
# p2 = Phone.create_iphone('X',45000,new)
# p2.sale_price(30,input('Enter code: '))

# print(p2.price)
# print(p1.title)
# iphones_SE_new = []
# for i in range(10):
#     iphones_SE_new.append(Phone.create_iphone('SE',78000,new))
# print(iphones_SE_new)
    
# p1 = Phone.create_iphone('SE',78000,new)
# p2 = Phone.create_iphone('X',45000,new)
# p3 = Phone.create_samsung('Galaxy 9',2300, used)
# p4 = Phone.create_nokia('3310',22000,repared)
# p5 = Phone.create_xiaomi('8 Light',15000,used)
# print(p5)

# phone1 = Phone(iphone, 'SE',45000, 'NEW')
# print(phone1.category)
class Account:
    def __init__(self,name,balance,city):
        self.name = name
        self.balance = balance
        self.city = city
        print('Счет создан')
        
    def __repr__(self):
        return f'{self.name} {self.balance}'
        
    def __str__(self):
        return f'Hello {self.name} {self.balance} {self.city}'
    
    def __del__(self):
        print('Пока')
obj_account = Account("Rick", 2013, 'Bishkek')  
print(obj_account)  
print(repr(obj_account)) 

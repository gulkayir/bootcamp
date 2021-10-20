#1 
# class Person:
#     def __init__(self,name, salary ):
#         self.name = name 
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, new_salary):
#         self.__salary = new_salary


#     def get_salary(self, name): 
#         response = input(f'{name} хочет узнать вашу зарплату. Разрешить доступ?: ') .lower()
#         if response == 'yes':
#             return self.__salary
#         return 'Не скажу'

#     def set_salary(self, new_salary):
#          self.__salary = new_salary 

# person1 = Person('Stefan', 100000)
# print(person1.salary)
# person1.salary = 150000
# print(person1.salary)
# # person1.__salary = 20000
# person1.set_salary(150000)
# print(person1.get_salary('Atai'))
    




#with decprates and per_hour arguments
# class Person:
#     def __init__(self,name, hours, per_hour ):
#         self.name = name 
#         self.hours = hours
#         self._per_hour = per_hour

#     @property
#     def salary(self):
#         try:
#             return self.__salary
#         except:
#             self.__salary = self.hours * self._per_hour
#             return self.__salary




#     @salary.setter
#     def salary(self, new_salary):
#         self.__salary = new_salary
        


# person2 = Person('Lu', 12, 45)
# print(person2.salary)
# person2.salary = 900
# print(person2.salary)




#3 example

# class User:
#     def __init__(self, username, password, email) :
#         self.__username = username
#         self.__password = password
#         self.__email = email


#     @property
#     def info(self):
#         return f'{self.__username} {self.__password},{self.__email}'

# user = User('ken1', '1234', 'ken@gmail.com')
# print(user.info)

#instagram fuctional
# class Post:
#     posts = []

#     def __init__(self,title, author):
#         self.title = title
#         self.author = author
#         self.comments = []
#         self._add_to_posts()

#     @property
#     def comments_count(self):
#         return len(self.comments)


#     def add_comment(self, comment):
#         self.comments.append(comment)
#         print('COMMENT ADDED!!!')


#     @classmethod
#     def _generate_id(cls):
#         import random
#         id_ = random.randint(100,1000)
#         for post in cls.posts:
#             if id_ == post.get('id'):
#                 return cls._generate_id() 
#         return id_
       

#     def _add_to_posts(self):
#         post = {
#             'id': Post._generate_id(),
#             'title': self.title,
#             'author': self.author
#         }
#         Post.posts.append(post)
        
# post1 = Post('Python', 'Kani')
# post2 = Post('django','janat')
# post3 = Post('Google','atai')
# post1.add_comment('I love Python!')
# post1.add_comment('Python3 one love')
# print(post1.comments_count)
# print(post1.comments)
# print(Post.posts)

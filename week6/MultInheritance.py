# class IceCream:
#     def __init__(self,flavor):
#         self.flavor = flavor

#     @staticmethod
#     def melt():
#         print('I am melting...')
    
#     def change_flavor(self, new_flavor):
#         self.flavor = new_flavor

# class Cake:
#     def __init__(self, level:int):
#         self.level = level 

#     def add_extra_level(self, k=1):
#         self.level += k

# class IceCreamCake(Cake,IceCream):
#     def __init__(self, flavor:str, level:int):
#             IceCream.__init__(self, flavor)
#             Cake.__init__(self, level)
#             self.layer = self.level - 1

#     def add_extra_level(self, k=1):
#         super().add_extra_level(k=k)
#         self.layer += k


#     def melt(self):
#         super().melt()
#         self.layer -= 1
    

# obj1 = IceCreamCake('vanilla',4)
# print(obj1.level)
# obj1.add_extra_level(3)
# print(obj1.level)
# print(obj1.layer)
# obj1.melt()
# obj1.melt()
# print(obj1.layer)
# obj1.change_flavor('chocolate')
# print(obj1.flavor)





# cake1 = Cake(5)
# print(cake1.level)
# cake1.add_extra_level()
# cake1.add_extra_level()
# cake1.add_extra_level()
# print(cake1.level)

            
# ic1 = IceCream('chocolate')
# print(ic1.flavor)
# ic1.melt()
# ic1.change_flavor('strawberry')
# print(ic1.flavor)



# #2 
# class Teacher:
#     def __init__(self,subject):
#         self.subject = subject
#         self.groups = []

#     @property
#     def groups_count(self):
#         return len(self.groups)

#     def add_group(self, group:str):
#         self.groups.append(group)
#         print(f'New group {group} added')


# class Developer:
#     def __init__(self, language):
#         self.language = language
#         self.projects = []

    # def add_projects(self,new_project:str):
    #     self.projects.append(new_project)
    #     print(f'Got a new project {new_project}')

    # @property
    # def projects_count(self):
    #     return len(self.projects)


# class Mentor(Developer, Teacher):
#     def __init__(self, language):
#         super().__init__(language)
#         self.groups = []

# jannat = Mentor('Python')
# print(jannat.projects)
# print(jannat.groups)
# jannat.add_group('Python 14')
# jannat.add_group('Python Ev.14')
# jannat.add_projects('Makers courses')
# jannat.add_projects('Individual project')
# print(jannat.projects)
# print(jannat.groups)
# print(jannat.groups_count)
# print(jannat.projects_count)


# john = Developer('Python')
# john.add_projects('Online Shop')
# john.add_projects('Tesla')
# john.add_projects('Makers courses')
# print(john.projects)
# print(john.projects_count)


# john = Teacher('Math')
# print(john.groups)
# john.add_group('Kuiruk Mai')
# john.add_group('a11-1')
# print(john.groups)
# print(john.groups_count)



# class GmailMixin:
#     def gmail_validate(self, email:str):
#         if email.endswith('@gmail.com'):
#             self.email = email
#             print(f'Account for {email} created!')
#         else:
#             print("It's not a gmail account!!!")

# class Facebook(GmailMixin):
#     def __init__(self, email):
#         super().gmail_validate(email)
    
# class HackerRank(GmailMixin):
#     def __init__(self, email, username):
#         super().gmail_validate(email)
#         try:
#             self.email
#             self.username = username
#         except AttributeError:
#             print('Account not created!!')

    


# user1 = Facebook('knai@gmail.com')
# user2 = HackerRank('some@gmail.com', 'somebody')


# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return self.side**2

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#          return self.base * self.height/2

# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         super().__init__(height, base)

#     def get_volume(self):
#         return 1/3*self.base**2*self.height

# s = Square(4)
# t = Triangle(2,3)
# p = Pyramid(3,4)
# print(s.get_area())
# print(t.get_area())
# print(p.get_volume())

# class CreateMixin:
#     def create(self,task):
#         ToDo.todos.

# class DeleteMixin:
#     def delete(self,todelete):
#         ToDo.todos.pop(todelete)
#         return f'удалили {todelete}'

# class UpdateMixin:
#     def update(self, key,val):
#         ToDo.todos.update(key,val)
        
        
# class ReadMixin:
#     def read(self):
#         pass


# class ToDo(CreateMixin, DeleteMixin, UpdateMixin,ReadMixin):
#     def __init__(self) -> None:
#         pass


#     todos = {}
#     def set_deadline(self,date):
#         pass

# task = ToDo()

# task.create('wash')
# task.create('wash1')
# pr


# class Game:
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#         self.extenions = []
        
#     def get_descripition(self):
#         return f'{self.name} это инди-игра в жанре песочницы с элементами выживания и открытым миром.'
#     def get_extensions(self):
#         pass


class CreateMixin:
    
    def create(self,task,key):
        ToDo.todos[key]=task
        return print(ToDo.todos)
    
class DeleteMixin:
    
    def delete(self,key):
        b = ToDo.todos.get(key)
        ToDo.todos.pop(key)
        return f'удалили {b} задачу'
class UpdateMixin:
    def update(self,key,value):
        ToDo.todos[key] = value
        return print(ToDo.todos) 

class ReadMixin:
    
    def read(self):
        return print({k: v for k, v in sorted(ToDo.todos.items(), key = lambda item: item[1])})
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    
    todos = {}
    
    def init(self):
        pass
    
    def set_deadline(self,date):
        from datetime import datetime
        d2 = datetime.now()
        d1 = datetime.strptime(d2, "%Y-%m-%d")
        d3 = datetime.strptime(date, "%Y-%m-%d")
        return abs((d3 - d1).days)
 
obj = ToDo()
print(obj.set_deadline('2021-12-31'))
obj.create('Pomoi posudu suka',1)
obj.create('Hello Pidor',5)
obj.create('Pomoi sebya',3)
print(obj.delete(3))
obj.update(5, 'Privet')
obj.read()

# class ExtensionMixin(Game):
#     def get_extension(self,extend):
#         self.extend = extend
#         return f'Добавлено новое расширение {self.extend} для игры {self.name}.'
        
#     def remove_extension(self):
#         try:
#             self.extenions.pop(self.extend)
#             return f'{self.extend} был отключен от {self.name}'
#         except:
#             return 'Нет подключенных расширений'  

# class Student:
#     def __init__(self, name, class_name, **ball):
#         self. name = name 
#         self.class_name = class_name
#         self.ball = ball

#     def __gt__(self, other):
#         val1 = self.ball.get()
#     def __gt__(self, other):...
#     def __le__(self, other):...

#     def __ge__(self, other):...



# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# # print(obj_student1 < obj_student2)  
# # print(obj_student1 >= obj_student2)  
# # print(obj_student1 <= obj_student2)  
    


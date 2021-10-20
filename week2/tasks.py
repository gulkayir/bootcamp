# name_of_friends = ['Beta', 'Alpha', 'Fenomen', 'Eric', 'Admin']
# for name in name_of_friends:
#     if name == 'admin':
#         print(name.title())
#     else:
#         print(name.title() )

# names = ['beta', 'alpha', 'fenomen', 'eric', 'admin']
# # name= 'alpha' подумайте что вы и для чего это сделали
# for name in names:
#     if name == 'admin':
#         print("Hello " + name.title() + " would you like to see a status report?")
#     else:
#         print("Hello " + name.title() + " how are you?")

# 

#correct
# labels = ['Subaru', 'Toyota','Porche']
# for name in labels:
#         print(f'I like brand {name}')

# name_of_list = ['Butter']
# new_list = name_of_list
# for i in (new_list):
#     name_of_list.append(new_list.randint(-50, 50))
 
# print('original:', name_of_list)
# mid = len(name_of_list)//2-1
 
# print('reversed:', name_of_list[mid::-1]+name_of_list[-1:mid:-1])

# import random
 
# lst = []
# n = int(input('Введите размер списка:'))
# for i in range(n):
#     lst.append(random.randint(-50, 50))
 
# print('original:', lst)
# mid = len(lst)//2-1
 
# print('reversed:', lst[mid::-1]+lst[-1:mid:-1])


# name_of_list = ['cucumber']
# firstpart, secondpart = name_of_list[:len(name_of_list)/2], name_of_list[len(name_of_list)/2:]
# new_list = (firstpart,secondpart)
# print

# from typing import List


# c
# if (len) % 2 != 0:
#     mean_index = len() // 2
#     new_list.append([(mean_index + 1):])
#     new_list.append([(mean_index + 1):])
    
#     print(new_list)
# else:
#     mean_index = len(i) // 2
#     new_list.append(i[mean_index:])
#     new_list.append(i[:mean_index ])
    
#     print(new_list)


# name_of_list = ['cucumber lol']
# new_list =(len(name_of_list) // 2 + len(name_of_list) % 2)
# new_list = name_of_list[1:] + name_of_list[:1]
# print(new_list)

# name_of_list = ['cucumber']
# new_list = []
# for letter in name_of_list[0]:
#     new_list.append(letter)
# if len(new_list) % 2 == 0:
#     len1=int(len(new_list)/2)
#     new_list =new_list[len1:]+new_list[:len1]
# elif len(new_list) % 2 !=0:
#     len1 = int((len(new_list)+1)/2)
#     new_list =new_list[len1:]+new_list[:len1]
# print(new_list)


# list_ = ['charm', 'way']
# new_list = list_ [::-1]
# print(new_list)


# suitcase = []
# suitcase.append([1])
# suitcase.append([2])
# suitcase.append([3])
# suitcase.append([4])
# suitcase.append([5])
# suitcase.append([7])
# suitcase.pop()
# suitcase.insert(0,9)
# print(suitcase)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print([elem for elem in nums if elem < 5])

# list_ = int(input('Введите числа через запятую: '))
# ints_as_strings = values.split(',')
# ints = map(int, ints_as_strings)
# lst = list(ints)
# tup = tuple(lst)
# print('Список:', lst)
# print('Кортеж:', tup)

# string = input()
# list_ = []
# list_ = string.split(',')
# print(sorted(list_))


# list_ = []

# for i in range(54,9185):

#    if i % 5 == 0:

#        list_.append(i)

# print(list_)

# monday = {'Math', 'Literature', 'Physics'}
# tuesday = {'Russian', 'Biology','Chemistry'}
# wendesday = {'Pe',  'Biology', 'History'}
# thursday = {'Russian', 'music', 'Math'}
# friday = {'economics', 'chemistry', 'cs', 'math'}

# study_week = ( monday,tuesday,wendesday, thursday,friday)

# #a
# for i in range(len(study_week)):
#     print('LOOOP:')
#     print(study_week[i])
#     print(study_week[i+1])
#     print('EEEND')

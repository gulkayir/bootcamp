# file1 = open('task1.txt', 'r')
# print(file1.read())

# def read_lines():
# 	with open('task1.txt') as f:
# 		for i in range(5):
# 			print(f.readlines(i))


# file1 = open('task1.txt', 'r')
# Lines = file1.readlines()

# for line in Lines[0:5]:
#     print(line)

# file1 = open('task1.txt', 'r')
# Lines = file1.readlines()
# print(Lines[0:5])


# with open('task1.txt', 'r') as file:
# file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10']) 
# Lines = file.readlines()
# print(Lines[0:5])
# file.close()

# with open('dog_breeds.txt', 'r') as reader:
# line = reader.readline()
# while line != 6:
#     print(line)
#     line = reader.readline()

# with open('task2.txt', 'r') as filehandle:
#     for line in filehandle:
#         print(line)


# with open('platform.txt', 'w+') as f:
#     while True:
#         email = input('enter your email: ')
#         if not email:
#             print('student added')
#             break
#         f.write(email + '\n')


# with open('platform.txt') as f:
#     student = input('enter your email: ')
#     students = f.read()
#     if student in students:
#         print('you have an acces')
#     else:
#         print('--')

# with open('makers.txt') as f:
#     # print(f.readlines())
#     data = list(map(lambda x : x.replace('\n', ''), f.readlines()))
#     # print(data)
#     data = [name.split() for name in data]
#     # print(data)
#     max_point = 0
#     max_voice = 0
#     for list in data:
#         if int(list[1]) > max_point:
#             max_point = int(list[1])
#             best_student = list[0]
#         if int(list[-1]) > max_voice:
#             max_voice = int(list[-1])
#             fire_student = list[0]
#     print(best_student,max_point)
#     print(fire_student, max_voice)


# with open('contaxts.txt') as f:
#     contacts = f.readlines()
#     contacts = [contact.split() for contact in contacts]
#     # print(contacts)
#     contacts = {contact[0]: contact[1] for contact in contacts}
#     name = input('Enter name: ').lower()
#     print(contacts.get(name, 'no such name in contacts book'))


# from datetime import datetime
# with open('qrcode.txt', 'a') as f:
#     name = input()
#     f.write(f'{name} {datetime.now().strftime("%H:%M:%S %d-%B-%Y")}\n')
#     print()

# with open('task4.txt','r') as file:
#     print(len(file.readlines()))

# with open('task5.txt','r') as file:
#     list1 = [int(i.replace('\n','')) for i in file.readlines()]
# with open('task6.txt','w') as file:
#     file.write(f'{min(list1)}-{max(list1)}')


# list_ = ['h','e','l','l','o']

# def func(list_):
#     list_.reverse()
#     return list_
# print(func(['h','e','l','l','o']))



# dict_ ={'Tom':'black',
#         'Alice':'yellow',
#         'Sam': 'green' }
# print(dict_['Alice'])
# dict_['Alice'] = 'pink' #change meaning
# dict_['Raychel'] = 'white' # add meaning
# print(dict_)


#should contain only two elements
# my_list = [['r',1], ['o',2], ['s',3], ['e',4]]
# my_dict = dict(my_list)
# print(my_dict)

# #you can combinate

# my_list = [['r',1], ['a',2], ['s',3], ['e',4]]
# my_dict = dict(my_list, a=1, b=2, c=3) #combinated
# print(my_dict)
# тут значение а поменялось,потому что во втором словаре есть а,оно перезаписалось

# ключами словаря могут быть только одни значения
# в словаре только уникальные ключи,значения же могут повторяться

# dict_ = {1: 'Milk', '2': True, False: []}
# print(dict_)
# keys = unmutable. lists can't be keys

# dict_ ={'Tom':'black',
#         'Alice':'yellow',
#         'Sam': 'green' }
# print(dict_['Alice'])
# getting meaning be the key

#METHODS
# get(key,none)
# my_dict = {1: 'Tom', 2: 'John', 3: 'Alice'}
# print(my_dict.get(3)) you can add 'no such key in my dictionary' amd it will be printed
# print(my_dict[1])(key error)

# avgTemp = {1945: 51.75, 1946: 52.95, 1947: 51.92, 1948: 51.61}

# for year, temperature in avgTemp.items():
#     print({year} )


# test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}
  
# # printing original dictionary

  
# # Using keys() + list()
# # Getting first key in dictionary
# res = list(test_dict.keys())[0]
  
# # printing initial key
# print( str(res))
# #tasks
# a = {'x' : 1, 'y' : 2, 'z' : 3}
# res= list(a.keys())[0]
# print(str(res) )

# a = {'a': 1, 'b': 2, 'c': 1}
# b = {'f': 55}
# a.update(b)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# разбор словарей оффлайн

# test = {
#      'Atai': 15,
#      'John': 11,
#      'emy':20,
#      'Alice': 34,
#      'Nick': 23
#  }

# scores = test.values()
# print(sum(scores)/len(test))
# #среднее арифметическое


#2
# users = {
#     'kanni': 'kani@gmail.com',
#     'atai': 'elchacha@mail.ru',
#     'allie': 'allie@yahoo.com',
#     'locky': 'lock@mail.com',
#     'ann': 'annie@gmail.com',
#     'eddison': 'eddy@yahoo.com',
#     'olly': 'ollylondon@mail.com',
    
# }
# user_emails = users.values()
# total = len(users)
# gmail_count =0
# for email in user_emails:
#     if email.endswith('@gmail.com'):
#         gmail_count += 1
# print(gmail_count)   
# # total - 100%
# # gmail_count - x%
# print(f'precent of @gmail users is {round(gmail_count*100/total,2)}%')

#3
# person = {
#     "name": "Nurbolot",
#     "age": 35,
#     "languages" : ['pyhton', 'JavaScript'],
#     "children": [
#         {
#             "name": "Jannat",
#             "age": 10
#         },
#         {
#             "name": "Aselya",
#             "age":5
#         }
#     ],
# }
# # langs = person["languages"]
# # langs.append('C++')
# person["languages"].append('C++')
# # person.setdefault('salary',4000)
# person.update({'salary': 4000})
# person['wife'] = {
#     "name": 'Karen',
#     "age": 29
# }
# children=person["children"]
# children.append({'name': "New child",'age':0})
# print(len(person["children"]))
# print(person)

#4
# TIME = "10:00:00"

# students = {
#     'Kanat': "09:20:34",
#     'Aliiya': "09:20:55",
#     'Uluk': "09:09:59",
#     'Kair': "14:00:00",
#     'Emmil': "10:00:01"
# }
# late_students = []
# for key,val in students.items():
#     if val > TIME:
#         late_students.append(key)
# print(late_students)

    
# a1 = {} 
# a2 = {'fruit': 'mango', 1: [4, 6, 8]}
# a3 = dict([(1,'mango'), (2,'pawpaw')])
 
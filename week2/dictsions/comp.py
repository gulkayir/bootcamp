#1
# string = 'Azamat is an amazing actor'
# list_ = [
#     letter + '$' if not letter.lower()== 'a' else '*' 
#     for letter in string 
#     if letter != ' ']
# print(" ".join(list_))

# string = 'Azamat is an amazing actor'
# list_ = [
#     f'this is {letter} letter' if not letter.upper()== 'a' else '*' 
#     for letter in string 
#     if letter != ' ']
# print(" ".join(list_))

#2
# users = {
#     'post1': ['emy','alice','sandra','john','jennie','rose','vlad','draco','kol'],
#     'post2': ['kol','nina','ien','lexie','klaus','draco','rose','vlad',],
#     'post3': ['lily','harry','ron','norris','draco','fleur','crab','vlad','kol']
# }
# # print(list(users.values()))
# list_users = [set(list_) for list_ in users.values()]
# # print(list_users)
# candidates = list_users[0]
# for set in list_users:
#     candidates &= set
#     print(candidates.pop())
# print(list_users[0] (list_users)[1]& (list_users)[-1])








# candidates = [name for name in users ['post1']
#  if name in users ['post2']
#  and name in users['post3']]
# import random
# winner = random.choice(list(candidates))
# print(winner)

# likes = {key: len(val) for key,val in users.items()}
# most_liked_post = None
# most_likes = 0
# for post,like in likes.items():
#     if like > most_likes:
#         most_likes = like
#         most_liked_post = post

# print(most_liked_post)

#u can't use ditionary comprihation here


# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# a ={c: [s for _,s in sorted(('Timur'[g],s) for (s,g) in grades if 'Timur'[g] >= 87)] for c,grades in dict_.items()}

# # people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# people[3] = {}

# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'

# print(people[3])




dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {key:val1 for key,val in my_dict.items() for key1,val1 in my_dict[key].items()}
print(dict_)
# list_ = [num for num in range(1,101)]
# print(list_)
# #worked



# list_ = [i for i in range(1,50)if i % 2 != 0 ]
# print(list_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0 > 0 ]
# print(int_list)

# list_ =[nums**2 for nums in range(1,26)]
# print(list_)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list ]
# print(int_list)

# list_ = []
# for x in range(1,11):
#     if x % 2 ==0:
#         list_.append(x % 1 == 0)
#     elif x % 2 != 0:
#         list_.append(x % 1 != 0)

# print(list_)

# list_name = ['Addie','Liana','Kanat', 'Aliiya','luk','Klara','Emy','Ane',"Ken","Kylie"]
# new_list = ["shorter" if len(x)<4 else "longer" for x in list_name]
# print(new_list)

# dict_=dict()
# for x in range(1,11):
#     dict_[x]=x**2
# print(dict_)  
 

# n = int(input('Enter number from 1 to 10 '))
# dict_ = [n for n in range(1,500) if n % n [n]=]
# print(dict_)

# a_dictionary = {"a": 1, "b": 2}
# values = a_dictionary.values()
# values_list = list(values) 
# print(values_list)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key:list(range(1,val+1)) for key,val in a.items()}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# dict1 = {v:('even' if v%2==0 else 'odd') for (k,v) in dict_.items()}
# print(dict1)

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}


# dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

# print(dict1_tripleCond)

# new_list = list(map(int, filter(lambda x: x.isdigit() and 10000000 < int(x) < 99999999, your_list)))
# print(new_list)



# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [s for s in string_.split() if s.isdigit()]
# print( list_)

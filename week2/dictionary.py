 #1

# a = {'x': 1, 'y': 2, 'z': 1}
# print(list(a.keys())[0])

# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.pop('a'))
    
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key in a_dict:
#     print(key)

# a = {'a': 1, 'b': 2, 'c': 1}
# b = {'f': 55}
# a.update(b)
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# keys = a.keys()
# print(keys)

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# a = {'a': 1, 'b': 2, 'c': 1}
# for items in a:
#     print(items)

# a = {'a': 1, 'b': 2, 'c': 1}
# for items, value in a.items():
#     print(value)
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# a.update({"b": 2,"e": 2})
# b = a.copy()
# print(b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# keys_to_remove = ["a", "d"]
# for key in keys_to_remove:
#   a.pop(key)

# print(a)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# a.update({'apple': 0.08, 'orange': 0.06999999999999999, 'banana': 0.05})
# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# keys_to_remove = ["apple", "banana"]
# for key in keys_to_remove:
#         a.pop(key)
# print(a)


# a = {'a': 1, 'b': 2, 'c': 3} 
# b = dict((value,key) for key,value in a.items())
# print(b)
# myDict = {'a': 1, 'b': 2, 'c': 3} 
# list = []
# for i in myDict:
#         list.append(myDict[i])
#         final = sum(list)
     
# print(final)

# a = {'a': 3, 'b': 2}
# list = []
# for i in a:
#         list.append(a[i])
#         final = sum(list)
     
# print(final)

# a1 = {} 
# a2 = {'fruit': 'mango', 1: [4, 6, 8]}
# a3 = dict([(1,'mango'), (2,'pawpaw')])


# d = {
#     'value1': 5,
#     'value2': 4,
#     'value3': 3,
#     'value4': 2,
#     'value5': 1,
# }
  
# # create a variable to store result
# answer = 1
  
# # run a loop
# for i in d:
#     answer = answer*d[i]
  
# # print answer
# print(answer)


# extraTusk
# d = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for i in d:
#     result = result*d[i]
# print(result)


# string = 'pythonist'
# my_dict = {i: string.count(i) for i in string}
# print(my_dict)

# my_dict = {'x':1, 'y':2, 'z':3}
# print({v: k for k, v in my_dict.items()})


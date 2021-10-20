# dict_ = {'Мурат':24,'Эржан':21, 'Чынгыз':24, 'Алтынай':17, 'Асема':16}
# def yes():
#   for key,val  in dict_.items():
#     if val >= 17:
#       print(f'{key}, Вы можете войти в клуб')
# def no():
#       for key,val  in dict_.items():
#           if val < 17:
#               print(f'{key}, Вы не можете войти в клуб')
# yes()
# no()


# from functools import reduce
# names = ['alice', 'helen', 'john','stefan']
# result = reduce(lambda a,b:a if len(a)>len(b) else b,names)

# def count_symbols(str):
#     vowels = 0
#     consonants = 0
#     others = 0

#     for i in range(0, len(str)):
#         alp = ['a', 'и', 'о', 'у', 'ы', 'э', 'я', 'е', 'ю', 'ё']
#         ch = str[i].lower()
#         if ch.isalpha():
#             if ch in alp:
#                 vowels += 1
#             else:
#                 consonants += 1
#         else:
#             others += 1
#     return f'кол-во гласных: {vowels}, гласных: {consonants}, других символов: {others}'
# print(count_symbols('привет мир!'))

def type_(num, string):
    print(type(num))
    print(type(string))
print(type_(3, 'lemona'))

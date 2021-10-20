# a ={1,2,3}
# b = {5,6,7}
# a.update(b)
# print(a)

# Создайте множество a и попробуйте удалить один из элементов. Используйте такой метод, который не будет выдавать ошибку, если так

# a = {'hello', 'world'}
# a.remove('hello')
# print(a)

# a = {1,2,3}
# b = {3,4,5}
# print(a & b)


# a = {1,2,3}
# b = {3,4,5}
# c = {3,6,7}
# diff_set = a.difference(b,c)  
# print(diff_set)

# a = {1,2,3,4}
# b = {5,6,7,8}
# a.union(b)  
# print(a)

# a = {1,2,3,4}
# b = {5,6,7,8}
# if a <= b:
#     print('Подмножество!')

# a = {1,2,3,4}
# b = {2}
# if a>b:
#     print('Надмножество!')


# robert = {5,7,11,10,28}
# kail = {1,5,14,8,28}
# merri = {19,20,3,11,10}
# a = (kail meri)


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}

# print('kail' " " 'merri')

# if robert & kail:
#     result.append('kail')
# if robert & merri:
#     result.append('merri')

# print(' '.join(reslult))


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# result = []
# if robert & kail:
#     result.append('kail')
# if robert & merri:
#     result.append('merri')
# if result:
#     print(' '.join(result))

# tilek = {'Dodo pizza', 'FreshBox'}
# timur= {'OchakKebab', 'FreshBox'}
# alexander={'Freshbox', 'KFC'}
# elina = set()
# print(tilek &timur&alexander &elina)

# ingredients = {'сыр чеддар', 'грибы', 'соус', 'шпинат', 'колбаса'}
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.remove("Сыр чеддар")
# ingredients.add('сыр моцарелла')
# print(ingredients)

goal = int(input('Find the number: '))
if goal < 24:
    print(int(input('Too small number! try again: ')))
elif goal > 24:
    print(int(input('Too big number! try again: ')))
else:
    print(input('well! don you wanna try again?'))

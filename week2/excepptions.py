
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     print(dict_['key4'])
# except KeyError:
#     print('Нет такого ключа!')
# else:
#     print(dict_.get('key1'))

# try:
#     list_ = [1, 4, 9, 16, 25, 36] 
#     print(list_[6])
# except IndexError:
#     print('Нет такого элемента!')
# else:
#     print(list_[1])


    
# try:
#     age = int(input())
#     if age < 18:
#        raise ValueError('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1/num2
# except ValueError:
#     print('Произошла ошибка!')
# except ZeroDivisionError:
#     print('Произошла ошибка! ')
# else:
#     print(result)


# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)

#1
# products = {
# "milk": 2,
# "bread":1,
# "eggs": 20,
# "potato":35 
# }
# while products:
#     product = input('Enter product: ')
#     try:
#         products.pop(product)
#         print(products)
#     except KeyError:
#         print('There is no such product!')
#     finally:
#         print(products)
# else:
#     print('Products is empty')


#2

# gallery = []
# try:
#     memory = int(input('choose memory size: '))
# except ValueError:
#     print('enter number,nt a symbol ')
# else:
#     while memory:
#         photo = input('Make photo: ')
#         gallery.append(photo)
#         memory -= 1
#     else:
#         print(gallery)
#         raise MemoryError('Your gallery  is full!')


#3
kurs = {
    'buy':{
        'dollar': 84.50,
        'euro': 101.25,
        'rub': 1.16
    },
    'sell':{
        'dollar': 84.10,
        'euro': 102.10,
        'rub': 1.30
    }
}

while True:
    try:
        operation = input('choose operation(buy,sell): ').lower()
        data = kurs[operation]
        print(data)
    except KeyError:
        print('enter correct operation')
        continue
    else:
        valuta = input('choose (dollar,euro,rub): ')
        try:
            exchange = data[valuta]
            summa = int(input('enter convert cash: '))
            if operation == 'buy':
                result = summa * exchange
                print(f'your exchange {result} soms')
            else:
                result = summa/exchange
                print(f'your exchange {round(result,2)}{valuta}s')
            if summa <= 0:
                    raise ValueError
        except ValueError:
            print('enter correct amount')
        
        except KeyError:
            print('enter correct currency')
        else:
            end = input('do you want to continue? ').lower()
            if end == 'y' or end == 'yes':
               continue
            else:
                print('thanks,bye!')
                break

            

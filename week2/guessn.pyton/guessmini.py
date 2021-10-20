
# import random
# attempts = 0
# number = random.randint(1,20)
# name = input('Введите имя игрока:\n')
# answer = input('Хотите ли вы сыграть? ')
# while answer == 'да':
#     while True:
#         stop =input("Вы можете остановить игру,если введете 'стоп'\nНачнём {0}, я загадал число между 1 и 20.Вперёд!\n ".format(name))
#         try:
#             guess = int(stop)
#             attempts += 1
#             if guess >20 or guess<=0:
#                 attempts = attempts - 1
#                 print("Загаданно число только от 1 до 20! \n")
#                 stop = int(input('Попытайтесь снова: '))
#             elif guess < number and guess >0:
#                 print("Ваше число меньше загадонного. \n")
#             elif guess > number and guess <=20:  
#                 print(" Ваше число больше загадонного.\n")
#         except:
#             break 
#         if guess == number:
#             attempts = str(attempts)
#             print("Превосходно, {0}! Вы угадали число за {1} попыток!".format(name, attempts))
#             answer = input('Хотите ли вы сыграть ещё? ')
#             attempts = 0
#         elif answer.lower().strip() == 'нет':
#             print(f'До свидания,{name}')
#             break
#         else:
#             break

    



# import random
# name = input('enter your name:\n')
# number = random.randint(1,15)
# wish = input('do you wanna play? ')

# attempts = 0
# while True:
#     attempts += 1
#     if attempts >6:
#         print('GAME OVER')
#         wish = input('Do you wanna play again? ')
#         number = random.randint(1,15)
#         attempts = 0 
#         continue
#     if wish.lower().strip() == 'yes':
#         try:
#             guess_number = int(input(f'guess the number from 1 to 15.You have 6 atempts.Guess #{attempts}: '))
#         except ValueError:
#             print('enter number,not the symbol')
#             continue
#         if guess_number == number:
#             print(f'congratulations,{name},you won!')
#             wish = input('Do you wanna play again? ')
#             attempts = 0
#     elif wish.lower().strip() == 'no':
#         print(f'goodbye,{name}')
#         break
#     else:
#         print('enter yes or no')
#         attempts
https://github.com/gulkayir1/git_practice.git
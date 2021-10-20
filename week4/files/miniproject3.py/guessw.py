# import random

# def Hangman():
#     print ('Сыграем в виселицу!')

#     wordlist =['водопад', 'дождь', 'фрукты', 'пианино', 'ноутбук', 'завтрак', 'рост', 'карусель']
#     guessed = random.choice(wordlist)
#     guesses = 'аиеоуы'
#     turns = 5

#     while turns > 0:
#         missed = 0
#         for letter in guessed:
#             if letter in guesses:
#                 print (letter,end=' ')
#             else:
#                 print ('*',end=' ')
#                 missed= missed + 1

#             print

#         if missed == 0:
#             print ('\nТы выиграл!')
#             break

#         guess = input('\nугадайте букву: ')
#         guesses += guess

#         if guess not in guessed:
#             turns = turns -1
#             print ('\nОтвет неверный.')
#             print ('\nКоличество попыток: ', turns )
#             if turns < 5: print ('\n  |  ')
#             if turns < 4: print ('  O  ')
#             if turns < 3: print (' /|\ ')
#             if turns < 2: print ('  |  ')
#             if turns < 1: print (' / \ ')
#             if turns == 0:
#                 print ('\n\nВы проиграли. Правильный ответ: ', guessed)

# playagain = 'да'
# while playagain == 'да': 
#     Hangman()
#     print('Играть заново? (да/нет): ')
#     playagain = input()



import random
words = ['книга', 'ручка', 'дом', 'конкатенация', 'очки']
secret = random.choice(words)
print(secret)
hidden_word = list('*' * len(secret))
attempts = 5

while attempts !=0:
    letter = input(f'угадайте слово {hidden_word}\nколичество попыток:{attempts}\nвведите букву:').lower().strip()
    if letter in secret:
        for index, value in enumerate(secret):
            if letter == value:
                hidden_word[index] = letter
            if '*' not in hidden_word:
                print(f'вы угадалт слово {secret},поздравляю!')
                break
    else:
        attempts -= 1
        if attempts <5: print('  | ')
        if attempts <4: print('  O ')
        if attempts <3: print(' /|\ ')
        if attempts <2: print('  | ')
        if attempts <1: print(' / \ ')
    if attempts ==0:
        print(f'игра окончена,вы проиграли. загаданное слово:{secret}')
        break

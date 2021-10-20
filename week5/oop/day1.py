# Класс в Python — это логическая группа данных и функций. Он дает возможность создавать
#  структуры данных, которые содержат произвольный контент и, 
#  следовательно, легко доступны.
"""абстрактный тип данных
#  может наследовать данные и функциональность некоторого
#   существующего типа, способствуя повторному использованию компонентов 
#   программного обеспечения."""

#1 user registration

# class User:
#     plaform = 'Makers'
#     def __init__(self, age, username, password):
#         self.username = username
#         self.age = age
#         self.password = password
#         self.followers = []

#     def follow(self,user):
#         user.followers.append(self.username)

#     def unfollow(self, user):
#         user.followers.remove(self.username)
        
#     def followers_count(self):
#         return len(self.followers)


#     def __str__(self):
#         return f'{self.username} {self.age}'
    
# user1 = User(username='edward',password= 'vampire',age=17)
# user2 = User(username = 'jasper', password= 'vampire2', age=18)
# user3 = User(username='emmet',password='ihatewolfs',age=312)
# user1.follow(user2)
# user2.follow(user1)
# user3.follow(user2)
# # user1.unfollow(user2)
# # user3.unfollow(user2)
# print(user2.followers_count())

# print(user1.followers)

# print(user1.username, user1.password, user1.age, user1.plaform)
# print(user2.username, user2.password, user2.age, user2.plaform)




#2 football player
class FootballPlayer:

    status = 'sportsman'
    def __init__(self, name, last_name, team):
        self.name = name
        self.last_name = last_name
        self.team=team
        self.goals = 0


    def goal(self):
        self.goals += 1
        print('GOOAAALLL!!!!')
    

player1 = FootballPlayer('Cristiano','Ronaldo','MU')
player2 = FootballPlayer('Lionel','Messi','PSG')


import random

players = [player1, player2]
for _ in range(10):
    random.choice(players).goal()


print(player2.status)
player1.status = 'proger'
print(player1.status)

# print(player1.goals)
# print(player2.goals)

# # print(player1.team)
# player1.team = player2.team
# print(player1.team)
# player1.goal()
# player2.goal()
# player1.goal()
# player2.goal()
# player1.goal()
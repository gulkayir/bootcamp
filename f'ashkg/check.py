"""
1) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm,
 с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник.
"""

"""
2) Напишите класс Student, который описывает студента. У студента есть следующие атрибуты:
 имя, фамилия, класс, и оценки по предметам в следующем виде:
 {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по 
средней оценке студента по предметам.
"""

class Marks:
    def 
class Student:
    def __init__(self,name,lastname,group,marks:dict):
        self.name = name
        self.lastname = lastname
        self.group = group
        self.marks = marks

    def __eq__(self, other:dict):
        return self.marks.get('math') > other.get('math')

    
student1 = Student('Karl','Nolan','A1','{math’: 100, ‘history’: 89, literature’: 88}')
student2 = Student('Noah','Lokid','A1','{math’: 100, ‘history’: 90, literature’: 86}')


"""
3) Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
"""



"""
4) Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:

dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"

Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3
"""

# class MoneyFmt:
    
#     def init(self, amount):
#         self.amount = amount
        
#     @staticmethod
#     def dollarize(float_num):
#         if float_num >= 0:
#             return '${:,.2f}'.format(float_num)
#         else:
#             return '-${:,.2f}'.format(-float_num)
            
#     def update(self, num):
#         self.amount = num
        
#     def repr(self):
#         return f'{self.amount}'
        
#     def str(self):
#         return self.dollarize(self.amount)
        
        
# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))
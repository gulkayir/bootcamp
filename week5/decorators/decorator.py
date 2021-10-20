
# def call_function(funct):
#     def some_func(value = f'вызов функции прошел успешно {funct.__name__}'):
#         print(f'Вызываю функцию {funct.__name__}')

#         print('hello world')
#         funct(value)
#     return some_func
    

# @call_function
# def first(value):
#     print(f'{value}')

# first()


# def call_function(func):
#     def wrapper():
#         print('Вызываю функцию', func.__name__)
#         func()
#         print('Вызов функции', func.__name__,'прошёл успешно')
#     return wrapper

# @call_function
# def wrapped():
#     print('hello world')
# wrapped()



# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper
    
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())


from datetime import datetime

def benchmark(func):
    def wrapped():
        start_time = datetime.now()
        value = func()
        end_time = datetime.now()
        time1=end_time-start_time
        print(f'Время выполнения: {time1} секунд')
        return value
    return wrapped

@benchmark 
def fetch_webpage(): 
  import requests 
  webpage = requests.get('https://google.com')
fetch_webpage()  



from datetime import datetime

def func_start_time(func):
    def wrapper():
        start = datetime.now().strftime('%d.%m.%Y, %H:%M')
        print(f'Функция запущена {start}')
        print(func())
    return wrapper

@func_start_time
def func():
    return 'Hello world'
func()

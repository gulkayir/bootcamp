#1
# def slugify(func):
#     def wrapper(title):
#         return title.replace(' ','-').lower()
#     return wrapper


# @slugify
# def get_title(word):
#     return word

# print(get_title('Nike Airforce 2021'))



# def on_sale(func): 
#     def wrapper(sale,old_price):
#         func(sale, old_price)
#         new_price = old_price- (sale * old_price / 100)
#         print(f'New price is {new_price}')
#         return new_price
#     return wrapper


# @on_sale
# def buy_product(sale, price):
#     print(f'I have a {sale}% coupon . Old price is {price}$')


# buy_product(int(input('Enter sale: ')), int(input('Enter price: ')))

# login

# users = {
#     'jannat': 'qwerty',
#     'atai': 'elchacha',
#     'ulan': 'ulik'
# }

# def login_required(func):
#     def wrapped(**kwargs):
#         username = kwargs.get('username')
#         password = kwargs.get('password')
#         if username in users and password == users.get(username):
#             print('POST CREATED!!!!')
#             func(kwargs.get('title'),kwargs.get('image'))
#         elif not username or not password:
#             print('YOU SHOULD LOGIN!!')
#         else:
#             print('Not valid')
#     return wrapped

# @login_required
# def create_post (title, image):
#     print(f'{title} - {image}')
# create_post(title ='Post 1',
#             image='post 1.jpeg',
#             username='atai',
#             password='elchacha')

users = {
    'jannat': 'qwerty',
    'atai': 'elchacha',
    'ulan': 'ulik'
}

def validate_password(func):
    def wrapper(username1,password1):
        if username1 in users.keys() and password1 == users.get(username1):
            func(username=username1,password=password1)
        elif username1 in users.keys() and password1 != users.get(username1):
            print("Password is invalid")
        elif not username1 in users.keys():
            print("Username is not defined")
    return wrapper

@validate_password
def login(username,password):
    print(f'Welcome, {username}')
login('jannat','qwerty')


# connection = psycopg2.connect(
#     database = 'db_practice',
#     user = 'test_user',
#     password = '1',
#     host = 'localhost',
#     port = '5432'
# )
# print('Database successfully opened')

# cursor = connection.cursor() #обьект курсора
#создание таблицы
# cursor.execute(
#     '''CREATE TABLE company(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         city VARCHAR(50) NOT NULL
#     );
#     '''
# )
# print('Table successfully created')
# connection.commit()
# connection.close()

# cursor.execute(
#     '''
#     insert into company(name, city) values ('IBM', 'Los Angeles'),
#     ('Apple', 'Cupertino'), ('HP', 'New York'), ('Dell', 'New Jersey')
#     '''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close() #you should always close connection for security

# cursor.execute(
    # '''
    # insert into company(name, city) values ('Samsung','Seoul')
    # '''
# )
# cursor.execute(
#     '''
#     insert into company(name, city) values ('Toyota','Tokyo')
#     '''
# )
# connection.commit()
# print('inserted successfully')
# connection.close()

# cursor =connection.cursor()

# cursor.execute(
#     '''
#     select * from company
#     '''
# )
# print(cursor.fetchall())
# data = cursor.fetchall()
# for item in data:
#     # print(f'id:{item[0]}, name: {item[1]}, city: {item[2]}')
#     print(*item)

# cursor.execute(
#     """
#     select name, city from company where id=2
#     """
# )
# data = cursor.fetchone()
# print(data)

# connection.close()

# cursor.execute(
#     '''
#     update company set city='New Mexico' where id=2
#     '''
# )
# connection.commit()
# cursor.execute(
#     '''
#     select * from company
#     '''
# )
# data = cursor.fetchall()
# for item in data:
#     print(*item)
# connection.close()


# cursor.execute(
#     '''
#     delete from company where id=3
#     '''
# )
# connection.commit()
# print(f'total count of deleted: {cursor.rowcount}')
# cursor.execute(
#     ''' 
#     select * from company order by id
#     '''
# )

# data = cursor.fetchall()
# for item in data:
#     print(*item)

# connection.close()

import psycopg2
# from sqlalchemy import create_engine

# engine = create_engine('postgresql+psycopg2://gulkayir:1@localhost:5432/db_practice')
# print('database connected')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# students_table = Table(
#     'students', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('last_name', String)
# )

# students_table.create(bind=engine)
# print('successfully created table')

# inserted_data = students_table.insert().values(name='Edward', last_name= 'Cullen')
# engine.execute(inserted_data)
# print('successfully insertted')

# from sqlalchemy import select
# query = select([students_table.c.name, students_table.c.last_name])
# data = engine.execute(query).fetchall()
# for item in data:
#     print(*item)



# from sqlalchemy import create_engine

# engine = create_engine('postgresql+psycopg2://gulkayir:1@localhost:5432/db_practice')


# metadata = MetaData()
# company_table = Table(
#     'company', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('city', String)
# )
# metadata.create_all(engine)

# class Company:
#     def __init__(self,name, city):
#         self.name = name
#         self.city = city

#     def __str__(self):
#             return f'Company {self.name} in {self.city} city'

# from sqlalchemy.orm import mapper 
# mapper(Company, company_table)

# print('successfully creates table')
        

from sqlalchemy import Column, Table, Integer, String
from sqlalchemy.ext.de
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://gulkayir:1@localhost:5432/db_practice')

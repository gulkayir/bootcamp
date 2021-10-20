"""основные комнады пишутся с верхним регистром,но sql не чувствителен к регистрам

create database name_database --> создание бд
create user name_user with password ---> создание пользователя с паролем
alter user user_name with (superuser) ---> присвоение статуса superuser
grant all privilegies on batabase_name to name_user ---> присвение всех привилегий пользвателю
create database name_database with owner name_user ---> сздание бд с указанием владельца
"""


"""deleting
drop database db_name

"""
# \c  database_name ---> connecting to database
# \l ---> list of databases ; DON'T FORGET TO TYPE ';' AFTER COMMANDS
# psql -U user_name ---> inintialixing eith username to databse



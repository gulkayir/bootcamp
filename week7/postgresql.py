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


# working with columns

"""
update ---> changing value
select works like filter
insert into --> adding STRING 
DELETE --> deleting table 
ALTER TABLE -->

order desc --> сортировка по убыванию в алфвитном порядке
order by __ asc (nulls first(), nulls last) ---> нулевые поля
select distinct country(убрать повторяющиеся значения)
select distinct on(values) for unique values
select * 'where' ---> also filter where value = 'some value'
... where not in ('values', 'value) --->filter

between .. and ..
select * from 'table name' where 'cloumn name' like '%value'  ----> % означает какие либо значения,
 он может стять и в начале и в конце, 

is null ---> вытащить нулевые значения
select * from 'table' limit 10 ---> set limit to 10 table elements
but sql prefers 'fetch'
select country, avg(age) from info group by country;
 country |         avg        

having is like where

"""

# update

"""
select souce,count(*) from dish group by souce;
select type, money (sum(price)) from dish group by type;

"""

"""
join

select u.id, u.name, u.last_name, e.email from users as u inner
 join email as e on u.id=e.user_id;

"""
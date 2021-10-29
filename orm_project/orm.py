from requests.sessions import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,  String
from sqlalchemy.orm import sessionmaker

from main import main

engine = create_engine('postgresql+psycopg2://gulkayir:1@localhost:5432/deputy_db')
print('connected') #\c debuty_db

Base = declarative_base()

class Deputy(Base):
    __tablename__ = 'deputy'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    fraction = Column(String)
    telephone = Column(String)

    def __init__(self, full_name, fraction, telephone):
        self.full_name = full_name
        self.fraction = fraction
        self.telephone = telephone

    def __str__(self):
        return f'{self.full_name}, {self.fraction}, {self.telephone}'

# Base.metadata.create_all(engine)
# print('Table created!!')

Session = sessionmaker(bind=engine)
session = Session()

# deputy1 = session.query(Deputy).get(1)
# print(deputy1)
# deputy1.full_name = 'Kani'
# session.commit()
# print(deputy1)

birbolovci = session.query(Deputy).filter(Deputy.fraction.ilike('%Бир Бол%'))

for dep in birbolovci:
    print(dep)

# data = main()
# for deputy in data:
#     session.add(Deputy(*deputy))
#     print('successfully added note')

#     session.commit()
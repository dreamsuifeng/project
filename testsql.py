from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table,backref='parents')

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

if __name__ == '__main__':
    enging=create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/flaskdb2')
    Base.metadata.create_all(enging)

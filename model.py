# -*- coding:utf-8 -*-

from sqlalchemy import Table, Column, Integer, ForeignKey,String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mysqlurl="mysql+pymysql://root:123456@114.212.86.79:3306/flaskdb"

Base=declarative_base()

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(80),nullable=False)
    password=Column(String(80),nullable=False)
    roleid=Column(Integer,ForeignKey('roles.id'))
    role=relationship('Role',backref=backref('users',lazy='dynamic'))

    def __init__(self,name,pasw):
        self.username=name
        self.password=pasw


association_table=Table('association',Base.metadata,
            Column('roleid',Integer,ForeignKey('roles.id')),
            Column('authid',Integer,ForeignKey('authorities.id'))
            )
class Role(Base):
    __tablename__='roles'
    id=Column(Integer,primary_key=True)
    rolename=Column(String(80),nullable=False)
    def __init__(self,name):
        self.rolename=name

class Authority(Base):
    __tablename__='authorities'
    id=Column(Integer,primary_key=True)
    auname=Column(String(80),nullable=False)
    audec=Column(String(128),nullable=True)
    def __init__(self,name):
        self.auname=name
    


engine=create_engine(mysqlurl)
Session=sessionmaker(bind=engine)
sess=Session()
if __name__=='__main__':
    Base.metadata.create_all(engine)


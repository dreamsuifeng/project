from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import adminApp
db=SQLAlchemy(adminApp)

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

db.create_all()

tag1=Tag()
tag2=Tag()
page1=Page()
page2=Page()

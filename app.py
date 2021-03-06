# -*- coding:utf-8 -*-

# app config
mysqlurl="mysql+pymysql://root:123456@114.212.86.79:3306/flaskdb2"


from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import *

adminApp=Flask(__name__)
adminApp.config['SQLALCHEMY_DATABASE_URI']=mysqlurl
adminApp.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
adminApp.config['SECRET_KEY']='my precious'

from model import *
@adminApp.route('/')
def home():
    if request.method=='GET':
        form=LoginForm(request.form)
        return render_template('forms/login.html',form=form)


@adminApp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm(request.form)
    if request.method=='GET':
        
        return render_template('forms/login.html',form=form)
    if request.method=='POST':
        name=request.form.get('name')
        pasw=request.form.get('password')
        datauser=sess.query(User).filter(User.username==name).first()

        if  datauser==None or datauser.password!=pasw:
            return render_template('forms/login.html',form=form,message='username or password error, please input again')
        else:
            return render_template('pages/placeholder.home.html',username=name)


@adminApp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        form=RegisterForm(request.form)
        
        return render_template('forms/register.html',form=form)
    if request.method=='POST':
        name=request.form.get('name')
        passw=request.form.get('password')
        if len(sess.query(User).filter(User.username==name).all())==0:
            user=User(name,passw)
            sess.add(user)
            sess.commit()
            return render_template('forms/ok.html',message='register sussess,please login in')
        else:
            form=RegisterForm(request.form)
            return render_template('forms/register.html',form=form,message='username is existed,please modify')

@adminApp.route('/logout')
def logout():
    return redirect(url_for('login'))
@adminApp.route('/admininformation/<username>',method=['GET','POST'])
def admininformation(username):
    return render_template()

@adminApp.route('/roleandauthadmin',methods=['GET','POST'])
def roleandauthadmin():
    if request.method=='GET':
        form=LoginForm(request.form)
        return render_template('superpages/suerlogin.html',form=form)
    if request.method=='POST':
        supername=request.form.get('name')
        superpass=request.form.get('password')
        if supername==admin and superpass=='admin':
            return render_template('superpages/roleandauthadmin.html')
if __name__=='__main__':
    adminApp.run(debug=True)
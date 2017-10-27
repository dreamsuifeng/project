# coding:utf-8

import requests
from bs4 import BeautifulSoup
import pymysql
import time
url="http://status.daocloud.io/"
times=300
host='127.0.0.1'
port=3306
user='root'
passwd='123456'
dbname='flaskdb'
charset='utf8'

def getInfo(url):
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    result_text=soup.findAll('li',class_='list-group-item component')
    data_list=[]
    
    for r in result_text:
        tmpkey=''
        tmpvalue=''
        if r.find('a'):
            tmpkey=r.find('a').text
            tmpvalue=r.find('small').text
        else:
            strings=r.text.replace('\n','').strip().split(' ')
            
            tmpkey=strings[0]
            tmpvalue=strings[-1]
        data_list.append((tmpkey,tmpvalue))
    timestamp=time.strftime('%Y/%M/%d %H:%M:%S',time.localtime(time.time()))
    sql="insert into status values(0,'"+data_list[0][1]+"','"+data_list[1][1]+"','"+data_list[2][1]+"','"+data_list[3][1]+"','"+data_list[4][1]+"','"+timestamp+"')"
    updateDB(sql)

def updateDB(sql):
    print(sql)
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset=charset)
    
    cursor=conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        print("success")
    except:
        db.rollback()
        print('failed insert data')
    # print(e)
    # db.rollback()
    # print("failed insert data")

    conn.close()
def mainrun(times,url):
    """
    time is a parameter which means the program executes every times seconds
    url is where we get information from
    """
    while True:
        getInfo(url)
        time.sleep(times)
if __name__  == '__main__':
   
    mainrun(times,url)

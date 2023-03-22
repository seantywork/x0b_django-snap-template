from . import retriever
import json
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')

def searchengine(query,psw):

    x = query
    y = psw
    check = 0
    token_check = 0
    count_check = 0
    z = list()

    try:

        connection = mysql.connector.connect(host=DB_HOST,
                                                database='test',
                                                user='seantywork',
                                                password=DB_PASS)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM counter;')
            z = cursor.fetchall()

    except Error as e:
        
        data = 'DB Connection Failed : ' + e
        context = {'res':data, 'status':'n'}
        
        return context

    for i in range(len(z)):
        if y == z[i][0] :
            token_check = 1
        if z[i][1] <= 10 and token_check == 1:
            count_check = 1
            new_num = z[i][1] + 1
            cursor.execute('UPDATE counter SET count = '+str(new_num)+' WHERE user = \''+z[i][0]+'\';')
            connection.commit()
            cursor.close()
            connection.close()
            break


    if  len(x) < 100 and x.isascii() and token_check == 1 and count_check == 1:
        for i in x :
            if ord(i) == 32:
                check = 1
        if check == 0:
            res = retriever.retriever([x],1)

        elif check == 1:
            res = retriever.retriever([x],2)

        res = res.sample(frac=1).reset_index(drop=True)
        if len(res) > 10 :
            res = res.head(10)

        res = res.reset_index().to_json(orient='records')
        data = []
        data = json.loads(res)
        context = {'res':data, 'status':'y'}
        return context

    elif len(x) < 100 and x.isascii() and token_check == 1 and count_check == 0:
        data = 'Auth Expired'
        context = {'res':data, 'status':'n'}
        return context

    else :
        data = 'Credential Not Found Or Query Invalid'
        context = {'res':data,'status':'n'}
        return context
import json
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')




def searchWord(query):



    ca_query = '%' + query + '%'


    try:

        connection = mysql.connector.connect(host=DB_HOST,
                                                database='test',
                                                user='seantywork',
                                                password=DB_PASS)

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT IDX, WORD FROM words_alpha WHERE WORD LIKE %s;',[ca_query])
        res_arr = cursor.fetchall()

        data = res_arr

        if len(data) == 0 :

           data = [{"IDX":'Not Availabe',"WORD":"No Such Entry: "+query}] 

           context = {'RES':data, 'STATUS':'y'}

        else :

            context = {'RES':data, 'STATUS':'y'}

    except Error as e:
        
        data = 'Failed : ' + e
        context = {'RES':data, 'STATUS':'n'}
        

    finally:

        connection.close()


    return context


        


import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def bd_conexao():
    return pymysql.connect(
        host='localhost',
        user='root',
        password=os.getenv('senha_secreta'), 
        database='unify',
        cursorclass=pymysql.cursors.DictCursor 
    )
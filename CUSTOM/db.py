import pymysql
from CONFIG import conf_parser
import boto3

            
db_endpoint = conf_parser.do('mysql')['db_endpoint']
db_name = conf_parser.do('mysql')['db_name']
db_port = conf_parser.do('mysql')['db_port']
db_username = conf_parser.do('mysql')['db_uname']
db_password = conf_parser.do('mysql')['db_pass']



#==============================================================
def db_conn():
    #==============================================================
    global db
    global cur
    #==============================================================
    try:
        db = pymysql.connect(db_endpoint, user=db_username, passwd=db_password, db=db_name, connect_timeout=5)
        cur = db.cursor()
        return {'status': 'success'}
    except:
        return {'status': 'failed', 'err': 'Unexpected error: Could not connect to MySql instance.'}
#==============================================================

#==============================================================
def db_close():
    cur.close()
    db.close()
#==============================================================    

#==============================================================
def fetch(table_name,condition):
    db_conn()
    try:
        cur.execute("SELECT * FROM " + table_name + " WHERE " + condition)
        rows = cur.fetchall()
        return {'status': 'success', 'rows': rows}
    except Exception as e:
       
        return {'status': 'failed', 'err': e}
#==============================================================

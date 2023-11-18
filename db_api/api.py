import flask
from flask import request, jsonify
from config import *
import pymysql.cursors

# Define function to establish RDS connection
def start_rds_connection():
    try:
        connection = pymysql.connect(host=ENDPOINT,
        port=PORT,
        user=USERNAME,
        passwd=PASSWORD,
        db=DBNAME,
        cursorclass=CURSORCLASS,
        ssl_ca=SSL_CA)
        print('[+] RDS Connection Successful')
    except Exception as e:
        print(f'[+] RDS Connection Failed: {e}')
        connection = None
    return connection
    
    


app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/v1/resources/songs', methods=['GET'])
def song_year():
    if 'year' in request.args:
        year = int(request.args['year'])
    else:
        return 'Error: no year provided, please specify a year'
    
    connection = start_rds_connection()

    with connection.cursor() as cursor:
        sql = f"SELECT * FROM top10s_1 where year = {year}"
        cursor.execute(sql)
        result = cursor.fetchall() # Retrieve all rows
        print(result)
        connection = None
        
    return jsonify(result)
    
# Initiate RDS connection
# connection = start_rds_connection()


# with connection.cursor() as cursor:
#     sql = f"SELECT * FROM top10s_1"
#     cursor.execute(sql)
#     result = cursor.fetchall() # Retrieve all rows
#     print(result)
    
# connection.commit()

# connection = None

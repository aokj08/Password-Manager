import psycopg2

def connect():
    try:
        conn = psycopg2.connect(host="localhost", port=5432, database="password_table", user="User", password="Password")
        return conn
    except(Exception, psycopg2.Error) as error:
        print(error)

def store_passwords(password, user_email, username, url, app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        insert_query = """ INSERT INTO accounts (password,email,username, url, app_name) VALUES (%s,%s,%s,%s,%s)"""
        insert_value = (password, user_email, username, url, app_name)
        cur.execute(insert_query,insert_value)
        conn.commit()
        conn.close()
        cur.close()
    except(Exception, psycopg2.Error) as error:
        print(error)
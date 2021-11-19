import requests
import json
import pandas.io.sql as psql

DBNAME = 'postgres'
HOST='localhost'
USENAME='postgres'
PASSWORD='postgres'

def DatabaseConnection():
    try:
        dbconn = pg.connect("dbname={} user={} host={} password={}".format(DBNAME,USENAME,HOST,PASSWORD))
    except pg.Error as error:
        print(error)
    return dbconn


def SelectSongsFrame():
    dbconn = DatabaseConnection()
    try:
        with dbconn:
            sql = "SELECT * FROM spotify_daily_listened_songs"
            df = psql.read_sql(sql,dbconn)
    except pg.DataError as e:
        print(e)
        print("Error during inserting logs into RDS database in table_log")
    return df

def SlackMessageSending():
    df = SelectSongsFrame()
    webhook = 'https://hooks.slack.com/services/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'
    data = {
        "text": """Bok Matac, zadnjih tjedan dana najviše ti se dopala pjesma """ +  df['song_name']  + """" od """ + ['artist']+ ""

    }
    try:
        response = requests.post(webhook,json.dumps(data))
    except:
        'Greska prilikom slanja poruke'
    return 1


SlackMessageSending()
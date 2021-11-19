import psycopg2 as pg
from SpotifyAPI import transform_data()

DBNAME = 'postgres'
HOST='localhost'
USENAME='postgres'
PASSWORD='postgres'

def datebase_conenction():
    try:
        dbconn = pg.connect("dbname={} user={} host={} password={}".format(DBNAME,USENAME,HOST,PASSWORD))
    except pg.Error as error:
        print(error)
    return dbconn



def get_songs():
    dbconn = datebase_conenction()
    try:
        with dbconn:
            sql = "SELECT * FROM spotify_daily_listened_songs"
            df = psql.read_sql(sql,dbconn)
    except pg.DataError as e:
        print(e)
        print("Error during inserting logs into RDS database in table_log")
    return df
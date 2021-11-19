import psycopg2 as pg

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
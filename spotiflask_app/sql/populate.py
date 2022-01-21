import os
import csv
import psycopg2
from dotenv import load_dotenv

# loads environement variables with correct parameters for database connection
load_dotenv()
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
database = os.environ.get('POSTGRES_DATABASE')

conn = psycopg2.connect(f"host={server} dbname={database} user={user} password={password}")
cur = conn.cursor()
cur.execute('truncate "Band", "Album", "Song";')

#  load Bands into db
with open('bands.csv', 'r', encoding='utf-8') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'Band', sep=',', null='')  # copy all records from csv file to database
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Band_id_seq" RESTART WITH {lines};')  # set next id value in the database
    conn.commit()

#  load Albums into db
with open('albums.csv', 'r', encoding="utf-8") as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'Album', sep=',', null='')  # copy all records from csv file to database
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Album_id_seq" RESTART WITH {lines};')  # set correct next id value in the database
    conn.commit()

#  load Songs into db
with open('songs.csv', 'r', encoding='utf-8') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'Song', sep=',', null='')
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Song_id_seq" RESTART WITH {lines};')  # set correct next id value in the database
    conn.commit()

conn.close()

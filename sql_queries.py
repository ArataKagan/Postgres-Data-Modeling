# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(ID text, TITLE text, ID_ARTIST text, YEAR int, DURATION double precision)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(ID text, TITLE text, ID_ARTIST text, YEAR int, DURATION double precision)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(ID text, TITLE text, ID_ARTIST text, YEAR int, DURATION double precision)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(ID text, TITLE text, ID_ARTIST text, YEAR int, DURATION double precision)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times(ID text, TITLE text, ID_ARTIST text, YEAR int, DURATION double precision)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
INSERT INTO song(ID, TITLE, ID_ARTIST, YEAR, DURATION)
VALUES(%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
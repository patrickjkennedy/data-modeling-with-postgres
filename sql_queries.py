# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL,
    ts BIGINT,
    userId INT,
    level VARCHAR,
    songId VARCHAR,
    artistId VARCHAR,
    sessionId INT,
    location VARCHAR,
    userAgent VARCHAR);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    userId INT PRIMARY KEY,
    firstName VARCHAR,
    lastName VARCHAR,
    gender VARCHAR,
    level VARCHAR);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration NUMERIC);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY,
    artist_name VARCHAR,
    artist_location VARCHAR,
    artist_latitude NUMERIC,
    artist_longitude NUMERIC);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time BIGINT PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songplays (ts, userId, level, songId, artistId, sessionId, location, userAgent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (userId, firstName, lastName, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (userId) DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s 
AND a.artist_name = %s
AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
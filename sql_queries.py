# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplayId SERIAL PRIMARY KEY,
    startTime TIMESTAMP NOT NULL,
    userId INT NOT NULL,
    level VARCHAR NOT NULL,
    songId VARCHAR,
    artistId VARCHAR,
    sessionId INT NOT NULL,
    location VARCHAR NOT NULL,
    userAgent VARCHAR NOT NULL);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    userId INT PRIMARY KEY,
    firstName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    gender VARCHAR NOT NULL,
    level VARCHAR NOT NULL);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INT NOT NULL,
    duration NUMERIC NOT NULL);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY,
    artist_name VARCHAR NOT NULL,
    artist_location VARCHAR NOT NULL,
    artist_latitude NUMERIC NOT NULL,
    artist_longitude NUMERIC NOT NULL);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INT NOT NULL,
    day INT NOT NULL,
    week INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    weekday INT NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songplays (startTime, userId, level, songId, artistId, sessionId, location, userAgent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (userId, firstName, lastName, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (userId) DO UPDATE SET 
firstName=EXCLUDED.firstName,
lastName=EXCLUDED.lastName,
gender=EXCLUDED.gender,
level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE SET 
title=EXCLUDED.title,
artist_id=EXCLUDED.artist_id,
year=EXCLUDED.year,
duration=EXCLUDED.duration;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO UPDATE SET 
artist_name=EXCLUDED.artist_name,
artist_location=EXCLUDED.artist_location,
artist_latitude=EXCLUDED.artist_latitude,
artist_longitude=EXCLUDED.artist_longitude;
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
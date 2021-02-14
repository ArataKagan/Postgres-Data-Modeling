# Song Metadata Data Modeling Project with Postgres 

## Overview

A hypothetical startup called Sparkify has been collecting songs and user activity data for their music streaming app. They would like to analyze what users are listening to from the dataset. However, the data resides in a directory of JSON logs and there is no easy access to query the data. 

In this project, I'm going to write an ETL pipeline that tranfers data from files in two local directories into tables in Postgres with Python. 

## Datasets
- Song Dataset
    - A subset of data from the Million Song Dataset. Each file is in JSON format and contains mtadata about a song and the artist of that song. 
    ```
     {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
    ```

- Log Dataset 
    - JSON format log files generated by this ![event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. Each record is simulation of activity log. 
    ```
     {"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}
    ```

## Scheman Design 

**Fact Table**: <br/>
Songplays Table
 * songplay_id int PRIMARY KEY
 * timestamp date REFERENCES times(start_time)
 * user_id int REFERENCES users(user_id)
 * level text
 * song_id text REFERENCES songs(song_id)
 * artist_id text REFERENCES artists(artist_id)
 * session_id int
 * location text
 * user_agent text


**Dimention Table**: <br/>
Users Table
 * user_id int PRIMARY KEY
 * first_name text
 * last_name text 
 * gender text
 * level text

Songs Table
 * song_id text PRIMARY KEY
 * title text NOT NULL
 * artist_id text NOT NULL REFERENCES artists(artist_id)
 * year int
 * duration float NOT NULL

Artists Table
 * artist_id text PRIMARY KEY
 * name text NOT NULL
 * location text
 * lattitude float
 * longitude float

Times Table 
 * start_time date PRIMARY KEY, 
 * hour int, 
 * day int, 
 * week int, 
 * month int,
 * year int,
 * weekday text
 
## Output Example 


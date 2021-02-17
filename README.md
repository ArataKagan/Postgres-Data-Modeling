# Song Metadata Data Modeling Project with Postgres 

## Overview

A hypothetical startup called Sparkify has been collecting songs and user activity data for their music streaming app. They would like to analyze what users are listening to from the dataset. However, the data resides in a directory of JSON logs and there is no easy access to query the data. 

In this project, I'm going to write an ETL pipeline that tranfers data from files in two local directories into tables in Postgres with Python. 


## Datasets
- Song Dataset
    - JSON data nested under subdirectories of data/song_data:
    ```
     {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
    ```

- Log Dataset 
    - JSON data nested under subdirectories of data/log_data:
    ```
     {"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}
    ```

## File Structure 

- data : A folder to store each dataset which is nested under subdirectories. Divided into song_data and log_data folders. 
- etl.ipynb : Testing purpose file to read and process first line of each dataset
- etl.py : Reads and process dataset and stored into database 
- sql_queries.py : Contains all sql queries
- create_tables.py : Contains CREATE and DROP functions 

## Scheman Design 

Star schema design is used to organize tables with one fact table (Songplay) and a several associated dimentional tables (Users, Songs, Artists, Times). 

### Fact Table: 
**Songplays Table**
 * songplay_id INT PRIMARY KEY 
 * timestamp DATE : Time table's start time 
 * user_id INT : User ID 
 * level TEXT : User level 
 * song_id TEXT : Song ID 
 * artist_id TEXT : Artist ID 
 * session_id INT : Session ID 
 * location TEXT : User's location  
 * user_agent TEXT : User's agent to access the app 


### Dimention Tables: 
**Users Table**
 * user_id INT PRIMARY KEY
 * first_name TEXT 
 * last_name TEXT
 * gender TEXT
 * level TEXT 

**Songs Table**
 * song_id TEXT PRIMARY KEY 
 * title text NOT NULL
 * artist_id TEXT NOT NULL : Refers to artist's ID
 * year INT
 * duration FLOAT NOT NULL

**Artists Table**
 * artist_id TEXT PRIMARY KEY
 * name TEXT NOT NULL
 * location TEXT
 * lattitude FLOAT
 * longitude FLOAT

**Times Table** 
 * start_time DATE PRIMARY KEY
 * hour INT 
 * day INT 
 * week INT 
 * month INT
 * year INT 
 * weekday text

## ETL Steps

1) Connect to the local Postgres DB using Python's psycopg2 ORM library
2) Retrieve each subdirectory files using os.walk and store each file into a list
3) Loop over each retrieved file 
4) Convert the retrieved list's JSON data into Pandas dataframe 
5) Retrieve values based on specified column names and convert into a list 
6) Insert the list into database 

## Output Example 
```
SELECT * FROM songplays LIMIT 5;
```
![query-output](https://github.com/ArataKagan/Postgres-Data-Modeling/blob/main/query1.png)

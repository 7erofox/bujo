import sqlite3
from datetime import datetime

table_creation_query = """CREATE TABLE IF NOT EXISTS moodtracker (
  id INTEGER PRIMARY KEY, 
  created_at TEXT NOT NULL,
  mood_score INTEGER NOT NULL,
  vinegar TEXT NOT NULL,
  refined_sugar TEXT NOT NULL,
  exercise TEXT NOT NULL
);"""

insert_row_query = """insert into moodtracker ( 
created_at,
mood_score,
vinegar,
refined_sugar,
exercise
) VALUES (
"{}","{}","{}","{}", "{}");
"""
created_at = datetime.now()

mood_score = input("What is your mood today, on a scale of 1-10? ")

vinegar = input("Did you drink vinegar before your biggest meal today? ")

refined_sugar = input("Did you have refined sugar today? ")

exercise = input("Did you do any exercise today? ")

print("mood: ", mood_score,  "vinegar: ", vinegar, "sugar: ", refined_sugar, "exercise: ", exercise) 
input("Are these values correct? ")

conn = sqlite3.connect("moodtracker.db")
cursor = conn.cursor()
cursor.execute(table_creation_query)
conn.commit()
cursor.execute(insert_row_query.format(created_at, mood_score, vinegar, refined_sugar, exercise))
conn.commit()
conn.close()
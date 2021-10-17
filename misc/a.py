import pymongo
from datetime import datetime
import sqlite3
import ssl
import time

# defining the constant values
# change this value, so that on 100 th row insertion db commit will happen
threshold_value_to_commit = 1000
count = 0
width = 157
conn = sqlite3.connect('index.sqlite')
with conn:
    cursor = conn.execute("select * from BIKESTATION;")
    data = cursor.fetchall() # fetch all the data from the sqlite
    print("Total row count was : ", len(data))
    print("A sample data from sqlite database is:\n")
    # drawing table 
    print("-"*width)
    print(f"|{'ID':^5} |{'TIMESTAMP':<25} |{'STATION_NAME':<25}  |{'TOTAL_DOCKS':^15} |{'AVAILABLE_DOCKS':^15} |{'AVAIALBLE_BIKES':^15} |{'LATITUDE':^15} |{'LONGITUDE':^15}|")
    print("-"*width)
    for row in range(5):
        for i in range(len(data[row])):
            if i in [1,2]:
                print(f"|{data[row][i]:<25}",end=" ")
                continue
            print(f"|{data[row][i]:^15}",end=" ")
        print("\b|")
    print("-"*width)
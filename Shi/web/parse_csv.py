import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('shi_covid.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS Africa')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE Africa (iso_code TEXT, continent TEXT, location TEXT, date TEXT, total_cases TEXT, new_cases TEXT, new_cases_smoothed TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS owid_covid')
print("table dropped successfully");
# create the status table again  
conn.execute('CREATE TABLE owid_covid (iso_code TEXT, continent TEXT, location TEXT, date TEXT, total_cases TEXT, new_cases TEXT, new_cases_smoothed TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('Africa.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        #print(row)

        iso_code = row[0]
        continent = row[1]
        location = row[2]
        date = row[3]
        total_cases = row[4]
        new_cases = row[5]
        new_cases_smoothed = row[6]

        cur.execute('INSERT INTO Africa VALUES (?,?,?,?,?,?,?)', (iso_code, continent, location, date, total_cases, new_cases, new_cases_smoothed))
        conn.commit()
print("data parsed successfully");


# open the file to read it into the database
with open('owid_covid_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    print('start to work on the status table')
    for row in reader:
        #print(row)
        # check if the row starts with empty string (avoid reading empty lines after the data)
        iso_code = row[0]
        continent = row[1]
        location = row[2]
        date = row[3]
        total_cases = row[4]
        new_cases = row[5]
        new_cases_smoothed = row[6]

        cur.execute('INSERT INTO owid_covid VALUES (?,?,?,?,?,?,?)', (iso_code, continent, location, date, total_cases, new_cases, new_cases_smoothed))
        conn.commit()
print("data parsed successfully");



conn.close()
import mysql.connector

def create_database():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = con.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS voting_system")

        print("Database 'voting_system' created successfully.")

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL server: {}".format(error))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection is closed")





def create_tables():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="voting_system")
        cursor = con.cursor()

        # Create voters_details table
        cursor.execute("CREATE TABLE IF NOT EXISTS voters_details (id INT PRIMARY KEY, name VARCHAR(50), state VARCHAR(50), age INT, password VARCHAR(50))")

        # Create candidates table
        cursor.execute("CREATE TABLE IF NOT EXISTS candidates (number INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), id INT, age INT, qualification VARCHAR(50), state VARCHAR(50), party VARCHAR(50))")

        # Create vote_count table
        cursor.execute("CREATE TABLE IF NOT EXISTS vote_count (candidate_number INT, count INT, PRIMARY KEY (candidate_number), FOREIGN KEY (candidate_number) REFERENCES candidates(number))")

        # Create party table
        cursor.execute("CREATE TABLE IF NOT EXISTS party (number INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), vote_count INT)")

        print("Tables created successfully.")

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection is closed")

def insert_data():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="voting_system")
        cursor = con.cursor()
        
         # Insert data into voters_details table
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (101, 'Midhu', 'central', 25, 'Midhu123')")
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (102, 'Karan', 'western', 30, 'Karan123')")
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (103, 'Jeya', 'uva', 25, 'jeya123')")
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (104, 'Dhanu', 'western', 30, 'dhanu123')")
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (105, 'Dinu', 'central', 58, 'dinu123')")
        cursor.execute("INSERT INTO voters_details (id, name, state, age, password) VALUES (106, 'Sha', 'western', 17, 'sha123')")
        
       

        # Insert data into candidates table
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Shan', 108, 42, 'Master', 'central', 'B')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Dhira', 109, 35, 'Bachelor', 'western', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Jana', 110, 52, 'Master', 'central', 'B')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Jensi', 111, 35, 'Bachelor', 'uva', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Jeuba', 112, 22, 'Master', 'western', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Kogulan', 113, 36, 'Bachelor', 'central', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Anis', 114, 58, 'Master', 'uva', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Nimesh', 115, 35, 'Bachelor', 'central', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Nila', 116, 35, 'Bachelor', 'central', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Jegan', 117, 22, 'Master', 'western', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Jina', 118, 35, 'Bachelor', 'uva', 'A')")
        cursor.execute("INSERT INTO candidates (name, id, age, qualification, state, party) VALUES ('Kavi', 119, 52, 'Master', 'central', 'B')")

        
       
        # Insert data into party table
        cursor.execute("INSERT INTO party (name, vote_count) VALUES ('A', 0)")
        cursor.execute("INSERT INTO party (name, vote_count) VALUES ('B', 0)")
        con.commit()

        print("Tables created and data inserted successfully.")

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("MySQL connection is closed")



# Call the functions
create_database()
create_tables()

#insert data is optional  function becouse the admin can insert the records.
#insert_data()








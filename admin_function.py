import mysql.connector
import sys
import matplotlib.pyplot as plt

class AdminSystem:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="voting_system"
        )
        self.cursor = self.con.cursor()

    def add_citizen(self):
        print("-----------------Add New Citizens-----------------")
        a = int(input("Enter how many records you want to add: "))
        for i in range(a):
            id_number = input("Enter the id number: ")
            name = input("Enter the Citizen name: ")
            state = input("Enter the State: ")
            age = int(input("Enter the Age: "))
            password = input("Enter the password: ")
            
            self.insert_citizen(id_number, name, state, age, password)

    def insert_citizen(self, id_number, name, state, age, password):
        try:
            # Execute query to insert a new record
            insert_record = "INSERT INTO voters_details (id, name, state, age, password) VALUES (%s, %s, %s, %s, %s)"
            data = (id_number, name, state, age, password)
            self.cursor.execute(insert_record, data)
            self.con.commit()
            print("Record added successfully")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def update_citizen(self):
        print("-----------------Update Citizens details-----------------")
        a = int(input("Enter how many records you want to update: "))
        for i in range(a):
            current_id = input("Enter the current id Number: ")
            id_number = input("Enter the updated id number: ")
            name = input("Enter the updated Citizen name: ")
            state = input("Enter the updated State: ")
            age = int(input("Enter the Updated Age: "))
            password = input("Enter the Updated password: ")
            
            self.update_citizen_details(current_id, id_number, name, state, age, password)

    def update_citizen_details(self, current_id, id_number, name, state, age, password):
        try:
            # Execute query to update the record
            query = "UPDATE voters_details SET id = %s, name = %s, state = %s, age = %s, password = %s WHERE id = %s"
            data = (id_number, name, state, age, password, current_id)
            self.cursor.execute(query, data)
            self.con.commit()
            print("Record updated successfully")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def delete_citizen(self):
        print("-----------------Delete Citizens details-----------------")
        a = int(input("Enter how many records you want to delete: "))
        for i in range(a):
            id_number = input("Enter the id number to delete: ")
            self.delete_citizen_details(id_number)

    def delete_citizen_details(self, id_number):
        try:
            # Execute query to delete the record
            query = "DELETE FROM voters_details WHERE id = %s"
            self.cursor.execute(query, (id_number,))
            self.con.commit()
            print("Record deleted successfully")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def view_citizen(self):
        print("-----------------View Citizens Details-----------------")
        a = int(input("Enter how many records you want to view: "))
        for i in range(a):
            id_number = input("Enter the id number to view: ")
            self.view_citizen_details(id_number)

    def view_citizen_details(self, id_number):
        try:
            # Execute query to fetch the record
            query = "SELECT * FROM voters_details WHERE id = %s"
            self.cursor.execute(query, (id_number,))
            records = self.cursor.fetchall()

            if len(records) == 0:
                print("No records found.")
            else:
                print("NIC\tName\tState\tAge\tPassword")
                print("---------------------------------------------------------")
                for row in records:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def add_candidate(self):
        print("-----------------Add New Candidate-----------------")
        a = int(input("Enter how many records you want to add: "))
        for i in range(a):
            id_number = input("Enter the id number: ")
            name = input("Enter the Candidate name: ")
            state = input("Enter the State: ")
            age = int(input("Enter the Age: "))
            password = input("Enter the password: ")
            qualification = input("Enter the Qualification: ")
            party = input("Enter the party name: ")
            
            self.insert_candidate(id_number, name, state, age, password, qualification, party)

    def insert_candidate(self, id_number, name, state, age, password, qualification, party):
        try:
            # Execute query to insert a new record in the candidate table
            insert_candidate = "INSERT INTO candidates (id, name, age, qualification, state, party) VALUES (%s, %s, %s, %s, %s, %s)"
            candidate_data = (id_number, name, age, qualification, state, party)
            self.cursor.execute(insert_candidate, candidate_data)

            # Execute query to insert a new record in the voters_details table
            insert_voter = "INSERT INTO voters_details (id, name, state, age, password) VALUES (%s, %s, %s, %s, %s)"
            voter_data = (id_number, name, state, age, password)
            self.cursor.execute(insert_voter, voter_data)

            self.con.commit()
            print("Record added successfully")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def update_candidate(self):
        print("-----------------Update Candidate details-----------------")
        a = int(input("Enter how many records you want to update: "))
        for i in range(a):
            current_id = input("Enter the current id Number: ")
            id_number = input("Enter the updated id number: ")
            name = input("Enter the updated Candidate name: ")
            state = input("Enter the updated State: ")
            age = int(input("Enter the Updated Age: "))
            password = input("Enter the Updated password: ")
            qualification = input("Enter the Qualification: ")
            party = input("Enter the party name: ")
            
            self.update_candidate_details(current_id, id_number, name, state, age, password, qualification, party)

    def update_candidate_details(self, current_id, id_number, name, state, age, password, qualification, party):
        try:
            # Execute query to update the record in voters_details table
            query = "UPDATE voters_details SET id = %s, name = %s, state = %s, age = %s, password = %s WHERE id = %s"
            self.cursor.execute(query, (id_number, name, state, age, password, current_id))
            self.con.commit()
            print("Candidate details updated successfully.")

            # Execute query to update the record in candidates table
            query = "UPDATE candidates SET id = %s,state= %s ,age =%s,name = %s, qualification = %s, party = %s WHERE id = %s"
            self.cursor.execute(query, (id_number, state,age,name, qualification, party, current_id))
            self.con.commit()
            print("Candidate details updated in the candidates table.")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

        finally:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()
                print("MySQL connection is closed")

    def delete_candidate(self):
        print("-----------------Delete Candidate details-----------------")
        a = int(input("Enter how many records you want to delete: "))
        for i in range(a):
            id_number = input("Enter the id number to delete: ")
            self.delete_candidate_details(id_number)

    def delete_candidate_details(self, id_number):
        try:
            # Execute query to delete the record
            query = "DELETE FROM candidates WHERE id = %s"
            self.cursor.execute(query, (id_number,))
            self.con.commit()
            print("Record deleted successfully")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def view_candidate(self):
        print("-----------------View Candidate Details-----------------")
        a = int(input("Enter how many records you want to view: "))
        for i in range(a):
            id_number = input("Enter the id number to view: ")
            self.view_candidate_details(id_number)

    def view_candidate_details(self, id_number):
        try:
            # Execute query to fetch the record
            query = "SELECT * FROM candidates WHERE id = %s"
            self.cursor.execute(query, (id_number,))
            records = self.cursor.fetchall()

            if len(records) == 0:
                print("No records found.")
            else:
                print("\tNumber\tName\tNIC\tAge\tQualification\tState\tParty")
                print("---------------------------------------------------------")
                for row in records:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t\t{row[4]}\t{row[5]}\t{row[6]}")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

   

    def display_vote_count(self):
        try:
            query = "SELECT candidate_number, count FROM vote_count"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("No vote counts available.")
            else:
                print("Candidate Number\tVote Count")
                print("-----------------------------")
                for row in records:
                    candidate_number = row[0]
                    vote_count = row[1]
                    print(f"{candidate_number}\t\t{vote_count}")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    def display_party_vote_count(self):
        try:
            query = "SELECT number, name, vote_count FROM party"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("No party vote counts available.")
            else:
                print("Party Number\tParty Name\tVote Count")
                print("-----------------------------------------")
                for row in records:
                    party_number = row[0]
                    party_name = row[1]
                    vote_count = row[2]
                    print(f"{party_number}\t\t{party_name}\t\t{vote_count}")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    

    def display_vote_count_chart(self):
        try:
            query = "SELECT candidate_number, count FROM vote_count"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("No vote counts available.")
            else:
                candidate_numbers = []
                vote_counts = []

                for row in records:
                    candidate_number = row[0]
                    vote_count = row[1]
                    candidate_numbers.append(candidate_number)
                    vote_counts.append(vote_count)

                # Create the bar chart
                plt.bar(candidate_numbers, vote_counts)
                plt.xlabel("Candidate Number")
                plt.ylabel("Vote Count")
                plt.title("Vote Count by Candidate")
                plt.show()

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

    

    def display_party_vote_count_chart(self):
        try:
            query = "SELECT number, name, vote_count FROM party"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            if not records:
                print("No party vote counts available.")
            else:
                party_numbers = []
                vote_counts = []

                for row in records:
                    party_number = row[0]
                    vote_count = row[2]
                    party_numbers.append(party_number)
                    vote_counts.append(vote_count)

                # Create the bar chart
                plt.bar(party_numbers, vote_counts)
                plt.xlabel("Party Number")
                plt.ylabel("Vote Count")
                plt.title("Vote Count by Party")
                plt.show()

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

   

    def add_new_party(self):
        try:
            party_name = input("Enter the party name: ")
            count = 0

            query = "INSERT INTO party (name, vote_count) VALUES (%s, %s)"
            self.cursor.execute(query, (party_name, count))
            self.con.commit()

            print("New party added successfully.")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

        finally:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()

 

    def update_party(self):
        try:
            party_number = input("Enter the party number to update: ")
            new_party_name = input("Enter the new party name: ")

            query = "UPDATE party SET name = %s WHERE number = %s"
            self.cursor.execute(query, (new_party_name, party_number))
            self.con.commit()

            print("Party updated successfully.")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

        finally:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()

        

    def view_parties(self):
        try:
            query = "SELECT * FROM party"
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print("\tNumber\tParty Name")
            print("---------------------------------")
            for row in records:
                print(f"\t{row[0]}\t{row[1]}")

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

        finally:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()

        




    

        









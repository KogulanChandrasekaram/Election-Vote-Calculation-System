import mysql.connector
from admin_function import AdminSystem
import sys
import os



class VotingSystem:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="voting_system")
        self.cursor = self.con.cursor()

    def calculate_votes(self, user_id, votes):
        # Call result calculate function
        vote_count = {}
        for candidate_number in votes:
            if candidate_number in vote_count:
                vote_count[candidate_number] += 1
            else:
                vote_count[candidate_number] = 1
        return vote_count

    def vote(self, user_id):
        try:
            # Display parties
            query = "SELECT * FROM party"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print("Number\tParty Name")
            print("----------------------------")
            for row in records:
                print(f"{row[0]}\t{row[1]}")

            party_number = input("Enter the party number: ")
            count = 1

            query1 = "INSERT INTO party (number, vote_count) VALUES (%s, %s) ON DUPLICATE KEY UPDATE vote_count = vote_count + %s"
            self.cursor.execute(query1, (party_number, count, count))
            self.con.commit()



            # Execute query to fetch table data
            query = "SELECT * FROM candidates WHERE state = (SELECT state FROM voters_details WHERE id = %s) AND party = (SELECT name FROM party WHERE number = %s)"

            # Specify the desired parameters here
            self.cursor.execute(query, (user_id, party_number))
            records = self.cursor.fetchall()

            # Print table headers
            print("Number\t NIC\t \tName \tAge \tQualification \tState \tParty")
            print("-------------------------------------------------------")

            # Print table data
            for row in records:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")

            votes = []
            i = 1
            while i < 4:
                candidate_number = input(f"\nEnter the Candidate number {i}: ")
                if candidate_number in votes:
                    print("Duplicate candidate number. Please enter a different number.")
                    continue
                votes.append(candidate_number)
                i += 1

            print("Entered 3 candidate numbers successfully.")

            vote_counts = self.calculate_votes(user_id, votes)

            # Store vote counts in the database or perform any necessary actions
            for candidate_number, count in vote_counts.items():
                query = "INSERT INTO vote_count (candidate_number, count) VALUES (%s, %s)ON DUPLICATE KEY UPDATE count = count + %s"
                self.cursor.execute(query, (candidate_number, count, count))
                self.con.commit()

            print("Vote counts calculated and stored successfully.")
            print("Thanks for voting.....")


            

        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database: {}".format(error))

        finally:
            if self.con.is_connected():
                self.cursor.close()
                self.con.close()
                print("MySQL connection is closed")

 
def welcome():

    admin_system = AdminSystem()
    os.system("COLOR A")
    print("\t-----------------------------------------------------------------------")
    print("\t      ************* Welcome to Election System *************")
    print("\t-----------------------------------------------------------------------")

    print("\t\t1. User Login\n"
      "\t\t2. Admin Login\n"
      "\t\t3. Exit\n")
    choice = int(input("Enter your choice: "))
    while choice !=0:
        if choice == 1:
            user_id = int(input("\nEnter user ID: "))
            password = input("Enter password: ")
            

            # Database connection
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="voting_system")
                cursor = con.cursor()

                # Execute query to fetch user record
                query = "SELECT id FROM voters_details WHERE id = %s AND password = %s AND age >18 "
                cursor.execute(query, (user_id, password))
                record = cursor.fetchone()

                if record:
                    print("Login Successful.")
                    voting_system = VotingSystem()
                    voting_system.vote(user_id)
                    os.system('cls')
                    # Call user function from user log in file
                else:
                    print("Invalid credentials. Please try again.")

            except mysql.connector.Error as error:
                print("Failed to connect to MySQL database: {}".format(error))

            finally:
                if con.is_connected():
                    cursor.close()
                    con.close()
                    print("MySQL connection is closed")

        elif choice == 2:
            admin_id = int(input("Enter Admin ID: "))
            password = input("Enter password: ")

            if admin_id == 123 and password == 'abc123':
                a = -1

                while a !=0:
                    os.system("COLOR B")
                    print("\t\t1. Citizen List\n"
                      "\t\t2. Candidate List\n"
                      "\t\t3. Result\n"
                      "\t\t4. Parties\n"
                      "\t\t5. Exit \n")
                    a = int(input("Enter the number: "))
                    os.system("cls")

                    if a == 1:
                        os.system("COLOR B")
                        print("\t\t----------Citizen List----------")
                        print("\t\t1. Add New Citizens\n"
                              "\t\t2. Update Citizen List\n"
                              "\t\t3. Delete Citizen\n"
                              "\t\t4. View Citizen List\n")
                        b = int(input("Enter your choice: "))
                        os.system("cls")
                        if b == 1:
                            admin_system.add_citizen()
                        elif b == 2:
                            admin_system.update_citizen()

                        elif b == 3:
                            admin_system.delete_citizen()

                        elif b == 4:
                            admin_system.view_citizen()
                        else:
                            print("Enter the valid number.....")

                    elif a == 2:
                        os.system("COLOR B")
                        print("\t\t----------Candidate List----------")
                        print("\t\t1. Add New Candidate\n"
                              "\t\t2. Update Candidate List\n"
                              "\t\t3. Delete Candidate\n"
                              "\t\t4. View Candidate Details\n")
                        b = int(input("Enter your choice: "))
                        os.system("cls")
                        if b == 1:
                            admin_system.add_candidate()
                        elif b == 2:
                            admin_system.update_candidate()

                        elif b == 3:
                            admin_system.delete_candidate()

                        elif b == 4:
                            admin_system.view_candidate()

                        else:
                            print("Enter the valid number.....")

                    elif a == 3:
                        os.system("COLOR B")
                        print("-----------View Election Result------------")
                        print("\t\t1. Party Vote Count\n"
                                "\t\t2. Candidate Vote Count\n")

                        a = int (input("Enter the number :"))
                        os.system("cls")
                        if a == 1:
                            admin_system.display_party_vote_count()
                            admin_system.display_party_vote_count_chart()
                        elif a == 2:
                            admin_system.display_vote_count()
                            admin_system.display_vote_count_chart()  
                        else :
                            print("Enter the Valid Number..")
                        
                            

                    elif a == 4:
                        os.system("COLOR B")
                        print("\t-------------Party Details-------------\n")
                        print("\t\t1. Add new party\n"
                                  "\t\t2. Update Party\n"
                                  "\t\t3. view Party\n")
                        b = int(input("Enter the number: "))
                        os.system("cls")
                        if b == 1:
                            admin_system.add_new_party()
                        elif b == 2:
                            admin_system.update_party()

                        elif b == 3:
                            admin_system.view_parties()
                        else:
                            print("Enter the valid number.....")
                    elif a == 5:
                        print("Exiting...")
                        sys.exit()
                        
                    else:
                        print("Enter valid Number")

                else:
                    print("Invalid credentials. Please try again.")
                os.system("COLOR B")
                print("\t\t1. Citizen List\n"
                      "\t\t2. Candidate List\n"
                      "\t\t3. Result\n"
                      "\t\t4. Exit \n")
                a = int(input("Enter the number: "))
                os.system("cls")
            
        
            
        elif choice == 3:
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")
        

#call function
welcome()

    




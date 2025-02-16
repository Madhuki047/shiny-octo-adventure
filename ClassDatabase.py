import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.db = self.connect_db()                     # Initialize the database connection
        self.cursor = self.db.cursor(buffered=True)     # Initialize a cursor for executing queries
        self.cursor = self.db.cursor()                  
        self.create_table()                             # Create the contacts table if it doesn't exist

    # Connect to the MySQL database
    def connect_db(self):
        try:
            return mysql.connector.connect(
                host="localhost",                # Database server address
                user="root",                     # Database user
                password="root",                 # User password
                database="contact_log"           # 
            )
        except Error as e:
            raise Exception(f"Error connecting to db: {e}")

    # Creates a table in SQL Databse
    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    surname VARCHAR(255) NOT NULL,
                    phone VARCHAR(255) NOT NULL,
                    email VARCHAR(255)
                )
            """)
        except Error as e:
            raise Exception(f"Error creating table: {e}")

    # 
    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            self.db.commit()
        except Error as e:
            raise Exception(f"Error executing query: {e}")

    def fetch_data(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return []
        
        
    def reassign_ids(self):
        try:
            self.cursor.execute("SET @count = 0")
            self.cursor.execute("UPDATE contacts SET id = @count:= @count + 1")
            self.cursor.execute("ALTER TABLE contacts AUTO_INCREMENT = 1")
            self.db.commit()
        except Error as e:
            raise Exception(f"Error reassigning IDs: {e}")
        
        
        
        
class DatabaseManagement:
    def __init__(self, db):
        self.db = db

    def add_contact(self, contact):
        query = "INSERT INTO contacts (first_name, surname, phone, email) VALUES (%s, %s, %s, %s)"
        values = (contact.first_name, contact.surname, contact.phone, contact.email)
        self.db.execute_query(query, values)
        print(f"Contact {contact.first_name} added.")

    def view_contacts(self):
        return self.db.fetch_data()

    def delete_contact(self, first_name, surname, phone, email):
        query = "DELETE FROM contacts WHERE first_name = %s AND surname = %s AND phone = %s AND email = %s"
        values = (first_name, surname, phone, email)
        self.db.execute_query(query, values)
        self.db.reassign_ids()
        print(f"Contact {first_name} {surname} deleted.")

    def update_contact(self, contact, contact_id):
        query = """
        UPDATE contacts SET first_name = %s, surname = %s, phone = %s, email = %s WHERE id = %s
        """
        values = (contact.first_name, contact.surname, contact.phone, contact.email, contact_id)
        self.db.execute_query(query, values)
        print(f"Contact {contact.first_name} {contact.surname} updated.")
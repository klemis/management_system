import sqlite3
from sqlite3 import Error

class DatabaseOperation:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        """Create a database connection to a SQLite database"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ Create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_patient(self, conn, patient):
        """Create a new patient into patients table
        :param conn:
        :param patient:
        :return: patient id
        """
        sql = ''' INSERT INTO patients(name, surname, birthdate, address, telephone, email)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, patient)
        return cur.lastrowid

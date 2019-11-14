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

    def create_data(self, conn, patient):
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

    def update_data(self, conn, patient):
        """
        update
        :param conn:
        :param patient:
        :return: patient id
        """
        sql = ''' UPDATE patients
                  SET   name = ?,
                        surname = ?,
                        birthdate = ?,
                        address = ?,
                        telephone = ?,
                        email = ?
                  WHERE id = ?'''

        cur = conn.cursor()
        cur.execute(sql, patient)
        conn.commit()

    def select_data(self, conn, id):
        """
        Query data by id
        :param conn: the Connection object
        :param id:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM patients WHERE id=?", (id,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def delete_data(self, conn, id):
        """
        Delete a data by id
        :param conn:  Connection to the SQLite database
        :param id: id of the patient
        :return:
        """
        sql = 'DELETE FROM patients WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()

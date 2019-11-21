from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error


class DatabaseOperation:

    def read_db_config(self, filename='db/config.ini', section='mysql'):
        """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """
        # create parser and read ini configuration file
        parser = ConfigParser()
        parser.read(filename)

        # get section, default to mysql
        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception('{0} not in {1} file'.format(section, filename))

        return db

    def connect(self):
        """ Connect to MySQL database """
        db_config = self.read_db_config()
        conn = None
        try:
            print('Connecting to MySQL database...')
            conn = MySQLConnection(**db_config)

            if conn.is_connected():
                print('Connected to MySQL database')
            else:
                print('Connection failed')

        except Error as e:
            print(e)

        return conn

    def create_table(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            name VARCHAR(255),
                                            surname VARCHAR(255),
                                            birthdate VARCHAR(255),
                                            address VARCHAR(255),
                                            telephone INT,
                                            email VARCHAR(255))""")
        except Error as e:
            print(e)

        finally:
            self.disconnect(conn)

    def query_with_fetchone(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients")

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

        except Error as e:
            print(e)

        finally:
            self.disconnect(conn)

    def insert_record(self, name, surname, birthdate, address, telephone, email):
        query = "INSERT INTO patients(name,surname,birthdate,address,telephone,email) " \
                "VALUES(%s,%s,%s,%s,%s,%s)"

        args = (name, surname, birthdate, address, telephone, email)

        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            conn.commit()

        except Error as error:
            print(error)

        finally:
            self.disconnect(conn)

    def update_record(self, patient_id, name):
        # prepare query and data
        query = """ UPDATE patients
                    SET name = %s
                    WHERE id = %s """

        data = (name, patient_id)

        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)

            # accept the changes
            conn.commit()

        except Error as error:
            print(error)

        finally:
            self.disconnect(conn)

    def disconnect(self, conn):
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    db = DatabaseOperation()
    db.insert_record('Andrzej', 'Dupka', '01.02.1977', 'Bialystok', 123090847, 'tomek@tomek.pl')
    db.update_record(2, 'Marek')
    db.query_with_fetchone()

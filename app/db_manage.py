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
            raise Exception('{0} not found in the {1} file'.format(section, filename))

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
     
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
 
 
if __name__ == '__main__':
    db = DatabaseOperation()
    db.connect()
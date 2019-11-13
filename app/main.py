from patient import ManagePatient
from db_management import DatabaseOperation


def main():
    database = '/home/ute/PycharmProjects/Management/db/pythonsqlite.db'
    sql_patients_table = """ CREATE TABLE IF NOT EXISTS patients (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            surname text NOT NULL,
                                            birthdate text NOT NULL,
                                            address text NOT NULL,
                                            telephone INTEGER,
                                            email text NOT NULL
                                        ); """

    person_1 = ManagePatient('Tomasz', 'Chada', '04.02.1977', 'Bialystok', '123090847', 'tomek@tomek.pl')
    person_1.print_patient_info()

    db = DatabaseOperation(database)
    conn = db.create_connection()

    if conn is not None:
        # create patients table
        db.create_table(conn, sql_patients_table)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        # create a new patient
        patient_1 = ('Tomasz', 'Chada', '01.02.1977', 'Bialystok', 123090847, 'tomek@tomek.pl');
        patient_2 = ('Andzej', 'Dupa', '14.02.1977', 'Sady', 123090847, 'Andzej@tomek.pl');
        patient_3 = ('Pawel', 'Abc', '22.02.1977', 'Pola', 123090847, 'Pawel@tomek.pl');
        db.create_patient(conn, patient_1)
        db.create_patient(conn, patient_2)
        patient_id = db.create_patient(conn, patient_3)
        print('Last row id : {}'.format(patient_id))

        db.update_patients(conn, ('U', 'U', '0.0.0', 'U', 123090847, 'U@u.pl', patient_id))


if __name__ == "__main__":
    main()

# TODO
# Database operations:
#   - update specific fields in row instead of the whole row (default actual values)
# Manage patients (add, remove, update)
# Book an appointment
# Search records

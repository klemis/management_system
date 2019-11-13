class ManagePatient:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def add_patient(self):
        pass

    def remove_patient(self):
        pass

    def update_patient(self):
        pass

    def print_patient_info(self):
        print("[DEBUG] Name, surname : {} {} ".format(self.name, self.surname))

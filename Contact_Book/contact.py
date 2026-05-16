class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.name} : {self.phone}")
        pass

    def to_dict(self):
        contact_dict = {}
        contact_dict['name'] = self.name
        contact_dict['phone'] = self.phone
        return contact_dict




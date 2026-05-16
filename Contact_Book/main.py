from contact import Contact
import json
import os

def load_contacts():
    listOfContacts = []
    try:
        file_name = 'contacts.json'
        with open(file_name, 'r') as file:
            contactList = json.load(file)
            for entry in contactList:
                name = entry['name']
                phone = entry['phone']
                listOfContacts.append(Contact(name,phone))
            return listOfContacts
    except FileNotFoundError:
        return listOfContacts
    
def save_contacts(listofContacts):
    saved_contacts = []
    for contact in listofContacts:
        saved_contacts.append(contact.to_dict())
    with open('contacts.json', 'w') as file:
        json.dump(saved_contacts, file, indent=2) 

def add_contact(listOfContacts):
    name = input('What is the name for the contact? ')
    while True:
        phoneNum = input('What is the phone number for the contact? (Ex: 1234567890) : ')
        if len(phoneNum) != 10 or not phoneNum.isdigit():
            print('Give a number that is only 10 digits long.')
            continue
        else:
            break
    new_contact = Contact(name,phoneNum)
    listOfContacts.append(new_contact)
    save_contacts(listOfContacts)
    return listOfContacts

def view_all(listOfContacts):
    if not listOfContacts:
        print("No contacts.")
    else:
        for contact in listOfContacts:
            contact.display()
    return

def search_contacts(listOfContacts):
    name = input("What name would you like to search? ")
    check = False
    for contact in listOfContacts:
        if name == contact.name:
            contact.display()
            check = True
    if not check:
        print("\nContact not found.")
    return

def remove_contact(listOfContacts):
    name = input("What is the name of the contact you would like to remove? ")
    check = False
    for contact in listOfContacts:
        phone_num = contact.phone
        if name == contact.name:
            print(f"\n{name} with the number {phone_num} is removed from the contact list.")
            listOfContacts.remove(contact)
            check = True
            save_contacts(listOfContacts)
            break
    if not check:
        print("\nContact not found")
    return



listOfContacts = load_contacts()
while True:
    
    print(f'\nWelcome to your Contact Book! \n 1. Add contact \n 2. View all contacts \n 3. Search contact \n 4. Remove contact \n 5. Quit')
    option = input('\nChoose an option (1-5): ')
    try:
        option = int(option)
    except ValueError:
        print("Please select a correct option (1-5).")
        continue
    
    if option == 1:
        add_contact(listOfContacts)
    elif option == 2:
        view_all(listOfContacts)
    elif option == 3:
        search_contacts(listOfContacts)
    elif option == 4:
        remove_contact(listOfContacts)
    elif option == 5:
        break
    else:
        print("Please select a correct option (1-5).")
        


    







        





import os, pickle

phonebook = []

class Person(object):
    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone

def save_data():
    global phonebook
    phonebook_data_file = open('phonebook_data.pickle', 'w+')
    pickle.dump(phonebook, phonebook_data_file)
    phonebook_data_file.close()

def retrieve_data():
    global phonebook
    if os.path.isfile("phonebook_data.pickle") == True:
        retrieved_data_file = open('phonebook_data.pickle', 'r+')
        phonebook = pickle.load(retrieved_data_file)
        retrieved_data_file.close()
        print '**** RETRIEVED ****\n'
        print phonebook[0].first
    else:
        phonebook = []

user_action = 0
while user_action != 7:

    print '''
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save all entries
    6. Retrieve saved entries
    7. Quit
    
    '''
    while True:
        try:
            user_action = int(raw_input('What do you want to do (1-7)? '))
        except ValueError:
            user_action = 0
            print '\n*----Enter a number (1-7), please.\n'
        break
# LOOK UP ENTRY
    if user_action == 1:
        person_found = False
        person_to_find = raw_input('Person to Find (first name): ')
        for entry in phonebook:
            if entry.first == person_to_find:
                person_to_find = True
                print '\n*** FOUND ***\n %s %s, %s, %s' % (
                    entry.first, 
                    entry.last, 
                    entry.email, 
                    entry.phone
                ) 
        if person_found == False:
            print '\n** NOT FOUND **\n'


# SET ENTRY
    if user_action == 2:
        first = raw_input('First Name: ')
        last = raw_input('Last Name: ')
        email = raw_input('Email: ')
        phone = raw_input('Phone: ')
        new_person = Person(first, last, email, phone)
        phonebook.append(new_person)

# DELETE ENTRY
    if user_action == 3:
        person_to_remove = raw_input('Person to Remove (first name): ')
        for i in range(0, len(phonebook)):
            if phonebook[i].first == person_to_remove:
                are_you_sure = raw_input('Remove %s %s (Y/N)? ' % (phonebook[i].first, phonebook[i].last))
                if are_you_sure.upper() == 'Y' or are_you_sure.upper() == 'YES':
                    phonebook.remove(phonebook[i])
                else:
                    print 'OK. As you were...'

# LIST ALL ENTRIES
    if user_action == 4:
        for i in range(0, len(phonebook)):
            print '\n***%s %s, %s, %s' % (
                phonebook[i].first, phonebook[i].last, phonebook[i].email, phonebook[i].phone
                )

# SAVE ENTRIES
    if user_action == 5:
        save_data()
        print '\n***********\n** Saved **\n***********\n'

# RETRIEVE ENTRIES
    if user_action == 6:
        retrieve_data()



print 'Bye!'  

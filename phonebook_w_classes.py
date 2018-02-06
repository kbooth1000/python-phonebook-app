phonebook = []

class Person(object):
    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone

user_action = 0
while user_action != 5:

    print '''
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    
    '''
    while True:
        try:
            user_action = int(raw_input('What do you want to do (1-5)? '))
        except ValueError:
            user_action = 0
            print '\n*----Enter a number (1-5), please.\n'
        break
# LOOK UP ENTRY
    if user_action == 1:
        person_to_find = raw_input('Person to Find (first name): ')
        for i in range(0, len(phonebook)):
            if phonebook[i].first == person_to_find:
                print '*******\n%s %s, %s, %s' % (
                    phonebook[i].first, 
                    phonebook[i].last, 
                    phonebook[i].email, 
                    phonebook[i].phone
                ) 


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
            if phonebook[i].first == person_to_find:
                are_you_sure = raw_input('Remove %s %s? ' % (phonebook[i].first, phonebook[i].last))
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


print 'Bye!'  

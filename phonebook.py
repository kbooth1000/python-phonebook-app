phonebook = [
    { 1:  
        {
            'first_name': 'Jim',
            'last_name': 'Jones',
            'phone': '212-675-8570'
        }
    },
    { 2: 
        {   
            'first_name': 'Jamal',
            'last_name': 'Fletcher',
            'phone': '303-724-7371'
        }
    },
    { 3: 
        {
            'first_name': 'Francine',
            'last_name': 'Redfield',
            'phone': '913-388-2079'}
        },
    { 4: 
        {
            'first_name': 'Anne',
            'last_name': 'Johnson',
            'phone': '404-339-7942'
        }
    },
    { 5: 
        {
            'first_name': 'Glen',
            'last_name': 'Jones',
            'phone': '212-462-9157'
        }
    }
]

print '''1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Sort by first name, last name or phone number
6. Quit
6. Sort by Name
7. Sort by Number
'''

def pb_search(f_name):
    return_list = []
    #if phonebook[f_name]:
    for entry in phonebook:
        if entry == f_name:
            return_list.append('%s, %s' % (f_name, phonebook[f_name]) )
            return return_list

def pb_set(f_name, tel):
    phonebook[f_name] = tel
    return 'Entry added (%s, %s) ' % (f_name,tel)
    #else:
     #   return 'Name not in phonebook.'

def pb_delete(f_name):
    tel_num = phonebook[f_name]
    phonebook.pop(f_name)
    return 'Entry (%s, %s) removed.' % (f_name, tel_num)

def pb_sort_by_name():
    return sorted(phonebook)

def pb_sort_by_num():
    tmp_list = []
    for contact in phonebook:
        for ph_num in contact.items():
            tmp_row =ph_num[1]['phone'], ph_num[1]['first_name'], ph_num[1]['last_name']
            tmp_list.append(tmp_row)
    return sorted(tmp_list, key=lambda contact: contact[1])

def pb_sort_by(what):
    tmp_list = []
    for contact in phonebook:
        for ph_num in contact.items():
            tmp_row =ph_num[1]['phone'], ph_num[1]['first_name'], ph_num[1]['last_name']
            tmp_list.append(tmp_row)
    return sorted(tmp_list, key=lambda contact: contact[what])

def what_action():
    action = int(raw_input('What do you want to do (1-5)? '))
    if action == 1:
        f_name = raw_input('Name: ')
        print pb_search(f_name)
        what_action()
    elif action == 2:
        f_name = raw_input('Name to add: ')
        tel = raw_input('Phone: ')
        print pb_set(f_name, tel)
        what_action()
    elif action == 3:
        f_name = raw_input('Name to remove: ')
        print pb_delete(f_name)
        print phonebook
        what_action()
    elif action == 4:
        print phonebook
        what_action()
    elif action == 5:
        what = int(raw_input('Sort by 1. first name, 2. last name or 3. phone number (1-3)'))
        what -= 1
        print
        print pb_sort_by(what)
        print
        what_action()
    elif action == 6:
        print
        print pb_sort_by_num()
        print
        what_action()
    elif action == 7:
        print 'OK. All done.'
    else:
        print 'I don\'t recognize that command.'
        what_action()

#print sorted(phonebook)
what_action()
#exersise 1

def address_book():
    book = {}
    while True:
        key_name = input('What is the name of the person you would like to add to your address book? ')
        if key_name not in book:
            book[key_name] = input(f"What is {key_name}'s address? ")
        else:
            current_address = input(
                f"The address we have on file for this person is {key_name.get()}. Is this correct? y/n")
            if current_address == 'n':
                new_address = input(f"What is {key_name}'s new address? ")
                book[key_name] = new_address
            else:
                print("Great! Thank you for confirming.")
        next = input("Would you like to add another person to the address book? y/n ")
        if next == 'n':
            break
    for key, value in book.items():
        return f"{key} lives at {value}"

address_book()
book = {}



#exersise 2
person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']

def avail_meet_times(original_list, *args):
    orig_set = set(original_list)
    # print(orig_set)
    for person_avail in args:
        avail_set = set(person_avail)
        orig_set = orig_set.intersection(avail_set)
    print(orig_set)


avail_meet_times(person1, person2, person3, person4)
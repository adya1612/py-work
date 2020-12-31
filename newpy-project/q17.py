# adding an element to the tuple

def add_element(new_dance_form):
    dance_form = ("Samba", "Tango", "Ballet", "Tap", "Modern", "Jazz", "Hip-hop")
    list_dance_form = list(dance_form)
    print(f"These were the given dance forms:\n {dance_form}")
    list_dance_form.append(new_dance_form)
    print("These are the updated dance forms: ")
    print(tuple(list_dance_form))


add_element(input("Enter any one dance form: "))

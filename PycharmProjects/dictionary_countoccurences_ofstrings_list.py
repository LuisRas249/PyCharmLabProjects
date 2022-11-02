# Example to count occurences of strings in a list
def tally_staff(sL):
    # Create a dictionary to hold the name
    name_dict = {}

    # Step through the list of staff
    for staff in sL:
        # Step through the list of names
        # If the names is in the dictionary
        if staff in name_dict:
            # Update the existing element
            name_dict[staff] = int(name_dict[staff]) + 1
        else:
            #Otherwise, store the word in the dictionary
            name_dict[staff] = 1

    for key, value in name_dict.items():
        # Print the word
        print(key + ': ', value)

# Create e sample list
#staff_list = ['Simon', 'Mark', 'Mark', 'Peter', 'Leo', 'Leo', 'George', 'Ian', 'Pat', 'Nicola']

# Call the function
tally_staff(sL)
# Program to demonstrate object pickling
import pickle

# main function
def main():
    # Check if the user wants to enter more information
    again = 'y' # to control the loop repetition

    output_file = open('info.dat', 'wb')

    while again.lower() == 'y' or again.lower() == 'Y':
        save_data(output_file)

        again = input('Enter more data? (y/n): ')

    output_file.close()

def save_data(file):
    person = {}

    person['name'] = input('Name: ')
    person['age'] = input('Age: ')
    person['weight'] = input('Weight: ')

    pickle.dump(person, file)

main()
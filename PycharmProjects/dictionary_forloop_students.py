# Write a program that utilizes a for loop to collect 4 student names(key)
# and their ages(value), which are stored in a dictionary called register

# Print out the number of items in the dictionary

# Use a for loop to iterate in the dictionary,
# Listing names(keys)

students = ['Luis', 21, 'Kobe', 41, 'Kyrie', 29, 'Jayson', 20]

print(students)
# Create a blank dictionary called register
register = {}
# Iterate around the list four times in order to capture a name and an age
for each_student in range(4):
    key = input('Please enter the students name: ')
    value = int(input('Please enter students age: '))
    # Stored into the register using the name as the key and age as the value
    register[key] = value

# Use the len method to find out how many items are stored
print('The register contains: ', len(register), 'students')

# Iterate through out the dictionary to print out the details
for student in register:
    print(student, register[student], sep='->')
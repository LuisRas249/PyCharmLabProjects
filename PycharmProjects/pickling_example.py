# Import pickle
import pickle
# Dictionary of student and age
students_dict = {'Chris': 21, 'Paula': 22, 'Lucy': 21, \
                 'Sarah': 19, 'Michael': 20, 'Bruce': 21}

# Create an out_file and open that for writing
out_file = open('student_store.dat', 'wb')
pickle.dump(students_dict, out_file)
out_file.close()

# Input the file then create a reference to the file and opening that file for reading
input_file = open('student_store.dat', 'rb')
new_stud_dict = pickle.load(input_file)

# Test it by creating a simple for loop that goes through each item in the dictionary
# and print out the key and value pairs
for stud in new_stud_dict:
    print(stud, new_stud_dict[stud])
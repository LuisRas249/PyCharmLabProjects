# Program that reads actor grades from a file and stores these to a 2d list

# Import matplotlib that provides charting features
import matplotlib.pyplot as plt

# Set the list
actor_grade_list = []
# Read from the file
def read_file():
    infile = open('actor_grades.txt')

    # Search through a parse in the file to the list
   for row in infile:
        start = 0 # Used to point to the current position in each line
        string_builder = []
        if not row.startswith('#'):
            for index in range(len(row)):
                # Go to each row and go through until we reach a comma or the end of the line
                if row[index] == ',' or index == len(row)-1:
                    string_builder.append(row[start:index])
                    start = index + 1
                # Build up our list
            actor_grade_list.append(string_builder)
        infile.close()
def read_file():
    infile = open('actor_grades.txt')
    for row in infile:
        if not row.startswith('#'):
            row = row.rstrip('\n').split(', ')
            actor_grade_list.append(row)
    infile.close()
# Print a summary
def print_summary():
    total_tally = 0
    for each_actor in actor_grade_list:
        print(each_actor[0], each_actor[1], each_actor[2], sep='-->')
        total_tally += float(each_actor[2])
    print('Total number of actors', len(actor_grade_list))
    print('\n','The combined scores of all actors is: ', format(total_tally, '.2f'))
    print('\n','The average score is: ', format(total_tally / len(actor_grade_list), '.2f'))

# Find the lowest score
def get_minimum():
    minimum_grade = actor_grade_list[0]
    for current_actor in actor_grade_list:
        if current_actor[2] < minimum_grade[2]:
            minimum_grade = current_actor
    return minimum_grade

def plot_results():
    grade = []
    name_details = []
    for current_actor in open('actor_grades.txt', 'r'):
        grade.append(current_actor[1])
        name_details.append((current_actor[2]))

    plt.bar(grade, name_details)
    plt.title('Record Genre')
    plt.show()

def actor_search():
    again = 'y'
    while again =='y':
        name = input('Which Actor do you wish to search for? ')

        for each_actor in actor_grade_list:
            if name in each_actor:
                print('Success - found')
                print(each_actor[0], each_actor[1], each_actor[2], sep='->')
        again = input('Search again?')

def tally_student_type(aL):
    student_type_dict = {}
    for each_actor in aL:
        if each_actor[2] in student_type_dict:
            student_type_dict[each_actor[2]] = int(student_type_dict[each_actor[2]])+1
        else:
            student_type_dict[each_actor[2]] = 1

    for key, value in student_type_dict.items():
        print(key + '--> ', value)
# main
read_file()
print_summary()
print('\n', 'The minimum actor grade is: ', get_minimum())
plot_results()
actor_search()
tally_student_type(actor_grade_list)

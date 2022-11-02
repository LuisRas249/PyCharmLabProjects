# This is a program that creates a dictionary object called people
# Includes a number of names as keys and their respective age values

peoples = {'Luis': 21, 'Paolo': 19, 'Anne':52, 'Peter': 52}
print(peoples, '\n')

# Create an input to search one of the peoples in the dictionary
search = input('Enter a name: ')

if search in peoples:
    print(search, "'s age is: ", peoples[search], sep='')
else:
    print(search, 'Try again, not found in dictionary')

# Search the dictionary for a name entered
# Then print out a message indicating wether or not an item was found
people = {'Luis':'21', 'Paolo':'19', 'Anne':'52', 'Peter': '52'}
print('Luis' in people)
if 'Luis' in people:
    print(people['Luis'])



# Creating an Empty Dictionary and using for Loop to iterate over a Dictionary
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Create a new dictionary ‘planet_to_initial’
planet_to_initial = {}
# ‘planet’ is a variable references the items in the list
for planet in planets:
    planet_to_initial[planet] = planet[0]
print(planet_to_initial)

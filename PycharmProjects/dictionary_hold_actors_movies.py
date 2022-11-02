# Dictionary object to hold actor and movies

actor_dictionary = {'Daniel Craig': ['Casino Royale', 'Skyfall', 'Spectre'], \
                    'Tom Cruise': ['Mission Impossible', 'Vanilla Sky', 'Top Gun'], \
                    'Rowan Atkinson': ['Mr Bean', 'Johnny English']}

# Use the items function to return dictionary view
for key, value in actor_dictionary.items():
    print(key, value)

# Use the len function to get the size of each list contained in the dictionary
for key in actor_dictionary:
    print('\n', key, len(actor_dictionary[key]), '\n')

# Use lambda with sorted function to order actors by surname
for key, value in sorted(actor_dictionary.items(), key = lambda x: x[1]):
    print(key)

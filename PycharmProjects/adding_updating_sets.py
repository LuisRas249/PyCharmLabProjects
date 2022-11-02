# A set of letters
GEEK = {'g', 'e', 'k'}

GEEK.add('s') # Adding letter 's' in the set
print('The letters are: ', GEEK)

GEEK.add('s') # Adding letter 's' again
print('The letters are: ', GEEK)

# Showing the update() method
list1 = [1,2,3]
list2 = [5,6,7]
list3 = [10,11,12]

# Lists converted to sets
set1 = set(list2)
set2 = set(list1)

set1.update(set2)
# Update method
print(set1) # Print the updated set

# List is passed as an parameter - automatically converted to a set
set1.update(list3)
print(set1)

# remove(), discard(), and clear() methods

set1.remove(1)
print('\n', set1)
set1.discard(2)
print(set1)
set1.discard(2)
print(set1)

try:
    set1.remove(1)
    print(set1)
except KeyError:
    print('Something went wrong')
# This program demonstrates various set operations
baseball = set(['Jodi', 'Carmen', 'Aida', 'Lisa'])
basketball = set(['Eve', 'Carmen', 'Sarah', 'Lisa'])

# Display members of the baseball team (baseball set)
print('the following students are on the baseball team: ')
for name in baseball:
    print(name)

# Display members of the baseball team (baseball set)
print('the following students are on the basketball team: ')
for name in baseball:
    print(name)

# Demonstrate the intersection
print()
print('The following students play both baseball and basketball: ')
# Iterate through the result of this intersection
for name in baseball.intersection(basketball):
    print(name)
print()

# Display the union
print('The following students who play either sports: ')
for name in baseball.union(basketball):
    print(name)
print()

# Demonstrate the difference of basketball and baseball
print('The following students play basketball, but not baseball: ')
for name in basketball.difference(baseball):
    print(name)

# Demonstrate the symmetric
print('The following students play one sport, but not both')
for name in baseball.symmetric_difference(basketball):
    print(name)

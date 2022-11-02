# Get the two strings from the keyboard
# Create two blank dictionaries to hold the character occurence tallies
dict1= {}
dict2= {}
str1 = input('Enter the first word: '). lower()
str2 = input('Enter the second word: '). lower()
# For each character in the first string entered
for each_ch in str1:
    # If the character is a key in the dictionary then increment character tally by 1
    if each_ch in dict1:
        dict1[each_ch] = int(dict1[each_ch]) + 1
    # Else create a new key based on the character and set its value to 1
    else:
        dict1[each_ch] = 1
# For each character in teh second string entered
for each_ch in str2:
    # If the character is a key in the dictionary then increment character tally by 1
    if each_ch in dict2:
        dict2[each_ch] = int(dict2[each_ch]) + 1
    # Else create a new key based on the character and set its value to 1
    else:
        dict2[each_ch] = 1

# Compare the two dictionaries

# Optimised solution
def dict_tally(str):
    dict = {}
    for each_ch in str:
        if each_ch in dict:
            dict[each_ch] = int(dict[each_ch]) + 1
        else:
            dict[each_ch] = 1
    return dict

dict1 = dict_tally(input('Enter the first word: '). lower())
dict2 = dict_tally(input('Enter the second word: '). lower())
print(dict1 == dict2)
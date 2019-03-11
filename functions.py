# Make a function to determine if a number is odd or even

def odd_even(x):
    if x%2==0:
        return 'even'
    else:
        return 'odd'

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    new_list=[]
    for number in numbers:
        if number%2==0:
            new_list.append(number)
    return new_list

# Given a list return the unique names in the list

def unique_names(list_of_names):
    new_list=[]
    for name in list_of_names:
        if name!='john':
            new_list.append(name)
    return new_list

# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    """
    Input: string
    returns : True/False"""
    pass

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))

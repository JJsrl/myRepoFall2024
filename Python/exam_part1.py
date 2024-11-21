#   Josh Aresco


def not_string(str):
    """
    Given a string, return a new string where "not" has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string("cat") returns "notcat"
    not_string("not") returns not
    """
    if str == "not":
        return str
    new = "not"
    return new + str

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    minimum = min(lst)
    for i in range(len(lst)):
        if lst[i] == minimum:
            temp = lst[0]
            lst[0] = lst[i]
            lst[i] = temp
    
    return lst

    


def count_spaces(string):
    """
    Use comprehension to count the number of spaces in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_spaces("the cow jumped over the moon") returns 5
    Hint: your comprehension should return a new string (list of characters)
    with just spaces.
    """
    spaces = [x for x in string if x == " "]
    return len(spaces)


def build_heights_dict():
    '''
    Create a dictionary where the key is a person's name and the value is
    their height stored as an integer. 
    Read in the file, heights.txt, store the person's first name and 
    last name as the key (first and last name should have a space between them)
    and their height as the integer value.
    Your output should read:
     {'Thomas Jones': 70, 'Marcus Hansen': 68, 'Sarah Jenkins': 63, 
     'Abigail Ross': 65, 'Sebastian Adams': 70, 'Ella Rivera': 59, 
     'Luis Cruz': 71, 'Matt Patterson': 74, 'Jayden Cox': 67, 
     'Javier Alvaro': 69, 'Victoria Thompson': 62, 
     'Daniel Richardson': 68, 'Zoey Miller': 66}
    '''
    dictionary = dict()
    with open("heights.txt") as file:
        for line in file:
           fname,lname,height = line.split()
           full_name = fname + " " + lname
           dictionary[full_name] = int(height)
    return dictionary

print('not_string("cat") expected: notcat')
print('not_string("cat") actual:', not_string("cat"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print('count_spaces("the cow jumped over the moon") expected: 5')
print('count_spaces("the cow jumped over the moon") actual:', count_spaces("the cow jumped over the moon"))

print(build_heights_dict())

"""

run pytest for testing 

"""


def check_for_inserted_char(string1,string2):
    """ funtion to check inserted chars

        Find a score for each string and also the excess characters
        if a char from str1 is in str2 add 1 to the score

    """
    # here we check strip out the excess chars that aren't in string2
    # we create a new string if the chars are there.

    if len(string2) < len(string1):
        return False

    excess_char = 0
    new_str = ''
    for x in string2:
        if x in string1:
            if x not in new_str:
                new_str += x
        else:
            excess_char += 1
    # Now we stripped out the excess chars and we check if
    # the strings are equal. This will ensure that no chars are swapped here.
    # Then we check how many excess chars we have, if it's more than 1 return False
    stripped_string1 = ""
    for c in string1:
        if c not in stripped_string1:
            stripped_string1 += c
    if stripped_string1 == new_str and excess_char <= 1:
        return True
    return False


def check_for_replaced_char(string1, string2):
    """ function to check replaced char
    """
    string1,string2 = list(string1),list(string2)
    score = 0
    if len(string2) > len(string1):
        return False
    # add to score only if position of a char matches the same in string2
    for xpos,x in enumerate(string1):
        if x in string2 and xpos == string2.index(x):
            score += 1
    # generate a new stripped version of string1 to compare with score
    strip_string1 = ''
    for x in string1:
        if x not in strip_string1:
            strip_string1 += x
    # if score and new stripped string match the chars are replaced
    if score == len(strip_string1) or score == len(strip_string1) - 1:
        return True
    return False


def check_for_deleted_char(string1, string2):
    """ function to check deleted char

    example :
    str1 : joel
    str2 : joe

    after first loop
    string1 --- > new_str : joe
    missing_char_count : 1 --> l

    new_str is the stripped version of string1

    then comparison and conditional checking gives True.

    """
    # keeps track of the missing char
    missing_char_count = 0
    new_str = ''
    for x in string1:
        # checks if char from string1 is not in string2
        if x not in string2:
            # keeps track of the missing char
            missing_char_count += 1
        else:
            # if it's present, generates a new string excluding the missing chars
            new_str += x

    # using the check_for_inserted_char() to check for any inserted char
    # in the new string
    # using the insert() function to check if additional chars are there in the new string
    res = check_for_inserted_char(string2,new_str)
    # missing char count can be 1 or 0. More than 2
    if res and missing_char_count <= 1:
        return True
    return False



def check_for_swapped_char(string1,string2):
    """ function to check swapped char

    example:

    str1 : joel
    str2 : jeol

    j j  --> match    0
    o e  --> no match 1
    e o  --> no match 1
    l l  --> match    0

    Now since it's a single mutation, only one swap can take place.
    That's exchange of 2 chars, which leads to interchange in position.
    Now when the condition x!=y is run, the move satisfies since the
    corresponding char doesn't match the other.

    Here excess_char will always be 2 because of the interchange in its position
    if it's more than 2 there have been more swaps and 0 if there have been no swaps

    """
    excess_char = 0
    # loop through both strings
    for x,y in zip(string1,string2):
        # check if they don't match. If they don't that's the swapped char
        if x != y:
            excess_char += 1

    if excess_char == 2:
        return True
    return False


# passing refs of the function to avoid if conditions
functions = [check_for_inserted_char,check_for_replaced_char,check_for_deleted_char,check_for_swapped_char]


def nearly_eq(string1, string2):
    string1 = str(string1).lower()
    string2 = str(string2).lower()
    if string1 == string2:
        return True
    else:
        # loop through the functions
        for x in functions:
            # passes the strings through the functions one by one
            # if any of the function returns true the program ends and returns the result
            res = x(string1,string2)
            if res:
                return res
        return False

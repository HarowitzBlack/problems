

#  A mutation is defined as
# inserting a character [x]
# deleting a character  []
# replacing a character []
# or swapping 2 consecutive characters in a string []


def check_for_inserted_char(string1,string2):
    """ When they are sorted it's easier to figure out
        what's been inserted to a string.

        Find a score for each string and also the excess characters
        if a char from str1 is in str2 add 1 to the score

    """
    # So basically we are checking if all the char in string 1 are in string 2
    # and ignoreing the ones that aren't in it, that's how we find the score.
    # Now, the ignored charecters are the key
    # since these char are ignored we can find the additional chars that are inserted.
    score = 0
    excess_char = 0
    new_str = ''
    for x in string2:
        if x in string1:
            score += 1
            new_str += x
        else:
            excess_char += 1
    # Now we stripped out the excess chars and we check if
    # the strings are equal. This will ensure that no chars are swapped here.
    # Then we check how many excess chars we have, if it's more than 1 return False
    if string1 == new_str and excess_char <= 1:
        return True
    return False




def check_for_replaced_char(string1,string2):
    """ Same algo as above but here we take the score and
        discard the excess char(s)
    """
    string1,string2 = list(string1),list(string2)
    score = 0

    # only replaced chars
    if len(string2) > len(string1):
        return False

    # add to score only if position of a char matches the same in string2
    for xpos,x in enumerate(string1):
        if x in string2 and xpos == string2.index(x):
            score += 1
    if score == (len(string1)-1):
        # print(score,len(string1)-1)
        return True
    return False


#print(check_for_replaced_char("bool","cool"))

def check_for_deleted_char(str1,str2):
    pass

# we want the strings to go through all of the above functions to check if
# they are mutable or not. Since it'll be really messy to use if-elif-else
# we put the refs of the functions in a list. Then call them by looping through
# them. If anyone of the function returns True, it breaks the loop, if it returns
# false it continues and calls the rest of the functions.
functions = [check_for_inserted_char,check_for_replaced_char]

# works for all single mutations
def nearly_eq(string1, string2):
    string1 = str(string1).lower()
    string2 = str(string2).lower()
    if string1 == string2:
        return True
    else:
        for x in functions:
            res = x(string1,string2)
            print("DEBUG:",res,x)
            if res:
                return res
        return False


nq = nearly_eq("python","pythano")
print(nq)

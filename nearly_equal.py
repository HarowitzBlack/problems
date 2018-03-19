

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
    for x in string1:
        if x in string2:
            score += 1
    # finding the excess charecters
    excess_char_count = len(string2) - score
    # checking if additional char have been added and also checking if the score
    # is equal to the len of first string
    if excess_char_count <= 1 and score == len(string1):
        return True
    return False

def check_for_replaced_char(string1,string2):
    """ Same algo as above but here we take the score and
        discard the excess char(s)
    """
    string1,string2 = list(string1),list(string2)
    score = 0
    for x in string1:
        if x in string2:
            score += 1
    if score == (len(string1)-1):
        return True
    return False


#print(check_for_replaced_char("bool","cool"))

def check_for_deleted_char(str1,str2):
    pass


def check_for_swapped_char(str1,str2):
    pass


# works for all single mutations
def nearly_eq(string1, string2):
    string1 = str(string1).lower()
    string2 = str(string2).lower()
    if string1 == string2:
        return True
    else:

        res = check_for_inserted_char(string1,string2)
        return res


#nq = nearly_eq("perl","cerl")
#print(nq)

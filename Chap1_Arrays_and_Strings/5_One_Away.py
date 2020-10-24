# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one-edit (or zero-edits) away. 

# This literally took so long Jackie you best not forget it
def check_insert_removal(str1, str2):
    """ str1 is smaller than str2. Loops through str1 and see if the corresponding index in str2 matches. If not, check the next index. If that still doesn't match, return False because you can only have one insertion. 
    """
    if abs(len(str1)-len(str2))>1:
        return False
    i=0
    j=0
    while i < len(str1):
        if str1[i] != str2[i] and str1[i] != str2[i+1]:
            return False
        elif str1[i] != str2[i] and str1[i] == str2[i+1]:
            j = j+1
        i += 1
        j += 1
    return True

def check_replace(str1, str2):
    """ These strings should be of the same length. The function loops compares the letter at corresponding indices of str1 and str2. If it finds more than one differences, they must be more than one edit away.
    """
    foundDiff = False
    for i, char in enumerate(str1):
        if char != str2[i]:
            if foundDiff == True:
                return False
            else:
                foundDiff = True
    return True

def is_One_Away(str1, str2):
    """ Decides on what function to use based on str lengths.
    """
    if len(str1) == len(str2):
        return check_replace(str1, str2)
    elif len(str2) > len(str1):
        return check_insert_removal(str1, str2)
    else:
        return check_insert_removal(str2, str1)


if __name__ == "__main__":
    str1 = "pale"
    str2 = "pales`"
    result = is_One_Away(str1, str2)
    print(result)
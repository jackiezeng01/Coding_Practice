# Given two strings, write a method to decide if one is a permuation of the other

# CLARIFICATIONS: Is this case sensitive? and does white space matter?
# O(n)
def Check_Permutation(str1, str2):
    # If not the same length, they can't be permuations
    if len(str1) != len(str2):
        return False
    str1_dict = {}
    str2_dict = {}

    # Goes through each string and puts characters in dictionary. 
    for char in str1:
        if char in str1_dict:
            str1_dict[char] = str1_dict[char]+1
        else:
            str1_dict[char] = 0
    
    for char in str2:
        if char in str2_dict:
            str2_dict[char] = str2_dict[char]+1
        else:
            str2_dict[char] = 0

    if (str1_dict == str2_dict):
        return True
    return False


# O(nlogn)
def Check_Permutation_Sort(str1, str2):
    # Check length of strings
    if len(str1) != len(str2):
        return False
    # Convert string to array and sort the arrays
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()
    l2.sort()
    # sorts : O(nlogn) , sorts in place. To return a sorted list, use "sorted"
    print(l1, l2)
    if l1 == l2:
        return True
    return False


if __name__ == "__main__":
    str1 = "abcd"
    str2 = "abdc"
    # isPerm = Check_Permutation(str1, str2)
    isPerm = Check_Permutation_Sort(str1, str2)

    print(isPerm)

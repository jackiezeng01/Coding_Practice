# Given a string, write a function to check if it is a permuation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permuation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

# Clarifications: Is the palindrome case sensitive? Does white space count as a letter?

# O(n)
def is_Palindrome_Permutation(str):
    str = str.lower()
    char_dict = {}
    odd_counter = 0
    # Put string values in hashmap
    for char in str:
        # Checks to see if character is a letter
        if char.isalpha():
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
            else: 
                char_dict[char] = 1

    # If more than one value is odd, it can't be a palindrome
    for char in char_dict:
        if char_dict[char]%2 != 0:
            odd_counter += 1

    if odd_counter > 1:
        return False
    return True    

if __name__ == "__main__":
    str = "Tact Coa"
    output = is_Palindrome_Permutation(str)
    print(output)
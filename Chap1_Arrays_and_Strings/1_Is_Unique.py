# Implement an algorithm to determine if a string has all unique characters, What if you cannot use additional data structures?

def Is_Unique(str):
    # There are standard 128 ASCII characters and 256 extended ASCII characters
    if (len(str)> 128):
        return False
    # Initializes array to track all count of characters. Set all to 0 at first
    char_array = []

    for i in range(len(str)):
        
        if str[i] in char_array:
            return False
        else:
            char_array.append(str[i])

    return True

# Time Complexity: O(N)

if __name__ == "__main__":
    print(Is_Unique("abcdes"))

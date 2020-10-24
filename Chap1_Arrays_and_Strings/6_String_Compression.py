# Implement a method to perform basic string compression using the counts of repeated characters. For instance, the string aabccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string. You can assume the string only has uppercase and lowercase letters(a-z)

# String concatenation: O(n^2)
# Time Complexity: 
# My solution is really slow
def String_Compression(str1):
    i = 0
    compstr = ""
    while i < len(str1):
        char = str1[i]
        if i+1==len(str1) or char != str1[i+1]:
            compstr = compstr + char + str(1)
        else:
            j = i
            counter = 0
            while j<len(str1):
                if str1[j] != str1[i]:
                    break
                else:
                    counter = counter + 1
                    j += 1
            compstr = compstr + char + str(counter)
            print(compstr)
            i = i + counter - 1
        i += 1
    if len(compstr) >= len(str1):
        return str1
    return compstr

def String_Compression_Optim(str1):
    ''' Loops through each character and uses a "Stringbuilder" to make string. 
    Stringbuilder makes an array and then joins them at the end. This is a lot faster than concatenation
    '''
    compstr = []
    # counter for consecutive letters
    count = 0
    for i, char in enumerate(str1):
        count += 1
        # If next letter is not the same as current letter, add current character to array(Ex: a3) and set count to 0 again for the next letter. 
        if i+1 >= len(str1) or char != str1[i+1]:
            compstr.append(char)
            compstr.append(str(count))
            count = 0
    compstr = ''.join(compstr)
    if len(compstr) >= len(str1):
        return str1
    return compstr


if __name__ == "__main__":
    string = "aabccccaaa"
    output = String_Compression_Optim(string)
    print("Output:", output)

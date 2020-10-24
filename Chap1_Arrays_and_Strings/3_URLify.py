# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficuient space at the end to hold the additional characters, and that you are gven the "true" length of the string.

def URLify(str, strlen):
    output = ""
    for i,char in enumerate(str):
        if char == " " and i<strlen:
            output = output + "%20"
        else:
            output = output + char
    return output


if __name__ == "__main__":
    test_str = "Mr John Smith    "
    # Actual length without extra spaces at the end
    test_int = 13
    url = URLify(test_str, test_int)
    print(url)
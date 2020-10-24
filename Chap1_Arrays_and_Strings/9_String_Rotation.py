""" ASume you have a emthod isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring. 
"""
def isSubstring(s1, s2):
    pass

def String_Rotation(s1, s2):
    # If dif lengths, they can't be rotation. Also shouldn't be empty    
    if len(s1) != len(s2) and len(s1)>0:
        return False
    for i in range(len(s1)):
        x = s1[0:i]
        y = s1[i:]
        # xy = x+y #Should be x
        yx = y+x
        if yx==s2:
            return True
    return False

# Method that uses less space by only concatenating once:
def String_Rotation_Substring(s1, s2):
    if len(s1) != len(s2) and len(s1)>0:
        return False
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    output = String_Rotation(s1, s2)
    print(output)

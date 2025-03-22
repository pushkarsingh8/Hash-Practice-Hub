#Find First Non-Repeating Character in Given String:-

def find_non_repeat(strr):
    hs_mp = {}

    for char in strr:

        if char not in hs_mp:
            hs_mp[char] = 1


        else:
            hs_mp[char]  += 1


    for char in strr:
        if hs_mp[char] == 1:

            return char
        

    return "$"
            



string = "geeksforgeeks"

print(find_non_repeat(string))


def find_freq(strr):

    hs = {}

    for char in strr:
        if char not in hs:

            hs[char] = 1

        else:
            hs[char] += 1

    print(hs)




data = "geeksforgeeks"

find_freq(data) 
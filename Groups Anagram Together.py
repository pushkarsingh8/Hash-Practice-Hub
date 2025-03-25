#Groups Anagram Together:-



def Find_groupAnagram(arr):

    frequency = {}

    data = []

    for word in arr:

        sorted_word = "".join(sorted(word))


        if sorted_word not in frequency:

            frequency[sorted_word] = []



        frequency[sorted_word].append(word)



    data = (frequency.values())


    print(data)





arr = ["act", "god", "cat" , "dog" , "tac" ]

Find_groupAnagram(arr)
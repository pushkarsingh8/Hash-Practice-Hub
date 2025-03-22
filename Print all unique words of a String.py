#Print all unique words of a String:

def printUnique(string):
    
    l = []
    dict = {}

    for word in string.split():

        if word not in dict:
            dict[word] = 1
        
        else:
            dict[word] += 1

            
    for key,value in dict.items():

        if value == 1:
            l.append(key)


    return l
            



string = "Java is great Grails is also great"

print(printUnique(string))
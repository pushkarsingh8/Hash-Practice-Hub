#Majority Element:-

def Find_Majority_Element(arr):

    n = len(arr)

    dict = {}

    for x in arr:

        if x not in dict:

            dict[x] = 1


        else:


            dict[x] += 1


    
    for num,value in dict.items():

        if value > n//2:

            print("Majority Element: ",num)
            break

        else:
            
            print(-1)



arr = [3]

Find_Majority_Element(arr)







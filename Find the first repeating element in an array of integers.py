#Find the first repeating element in an array of integers:-

#Approacher using Two loops Time Complexity O(n) O(1)

def find_first_repeat(arr):

    dict = {}


    for num in arr:

        if num  in arr:

            print("Repeating Number:",num)
            break

        else:

            dict[num] = 1
            
            

    
   

arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]

find_first_repeat(arr)


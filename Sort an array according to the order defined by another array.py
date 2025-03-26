#Sort an array according to the order defined by another array:-


def sort_arr1(arr1,arr2):

    sorted_data = []

    temp = []
    
    i = 0
    while i < len(arr2):
        
        for num in arr1:

            if arr2[i] == num:

                sorted_data.append(num)

        i+=1

    
    
    for num in arr1:

        if num not in arr2:

            temp.append(num)

    temp = sorted(temp)

    for num in temp:
        sorted_data.append(num)


    return sorted_data



    
    



a = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]

b = [2,1,8,3] 

print(sort_arr1(a,b))






    
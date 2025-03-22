#Find a Missing Element of a Range:-

def missing_number(low,high,arr1):

    for x in range(low,high+1):
        if x not in arr1:
            print(x,end=" ")



    

low = 50
high = 55
arr = [1, 14, 11, 51, 15]

missing_number(low,high,arr)


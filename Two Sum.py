#Two sum Pair with Given Sum:-

#1. using two loops:

def Two_sum(arr,target):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            if arr[i] + arr[j] == target:
                print(arr[i],arr[j])

                return True
            

    return False

arr = [1, -2, 1, 0, 5]

t = 0

print(Two_sum(arr,t))


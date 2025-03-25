#Subarray with given Sum:-

def Subarrywith_sum(arr,target):

    c_sum = 0
    left = 0




    for right in range(len(arr)):

        c_sum += arr[right]



        while c_sum > target and left <= right:

            c_sum -= arr[left]

            left += 1


        if c_sum == target:
            
            print(f"subarray found between inidices {left+1} and {right+1}")
            return
        
        




    print(-1)

arr = [15, 2, 4, 8, 9, 5, 10, 23]

target = 23

Subarrywith_sum(arr,target)

        

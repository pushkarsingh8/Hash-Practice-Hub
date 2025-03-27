#find the Longest Subarray with 0 Sum:-

def longest_subarray(arr):

    max_len = 0
    curr_len = 0


    for i in range(len(arr)):

        sum  = 0

        for j in range(i,len(arr)):

            sum += arr[j]


            if sum == 0:

                curr_len = j - i + 1

                max_len = max(curr_len,max_len)




    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]

print(longest_subarray(arr))
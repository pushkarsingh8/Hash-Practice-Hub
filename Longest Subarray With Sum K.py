#Longest Subarray with sum k:-


def find_longest_subarray_withK(arr,k):

    res = 0

    for i in range(len(arr)):

        sum = 0

        for j in range(i,len(arr)):

            sum += j

            if sum == k:

                sublen = j - i + 1 
                res = max(res,sublen)



    return res



arr = [10, 5, 2, 7, 1, -10]

k = 15


print(find_longest_subarray_withK(arr,k))






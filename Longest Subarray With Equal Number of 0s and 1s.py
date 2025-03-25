#Longest Subarray with Equal Number 0s and 1s:-

def find_longest_subarr(arr):

    frq = {}

    max_len = 0
    sum = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            sum += -1

        else:
            sum += 1


        if sum == 0:
            max_len = i + 1


        if sum in frq:

            max_len = max(max_len,i - frq[sum])


        else:

            frq[sum] = i


    return max_len

arr = [1, 0, 1, 1, 1, 0, 0]

print(find_longest_subarr(arr))
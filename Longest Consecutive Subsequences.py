#Longest Consecutive Subsequence:-

def long_consecutive_subs(arr):

    num_set = set(arr)


    longest_streak = 0


    for num in num_set:

        if num - 1 not in num_set:

            current_num = num

            current_streak = 1


            while current_num + 1 in num_set:
                current_num+=1
                current_streak+=1


            longest_streak = max(current_streak,longest_streak)


    return longest_streak




arr = [2, 6, 1, 9, 4, 5, 3]

print(long_consecutive_subs(arr))
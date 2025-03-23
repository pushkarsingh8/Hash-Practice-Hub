#2 Sum – All distinct pairs with given sum

def Two_sum_pair(arr,target):

    seen_pairs = set()

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if arr[i] + arr[j] == target:

                pairs  = tuple(sorted((arr[i],arr[j])))

                seen_pairs.add(pairs)


                




    for pairs in seen_pairs:

        print(pairs,end=" ")




arr = [1, 5, 7, -1, 5]

target = 6

Two_sum_pair(arr,target)
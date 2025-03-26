#Print all the array with 0 Sum:-

def printallarr(arr):
    prefix_sum = 0

    has_map = {}

    for i in range(len(arr)):

        prefix_sum += arr[i]


        if prefix_sum == 0:
            print("Subarray found from Index 0 to ",i)





        if prefix_sum in has_map:

            for start_index in has_map[prefix_sum]:

                print(f"Subarray found from Index {start_index+1} to {i} ")

            has_map[prefix_sum].append(i)


        else:

            has_map[prefix_sum] = [i]
            







        




arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]


printallarr(arr)
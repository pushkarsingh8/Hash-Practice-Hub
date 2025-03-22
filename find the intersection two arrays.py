#Union and Intersection of Two Unsorted Arrays:-


def find_Union(arr1,arr2):
    union = []

    m = len(arr1)
    n = len(arr2)

    for i in range(m):
        if arr1[i] not in union:
            union.append(arr1[i])



    for j in range(n):

        if arr2[j] not in union:
            union.append(arr2[j])



    return union



def find_intersection(a,b):

    intersection = []

    for num in a:
        if num in b and num not in intersection:
            intersection.append(num)


    
    return intersection



arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]


data_union = find_Union(arr1,arr2) #Expected Union


data_ins = find_intersection(arr1,arr2) #Expected Intersection

print("Union: ",data_union)

print("Intersection: ",data_ins)





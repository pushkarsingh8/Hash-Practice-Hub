#Count a distinct number in a array:-

def count_distinct(arr):
    count = 0
    unique_el = []

    for num in arr:
        if num not in unique_el:
            unique_el.append(num)

    return len(unique_el)


arr = [10, 20, 20, 10, 30, 10]

print(count_distinct(arr))

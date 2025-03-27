def minRange(arr, k):
    n = len(arr)
    freq = {}
    l = 0
    min_len = float('inf')
    start, end = -1, -1
    unique_Count = 0

    for r in range(n):
        if arr[r] in freq:
            freq[arr[r]] += 1
        else:
            freq[arr[r]] = 1
            unique_Count += 1

        while unique_Count == k:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                start, end = l, r

            freq[arr[l]] -= 1
            if freq[arr[l]] == 0:
                del freq[arr[l]]
                unique_Count -= 1
            l += 1

    return (start, end) if start != -1 else -1

# Example
arr = [1, 2, 3, 4, 5]
k = 3
print(minRange(arr, k))  # Output: (0, 2)

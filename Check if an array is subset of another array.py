#check if an array is subset of another array:-

def arr(a,b):
    
    m = len(a)
    n = len(b)

    found = False

    for i in range(m):
        
        for j in range(n):
            
            if b[j] == a[i]:
                
                found = True
                break  

        if not found:
            return False
        

        

    return True


arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]

print(arr(arr1,arr2))
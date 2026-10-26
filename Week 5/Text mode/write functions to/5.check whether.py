def is_increasing(arr):
    i = 0
    while i < len(arr) - 1:  
        if arr[i] > arr[i + 1]:
            return False  
        i += 1
    return True

print("ชุด [1, 3, 5, 8]:", is_increasing([1, 3, 5, 8]))  # True
print("ชุด [1, 5, 3, 8]:", is_increasing([1, 5, 3, 8]))  # False
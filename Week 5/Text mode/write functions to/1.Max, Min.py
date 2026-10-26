def find_max_min_index(arr):
    max_idx = 0
    min_idx = 0
    i = 1
    
    while i < len(arr):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i
        i += 1
        
    return max_idx, min_idx

data = [12, 45, 7, 23, 89, 34]
max_i, min_i = find_max_min_index(data)
print(f"Max Index: {max_i}, Min Index: {min_i}")
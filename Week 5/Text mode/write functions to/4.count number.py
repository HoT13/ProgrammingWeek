def count_higher_than_avg(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    avg = total / len(arr)
   
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] > avg:
            count += 1
        i += 1
        
    return count

data = [10, 20, 30, 40, 50] 
print("จำนวนตัวที่มากกว่าค่าเฉลี่ย:", count_higher_than_avg(data))
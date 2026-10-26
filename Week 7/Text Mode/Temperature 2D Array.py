# ข้อมูลอุณหภูมิ 4 สัปดาห์ (4 แถว) สัปดาห์ละ 7 วัน (7 คอลัมน์)
temperatures = [
    [30, 32, 31, 29, 28, 30, 33],  # Week 0
    [34, 35, 33, 32, 31, 30, 29],  # Week 1
    [27, 26, 28, 29, 30, 31, 32],  # Week 2
    [31, 33, 34, 35, 36, 30, 29]   # Week 3
]

# ฟังก์ชันคำนวณค่าเฉลี่ยของสัปดาห์ที่เลือก
def week_average(temp_data, w):
    return sum(temp_data[w]) / len(temp_data[w])

# ฟังก์ชันหาค่าสูงสุดของสัปดาห์ที่เลือก
def week_max(temp_data, w):
    return max(temp_data[w])

# ฟังก์ชันหาค่าต่ำสุดของสัปดาห์ที่เลือก
def week_min(temp_data, w):
    return min(temp_data[w])

# ฟังก์ชันหาค่าสูงสุดรวมทั้งหมด โดยเรียกใช้ week_max()
def overall_max(temp_data):
    max_values = [week_max(temp_data, w) for w in range(len(temp_data))]
    return max(max_values)

# ฟังก์ชันหาค่าต่ำสุดรวมทั้งหมด โดยเรียกใช้ week_min()
def overall_min(temp_data):
    min_values = [week_min(temp_data, w) for w in range(len(temp_data))]
    return min(min_values)

# --- ทดสอบการใช้งาน ---
target_week = 0  # สัปดาห์แรก (w = 0)
print(f"Week {target_week} Average: {week_average(temperatures, target_week):.2f}°C")
print(f"Week {target_week} Max: {week_max(temperatures, target_week)}°C")
print(f"Week {target_week} Min: {week_min(temperatures, target_week)}°C")
print("---")
print(f"Overall Max Temperature: {overall_max(temperatures)}°C")
print(f"Overall Min Temperature: {overall_min(temperatures)}°C")
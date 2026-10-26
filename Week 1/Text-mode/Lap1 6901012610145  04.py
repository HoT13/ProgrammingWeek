width = float(input("ป้อนความกว้างของที่ดิน (เมตร): "))
length = float(input("ป้อนความยาวของที่ดิน (เมตร): "))

sq_meters = width * length

tarang_wah = sq_meters / 4

print("\n--- ผลการคำนวณพื้นที่ดิน ---")
print(f"พื้นที่ดิน: {sq_meters:.2f} ตารางเมตร")
print(f"พื้นที่ดิน: {tarang_wah:.2f} ตารางวา")
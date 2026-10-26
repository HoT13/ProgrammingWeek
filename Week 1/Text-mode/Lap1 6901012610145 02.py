weight = float(input("ป้อนน้ำหนักตัว (กิโลกรัม): "))
height_cm = float(input("ป้อนส่วนสูง (เซนติเมตร): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("\n--- ผลการคำนวณ BMI ---")
print(f"ดัชนีมวลกาย (BMI) ของคุณคือ: {bmi:.2f}")
import math
2
diameter = float(input("ป้อนความยาวเส้นผ่านศูนย์กลางของวงกลม (เซนติเมตร): "))

radius = diameter / 2

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print("\n--- ผลการคำนวณวงกลม ---")
print(f"ความยาวรัศมี: {radius:.2f} ซม.")
print(f"เส้นรอบวง: {circumference:.2f} ซม.")
print(f"พื้นที่วงกลม: {area:.2f} ตร.ซม.")
distance = float(input("กรุณาใส่ระยะทาง (กิโลเมตร): "))

fuel_efficiency = 12.5   # รถกินน้ำมัน กิโลเมตรต่อลิตร
price_per_liter = 42.5   # ราคาน้ำมันต่อลิตร (บาท)

# คำนวณ
fuel_needed = distance / fuel_efficiency      # ลิตร
total_cost = fuel_needed * price_per_liter    # บาท

# แสดงผล
print("\n=== ผลการคำนวณค่าน้ำมัน ===")
print(f"ระยะทาง          : {distance:,.2f} กิโลเมตร")
print(f"น้ำมันที่ใช้      : {fuel_needed:,.3f} ลิตร")
print(f"ราคาน้ำมันทั้งหมด : {total_cost:,.2f} บาท")
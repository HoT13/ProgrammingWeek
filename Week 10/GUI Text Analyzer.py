import tkinter as tk
from tkinter import messagebox

def text_analyzer_app():
    root = tk.Tk()
    root.title("GUI Text Analyzer")
    root.geometry("450x360")
    root.resizable(False, False)
    
    def count_char():
        text = entry_text.get()
        char = entry_char.get()
        if not char:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกตัวอักษรที่ต้องการค้นหา")
            return
        count = text.count(char)
        lbl_result.config(text=f"ตัวอักษร '{char}' ปรากฏทั้งหมด {count} ครั้ง")
        
    def count_vowels():
        text = entry_text.get()
        vowels = "aeiouAEIOU"
        count = sum(1 for char in text if char in vowels)
        lbl_result.config(text=f"จำนวนสระทั้งหมด (a, e, i, o, u): {count} ตัว")
        
    def check_palindrome():
        # ตัดช่องว่างออกและแปลงเป็นตัวพิมพ์เล็กเพื่อให้ตรวจสอบแม่นยำขึ้น
        text = entry_text.get().replace(" ", "").lower()
        if not text:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อความก่อนตรวจสอบ Palindrome")
            return
        
        is_palindrome = text == text[::-1]
        if is_palindrome:
            lbl_result.config(text="ผลลัพธ์: เป็น Palindrome ✅", fg="#27ae60")
        else:
            lbl_result.config(text="ผลลัพธ์: ไม่เป็น Palindrome ❌", fg="#e74c3c")
            
    # UI Components
    tk.Label(root, text="GUI Text Analyzer", font=("Arial", 14, "bold")).pack(pady=15)
    
    # ช่องรับข้อความหลัก
    f1 = tk.Frame(root)
    f1.pack(pady=5)
    tk.Label(f1, text="ข้อความ (Text):", width=15, anchor="w", font=("Arial", 10)).pack(side=tk.LEFT)
    entry_text = tk.Entry(f1, font=("Arial", 10), width=22)
    entry_text.pack(side=tk.LEFT)
    
    # ช่องรับตัวอักษรค้นหา
    f2 = tk.Frame(root)
    f2.pack(pady=5)
    tk.Label(f2, text="ตัวอักษรค้นหา:", width=15, anchor="w", font=("Arial", 10)).pack(side=tk.LEFT)
    entry_char = tk.Entry(f2, font=("Arial", 10), width=8)
    entry_char.pack(side=tk.LEFT)
    
    # ปุ่มกดฟังก์ชันต่างๆ
    f3 = tk.Frame(root)
    f3.pack(pady=15)
    tk.Button(f3, text="Count Character", bg="#2980b9", fg="white", font=("Arial", 9, "bold"), command=count_char).grid(row=0, column=0, padx=4)
    tk.Button(f3, text="Count Vowels", bg="#27ae60", fg="white", font=("Arial", 9, "bold"), command=count_vowels).grid(row=0, column=1, padx=4)
    tk.Button(f3, text="Check Palindrome", bg="#8e44ad", fg="white", font=("Arial", 9, "bold"), command=check_palindrome).grid(row=0, column=2, padx=4)
    
    # ส่วนแสดงผลลัพธ์
    lbl_result = tk.Label(root, text="ผลลัพธ์การวิเคราะห์จะแสดงที่นี่", font=("Arial", 11, "bold"), fg="#2c3e50")
    lbl_result.pack(pady=15)
    
    root.mainloop()

if __name__ == "__main__":
    text_analyzer_app()
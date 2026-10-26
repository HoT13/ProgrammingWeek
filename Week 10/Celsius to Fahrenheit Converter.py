import tkinter as tk
from tkinter import messagebox

def temp_converter_app():
    root = tk.Tk()
    root.title("Celsius to Fahrenheit Converter")
    root.geometry("350x240")
    root.resizable(False, False)
    
    def convert():
        try:
            # แปลงค่าที่กรอกเป็น float เพื่อเช็คว่าเป็นตัวเลขจริงไหม
            celsius = float(entry_c.get())
            fahrenheit = (celsius * 9/5) + 32
            lbl_result.config(text=f"ผลลัพธ์: {fahrenheit:.2f} °F", fg="#27ae60")
        except ValueError:
            # แจ้งเตือนเมื่อกรอกไม่ใช่ตัวเลข
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!")
            entry_c.delete(0, tk.END)
    
    # UI Components
    tk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold")).pack(pady=15)
    
    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)
    
    tk.Label(frame_input, text="Celsius (°C):", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    entry_c = tk.Entry(frame_input, font=("Arial", 11), width=12)
    entry_c.pack(side=tk.LEFT, padx=5)
    
    btn_conv = tk.Button(root, text="Convert", width=12, bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=convert)
    btn_conv.pack(pady=10)
    
    lbl_result = tk.Label(root, text="ผลลัพธ์: -", font=("Arial", 12, "bold"), fg="#2c3e50")
    lbl_result.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    temp_converter_app()
import tkinter as tk

def counter_app():
    root = tk.Tk()
    root.title("Counter App")
    root.geometry("320x220")
    root.resizable(False, False)
    
    # ตัวแปรเก็บค่าตัวเลข
    count = 0
    
    def increase():
        nonlocal count
        count += 1
        lbl_count.config(text=str(count))
        
    def decrease():
        nonlocal count
        count -= 1
        lbl_count.config(text=str(count))
        
    def reset():
        nonlocal count
        count = 0
        lbl_count.config(text=str(count))
        
    # UI Components
    tk.Label(root, text="Counter Application", font=("Arial", 14, "bold")).pack(pady=15)
    
    lbl_count = tk.Label(root, text="0", font=("Arial", 30, "bold"), fg="#2c3e50")
    lbl_count.pack(pady=5)
    
    frame_btns = tk.Frame(root)
    frame_btns.pack(pady=15)
    
    btn_dec = tk.Button(frame_btns, text="Decrease", width=8, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=decrease)
    btn_dec.grid(row=0, column=0, padx=5)
    
    btn_res = tk.Button(frame_btns, text="Reset", width=8, bg="#95a5a6", fg="white", font=("Arial", 10, "bold"), command=reset)
    btn_res.grid(row=0, column=1, padx=5)
    
    btn_inc = tk.Button(frame_btns, text="Increase", width=8, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=increase)
    btn_inc.grid(row=0, column=2, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    counter_app()
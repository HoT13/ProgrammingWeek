class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = int(age) # แปลงอายุเป็น int เพื่อใช้เปรียบเทียบ

    def show(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Age: {self.age}")

def find_youngest_student(student_array):
    if not student_array:
        print("No student data.")
        return
    
    # หาค่าอายุน้อยที่สุด
    youngest = student_array[0]
    for student in student_array:
        if student.age < youngest.age:
            youngest = student
            
    print("--- Youngest Student ---")
    youngest.show()

# ส่วนหลักของโปรแกรม
students_list = []
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 4:
                # สร้าง Object และเก็บลง List (Array)
                student_obj = Student(data[0], data[1], data[2], data[3])
                students_list.append(student_obj)

    find_youngest_student(students_list)
except FileNotFoundError:
    print("Error: Please create 'students.txt' first.")
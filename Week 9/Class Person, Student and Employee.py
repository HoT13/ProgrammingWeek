class Person:
    def __init__(self, name, address, weight_kg, height_cm):
        self.name = name
        self.address = address
        self.weight = weight_kg
        self.height = height_cm

    def getBMI(self):
        # BMI = weight(kg) / height(m)^2
        height_m = self.height / 100
        return self.weight / (height_m ** 2)

    def show(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Weight: {self.weight} kg, Height: {self.height} cm")

# Subclass: Student
class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        # Call superclass constructor
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        print("--- Student Info ---")
        super().show()  # Call show() from Person
        print(f"Student ID: {self.student_id}, Course: {self.course}, GPA: {self.gpa}")
        print(f"BMI: {super().getBMI():.2f}")  # Call getBMI() from Person

# Subclass: Employee
class Employee(Person):
    def __init__(self, name, address, weight, height, emp_id, department, salary):
        super().__init__(name, address, weight, height)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def show(self):
        print("--- Employee Info ---")
        super().show()
        print(f"Employee ID: {self.emp_id}, Dept: {self.department}, Salary: {self.salary:,.2f}")
        print(f"BMI: {self.getBMI():.2f}") # Can use self.getBMI() directly since it's inherited

# --- ทดสอบการทำงาน ---
s1 = Student("Alice", "Bangkok", 55, 160, "S001", "Computer Science", 3.8)
s1.show()

e1 = Employee("Bob", "Nonthaburi", 75, 175, "E999", "IT Support", 35000)
e1.show()
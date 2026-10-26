class Matrix:
    def __init__(self, data):
        # data คือ 2D List
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def show(self):
        for row in self.data:
            print(row)
        print()

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return "Cannot add: Dimensions do not match."
        result = [[self.data[r][c] + other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return "Cannot subtract: Dimensions do not match."
        result = [[self.data[r][c] - other.data[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(result)

    def multiplication(self, other):
        if self.cols != other.rows:
            return "Cannot multiply: Matrix 1 columns must equal Matrix 2 rows."
        # การคูณเมทริกซ์
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*other.data)] for X_row in self.data]
        return Matrix(result)

# --- ทดสอบการทำงาน ---
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
m1.show()
print("Matrix 2:")
m2.show()

print("Addition:")
m1.add(m2).show()

print("Subtraction:")
m1.subtract(m2).show()

print("Multiplication:")
m1.multiplication(m2).show()
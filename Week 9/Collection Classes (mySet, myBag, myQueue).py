class myBag:
    def __init__(self):
        self.items = [] # Allow duplicates

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def show(self):
        print(f"Bag contents: {self.items}")

class mySet:
    def __init__(self):
        self.items = [] # No duplicates

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def show(self):
        print(f"Set contents: {self.items}")

class myQueue:
    def __init__(self):
        self.items = [] # First In, First Out (FIFO)

    def add(self, item):
        self.items.append(item) # Add to the end

    def remove(self):
        if len(self.items) > 0:
            removed_item = self.items.pop(0) # Remove from the front
            return removed_item
        print("Queue is empty!")
        return None

    def show(self):
        print(f"Queue contents (front to back): {self.items}")

# --- ทดสอบการทำงาน ---
s = mySet()
s.add(1)
s.add(2)
s.add(1) # จะไม่เข้าไปซ้ำ
s.show() # [1, 2]

q = myQueue()
q.add("Alice")
q.add("Bob")
q.remove() # Alice จะถูกลบออกก่อน
q.show() # ['Bob']
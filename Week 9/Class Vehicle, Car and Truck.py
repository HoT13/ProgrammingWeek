class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        print(f"[{self.license_plate}] {self.year} {self.brand} {self.model} | Rate: {self.daily_rate}/day")

    def calculate_rental_cost(self, days):
        # Base calculation
        return self.daily_rate * days

# Subclass: Car
class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        print("--- Car Info ---")
        super().show_info()
        print(f"Seats: {self.seats}")

    def calculate_rental_cost(self, days):
        # Promotion logic: Every 7 days, you pay for 5 days.
        cycles = days // 7
        remainder = days % 7
        
        # If remainder is 5 or 6 days, you only pay for 5 days
        payable_remainder = min(remainder, 5)
        
        payable_days = (cycles * 5) + payable_remainder
        total_cost = payable_days * self.daily_rate
        return total_cost

# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        print("--- Truck Info ---")
        super().show_info()
        print(f"Payload: {self.payload} tons")
    
    # Truck uses the default calculate_rental_cost from Vehicle (no promotion)

# --- ทดสอบการทำงาน ---
my_car = Car("AB-1234", "Toyota", "Camry", 2022, 1000, 5)
my_car.show_info()
print(f"Rent for 7 days (Car): {my_car.calculate_rental_cost(7):,} Baht") # Should be 5000

my_truck = Truck("XY-9999", "Isuzu", "D-Max", 2020, 1500, 2.5)
my_truck.show_info()
print(f"Rent for 7 days (Truck): {my_truck.calculate_rental_cost(7):,} Baht") # Should be 10500
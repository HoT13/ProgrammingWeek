import os

class Product:
    def __init__(self, name, price, quantity):
        # Initialize product attributes and convert data types
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def show(self):
        # Display product details
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

def show_max_quantity_value(product_array):
    if not product_array:
        print("Array is empty.")
        return

    # Assume the first product has the max quantity initially
    max_qty_product = product_array[0]
    
    # Iterate to find the product with the highest quantity
    for p in product_array:
        if p.quantity > max_qty_product.quantity:
            max_qty_product = p
            
    # Calculate the total value (Price x Quantity)
    total_value = max_qty_product.price * max_qty_product.quantity
    
    print("--- Product with Maximum Quantity ---")
    max_qty_product.show()
    print(f"Total Value (Price x Quantity): {total_value:,.2f}")

# Main execution
products_list = []

# Get the exact directory where this python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Join it with the filename to get the absolute path
file_path = os.path.join(current_dir, "products.txt")

try:
    # Open the file using the absolute path
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Remove whitespace and split by comma
            data = line.strip().split(',')
            
            # Ensure the line has exactly 3 elements before processing
            if len(data) == 3:
                # Instantiate Product and append to list
                prod_obj = Product(data[0], data[1], data[2])
                products_list.append(prod_obj)

    # Call the function to find and display the max quantity product
    show_max_quantity_value(products_list)

except FileNotFoundError:
    print(f"Error: Could not find file at '{file_path}'")
    print("Please check if 'products.txt' exists in the same folder.")
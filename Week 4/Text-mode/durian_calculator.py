def durian_calculator():
    count = 0
    total_weight = 0
    while True:
        weight = float(input("Please input Durian weight: "))
        if weight == 0:
            break
        count += 1
        total_weight += weight
    
    if count > 0:
        print(f"\nTotal of {count} Durians")
        print(f"Average weight is {total_weight / count:.2f}")

durian_calculator()
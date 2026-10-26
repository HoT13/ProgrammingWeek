def find_perfect_numbers(limit):
    for num in range(1, limit + 1):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        if sum_divisors == num:
            print(f"{num} is a perfect number")

find_perfect_numbers(50)
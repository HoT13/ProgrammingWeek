def coin_exchange():
    while True:
        amount = int(input("\nEnter amount to exchange (0 to quit): "))
        if amount == 0:
            break
        
        c10 = amount // 10
        rem = amount % 10
        c5 = rem // 5
        c1 = rem % 5
        
        print(f"เหรียญ 10 จำนวน {c10} เหรียญ")
        print(f"เหรียญ 5 จำนวน {c5} เหรียญ")
        print(f"เหรียญ 1 จำนวน {c1} เหรียญ")

coin_exchange()
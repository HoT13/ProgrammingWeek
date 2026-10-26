import random

def guess_game_with_score():
    # สุ่มเลข 1-100
    target = random.randint(1, 100)
    score = 100
    print("--- เกมทายตัวเลข (1-100) ---")
    print("คุณมีคะแนนเริ่มต้น 100 คะแนน")
    print("ทายผิดจะถูกหัก 10 คะแนน, ใส่ 0 เพื่อเลิกเล่น")

    while True:
        try:
            guess = int(input("\nทายตัวเลขของคุณ: "))
        except ValueError:
            print("กรุณาใส่ตัวเลขจำนวนเต็มเท่านั้น")
            continue

        if guess == 0:
            print(f"เกมจบลงแล้ว! เลขที่ถูกต้องคือ {target}")
            print(f"คะแนนสุดท้ายของคุณคือ: {score}")
            break
        
        if guess == target:
            print(f"ยินดีด้วย! คุณทายถูก คะแนนของคุณคือ {score}")
            break
        else:
            score -= 10
            
            if score <= 0:
                print(f"คะแนนหมดแล้ว! คุณแพ้ เลขที่ถูกต้องคือ {target}")
                break
            
            if guess > target:
                print(f"น้อยกว่า (เหลือคะแนน {score})")
            else:
                print(f"มากกว่า (เหลือคะแนน {score})")

guess_game_with_score()
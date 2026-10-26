ROWS = 6
COLS = 7

def create_board():
    return [['.' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + " ".join([str(i) for i in range(COLS)]))
    for row in board:
        print("| " + " ".join(row) + " |")
    print("-" * (COLS * 2 + 3))

def drop_token(board, col, player):
    # วนลูปเช็คจากแถวล่างสุดขึ้นบน (Gravity System)
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == '.':
            board[r][col] = player
            return r
    return -1  # คอลัมน์เต็ม

def check_win(board, r, c, player):
    # ทิศทาง (dx, dy): แนวนอน, แนวตั้ง, ทแยงลงขวา, ทแยงขึ้นขวา
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        # เช็คทั้งทิศทางเดินหน้า (+1) และถอยหลัง (-1)
        for direction in [1, -1]:
            step = 1
            while True:
                nr = r + (dy * step * direction)
                nc = c + (dx * step * direction)
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == player:
                    count += 1
                    step += 1
                else:
                    break
        if count >= 4:
            return True
    return False

def play_game():
    board = create_board()
    current_player = 'X'  # ผู้เล่น X และ O
    turns = 0
    max_turns = ROWS * COLS

    while True:
        print_board(board)
        print(f"Turn: Player [{current_player}]")
        
        # รับค่าและตรวจสอบ Input
        try:
            col = int(input(f"Select column (0-{COLS-1}): "))
            if col < 0 or col >= COLS:
                print("Out of range! Please choose a valid column.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        row = drop_token(board, col, current_player)
        if row == -1:
            print("Column is full! Choose another column.")
            continue

        turns += 1

        # ตรวจสอบการชนะและเสมอ
        if check_win(board, row, col, current_player):
            print_board(board)
            print(f"\n Player [{current_player}] WINS!")
            break

        if turns == max_turns:
            print_board(board)
            print("\n DRAW GAME!")
            break

        # สลับผู้เล่น
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
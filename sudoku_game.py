def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(grid, row, col, num):
    # ตรวจสอบแถว
    if num in grid[row]:
        return False

    # ตรวจสอบคอลัมน์
    if num in [grid[i][col] for i in range(9)]:
        return False

    # ตรวจสอบกล่องย่อย 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # ค้นหาช่องว่าง
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = 0  # กลับสู่ค่าก่อนหน้า (backtrack)

                return False  # ไม่มีตัวเลขที่เหมาะสม

    return True  # แก้ปริศนาเสร็จสมบูรณ์
def add_num_to_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            num = int(input("Add Numbers To Board : "))
            board[i][j] = num
# ตัวอย่างตาราง Sudoku (0 แทนช่องว่าง)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Sudoku Puzzle:")
add_num_to_board(board)
print_grid(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_grid(board)
else:
    print("\nNo solution exists.")
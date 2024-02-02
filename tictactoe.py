move_data = []
matrix = [
    [" ", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count = 1 - count
        return count

    return counter


def print_matrix(mat):
    print("\n" * 100)
    for row in mat:
        print(" ".join(map(str, row)))


def input_step(mat, m_d, step_counter):
    sym = "x" if step_counter() == 1 else "o"
    print(f"Ход делает {'Керстик' if sym == 'x' else 'Нолик'}")

    while True:
        try:
            st = list(map(int, input("Введи два числа: ").split()))
            if len(st) == 2 and all(0 <= num <= 2 for num in st):
                if st not in m_d:
                    m_d.append(st)
                    mat[st[0] + 1][st[1] + 1] = sym
                    return st
                else:
                    print("Такой ход уже был совершен, попробуй снова")
            else:
                print("Введи ровно два числа в диапазоне от 0 до 2.")
        except ValueError:
            print("Неверный ввод. Введите только числа")


def check_win(mat):
    for row in mat[1:]:
        if row[1] == row[2] == row[3] != "-":
            return row[1]

    for col in range(1, 4):
        if mat[1][col] == mat[2][col] == mat[3][col] != "-":
            return mat[1][col]

    if mat[1][1] == mat[2][2] == mat[3][3] != "-":
        return mat[1][1]
    if mat[1][3] == mat[2][2] == mat[3][1] != "-":
        return mat[1][3]

    return None


def main():
    step_counter = create_counter()
    winner = None

    for i in range(9):
        print_matrix(matrix)
        input_step(matrix, move_data, step_counter)
        winner = check_win(matrix)
        if winner:
            print(f"Игрок {winner} победил")
            break

    if not winner:
        print("Ничья")


if __name__ == "__main__":
    main()

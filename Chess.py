class Chess:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.user_color = None

    def start(self):
        while True:
            print("Выберите цвет:")
            print("1. Белые")
            print("2. Черные")
            choice = input("Ваш выбор: ")
            if choice == "1":
                self.user_color = "white"
                break
            elif choice == "2":
                self.user_color = "black"
                break
            else:
                print("Пожалуйста, введите правильный номер.")

    def fill_board(self):
        # Располагаем фигуры на столе по умолчанию.
        for i in range(8):
            if i == 0:
                self.board[1][i] = 'r'
                self.board[6][i] = 'R'
            elif i < 3:
                self.board[i+1][i] = 'n'
                self.board[7-i][i] = 'N'
            elif i in [4,5]:
                self.board[0][i] = 'q'
                self.board[7][i] = 'Q'
            elif i == 6:
                self.board[i-1][i] = 'b'
                self.board[i+1][i] = 'B'

    def show_board_from_user_perspective(self):
        # Показывает текущее состояние стола от лица игрока
        if self.user_color == "white":
            for i in range(7, -1, -1):
                row = []
                for j in range(8):
                    row.append(self.board[i][j] if self.board[i][j] != ' ' else str(i+1) + str(j+1))
                print(" | ".join(row))
                print("-" * 30)
        else:
            for i in range(7, -1, -1):
                row = []
                for j in range(8):
                    if self.board[7-i][j] != ' ':
                        if self.board[7-i][j] == 'r':
                            row.append('R')
                        elif self.board[7-i][j] == 'n':
                            row.append('N')
                        elif self.board[7-i][j] == 'b':
                            row.append('B')
                        elif self.board[7-i][j] == 'q':
                            row.append('Q')
                    else:
                        row.append(str(8-i) + str(j+1))
                print(" | ".join(row))
                print("-" * 30)

    def show_board(self):
        # Показывает текущее состояние стола.
        for i in range(7, -1, -1):
            row = []
            for j in range(8):
                if self.board[i][j] != ' ':
                    if self.board[i][j] == 'r':
                        row.append('R')
                    elif self.board[i][j] == 'n':
                        row.append('N')
                    elif self.board[i][j] == 'b':
                        row.append('B')
                    elif self.board[i][j] == 'q':
                        row.append('Q')
                else:
                    row.append(str(8-i) + str(j+1))
            print(" | ".join(row))
            print("-" * 30)

def main():
    chess_game = Chess()
    chess_game.start()
    
    if chess_game.user_color == "white":
        print(f"You will play as {chess_game.user_color}.")
    else:
        print(f"Your opponent plays as {chess_game.user_color}. You will play as black.")
        
    chess_game.fill_board()
    chess_game.show_board_from_user_perspective()

if __name__ == "__main__":
    main()

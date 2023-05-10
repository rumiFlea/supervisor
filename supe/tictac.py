import tkinter as tk

class TicTacToeGUI:
    
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_player = 'X'
        self.x_score = 0
        self.o_score = 0
        self.create_gui()
        
    def create_gui(self):
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        
        self.frame1 = tk.Frame(self.window)
        self.frame1.pack()
        
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.frame1, text='', width=5, height=2, font=('Helvetica', 30, 'bold'),
                                   command=lambda row=row, col=col: self.handle_button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
            
        self.frame2 = tk.Frame(self.window)
        self.frame2.pack()
        
        self.turn_label = tk.Label(self.frame2, text=f"Current Player: {self.current_player}", font=('Helvetica', 16))
        self.turn_label.pack(side='left')
        
        reset_button = tk.Button(self.frame2, text='Reset', font=('Helvetica', 16), command=self.reset_board)
        reset_button.pack(side='left', padx=20)
        
        quit_button = tk.Button(self.frame2, text='Quit', font=('Helvetica', 16), command=self.window.destroy)
        quit_button.pack(side='left')
        
        self.window.mainloop()
        
    def handle_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                self.update_score()
                self.show_win_message()
                self.reset_board()
            elif self.check_tie():
                self.show_tie_message()
                self.reset_board()
            else:
                self.switch_player()
                self.update_turn_label()
        
    def check_win(self):
        for i in range(3):
            # check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            # check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
            
    def update_turn_label(self):
        self.turn_label.config(text=f"Current Player: {self.current_player}")
        
    def update_score(self):
        if self.current_player == 'X':
            self.x_score += 1
        else:
            self.o_score += 1
            
    def show_win_message(self):
        winner = self.current_player
        tk.messagebox.showinfo("Winner", f"{winner} wins!")
        
    def show_tie_message(self):
        tk.messagebox.showinfo("Tie", "It's a tie!")
        
    def check_tie(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
            
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ' '
                self.buttons[row][col].config(text='')
        self.current_player = 'X'
        self.update_turn_label()
            
if __name__ == '__main__':
    TicTacToeGUI()
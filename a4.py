# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self) -> int:
       
       self.board = ['*'] * 9
    
    def __str__(self) -> str:
       
        s = f"{self.board[0]} {self.board[1]} {self.board[2]}\n" f"{self.board[3]} {self.board[4]} {self.board[5]}\n" f"{self.board[6]} {self.board[7]} {self.board[8]}"
        return s
    
    def make_move(self, player, pos) -> bool:
       
        if pos < 0 or pos >= 9 or self.board[pos] != '*':
            return False  
        
        self.board[pos] = player
        return True
    
    def has_won(self, player) -> bool:
        ps = [player] * 3 
        
        if self.board[:3] == ps or self.board[3:6] == ps or self.board[6:] == ps:
            return True
        
        if self.board[::3] == ps or self.board[1::3] == ps or self.board[2::3] == ps:
            return True
        
        if self.board[::4] == ps or self.board[2:7:2] == ps:
            return True
        
        return False
    
    def game_over(self) -> bool:

        if self.has_won("X") or self.has_won("O") or "*" not in self.board:
            return True
        return False

    def clear_board(self):
        self.board = ['*'] * 9
        return self.board


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    print(brd)
    brd.make_move("X", 8)
    brd.make_move("O", 7)
    print(brd)
    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)
    print(brd)
    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear_board()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    play_tic_tac_toe()

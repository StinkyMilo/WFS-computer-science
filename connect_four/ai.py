import game_logic as game
from random import randint
class AI:
    name = "Default"
    team = -1

    def __init__(self,team):
        self.name="Default"
        self.team=team

    def make_move(self,board):
        return 0
class InputPlayer(AI):
    name = "Player"

    def __init__(self, team):
        super().__init__(team)
        self.name="Player"

    def make_move(self,board):
        return int(input("Make Move (0-6):\n"))


game.ai_classes.append(InputPlayer)


class RandomPlayer(AI):
    name = "Random"

    def __init__(self,team):
        super().__init__(team)
        self.name="Random"

    def make_move(self,board):
        valid_moves = []
        for i in range(0,game.BOARD_SIZE[0]):
            if game.get_y_of(board,i)!=-1:
                valid_moves.append(i)
        return valid_moves[randint(0,len(valid_moves)-1)]


game.ai_classes.append(RandomPlayer)


class Minimax(AI):
    # Loss function is how many the opponent has in a row.
    name = "Minimax"

    def __init__(self,team,depth=2):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK

    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -100 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 100 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.2*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000 if team == self.team else -1000000)
            else:
                boards.append(new_board)
        return boards

    def make_move(self,board):
        boards = self.get_boards(board,self.team)
        return self.choose_move(boards)[0]

    def choose_move(self,boards,layer=1):
        playing = self.team if layer % 2 == 0 else self.other_team
        if layer==self.depth:
            values = []
            for board in boards:
                value = self.value_of(board)
                values.append(value)
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        else:
            values = []
            for i in range(0,len(boards)):
                new_boards = self.get_boards(boards[i],playing)
                val = self.choose_move(new_boards,layer+1)
                values.append(val[1])
            val = self.choose_val(values,max if playing==self.team else min)
            return val


game.ai_classes.append(Minimax)


class MinimaxD4(Minimax):
    # Loss function is how many the opponent has in a row.
    name = "MinimaxD4"

    def __init__(self,team,depth=4):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK


game.ai_classes.append(MinimaxD4)
# Here's what you edit
class Template(AI):
    # Change "Template" to your AI's name
    name = "Default"

    def __init__(self,team):
        super().__init__(team)

    def make_move(self,board):
        # This is where your logic will go. This default AI will always go in the leftmost column.
        return 0


# Change "Template" to your AI's name
game.ai_classes.append(Template)

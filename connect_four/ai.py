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


# Here's what you edit
class Template(AI):
    # Change "Template" to your AI's name
    name = "Default"

    def __init__(self,team):
        super().__init__(team)
        self.name="Default"

    def make_move(self,board):
        # This is where your logic will go. This default AI will always go in the leftmost column.
        return 0


# Change "Template" to your AI's name
game.ai_classes.append(Template)

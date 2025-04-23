import random
from pieces import IPiece, TPiece, LLeftPiece, LRightPiece, SRightPiece, SLeftPiece, SquarePiece
from common import ColorEnum

class Factory():

    def __init__(self):
        super().__init__()
        self.pieces_class = [IPiece, TPiece, LLeftPiece, LRightPiece, SRightPiece, SLeftPiece, SquarePiece]
        self.pieces_colors = [ColorEnum.BLUE, ColorEnum.GREEN, ColorEnum.RED, ColorEnum.RED, ColorEnum.VIOLET, ColorEnum.VIOLET, ColorEnum.YELLOW]
    
    def create_piece(self, position_x, position_y):
        random_index = random.randint(0, len(self.pieces_class) - 1)
        return self.pieces_class[random_index](position_x, position_y, self.pieces_colors[random_index].value)
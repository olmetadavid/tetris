from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, position_x, position_y, color):
        super().__init__()
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        
        self.matrix = []
    
    def rotate(self):
        """ Rotate the piece, always in the same direction """
        self.matrix = list(zip(*self.matrix[::-1]))

class IPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 1, 4
        matrix = [[True for x in range(cols)] for y in range(rows)] 

        self.matrix = matrix

class TPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 2, 3
        matrix = [[False for x in range(cols)] for y in range(rows)] 

        matrix[0][0] = True
        matrix[0][1] = True
        matrix[0][2] = True
        matrix[1][1] = True

        self.matrix = matrix

class LRightPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 3, 2
        matrix = [[False for x in range(cols)] for y in range(rows)] 

        matrix[0][0] = True
        matrix[1][0] = True
        matrix[2][0] = True
        matrix[2][1] = True

        self.matrix = matrix

class LLeftPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 3, 2
        matrix = [[False for x in range(cols)] for y in range(rows)] 

        matrix[0][1] = True
        matrix[1][1] = True
        matrix[2][0] = True
        matrix[2][1] = True

        self.matrix = matrix

class SRightPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 2, 3
        matrix = [[False for x in range(cols)] for y in range(rows)] 

        matrix[0][1] = True
        matrix[0][2] = True
        matrix[1][0] = True
        matrix[1][1] = True

        self.matrix = matrix

class SLeftPiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 2, 3
        matrix = [[False for x in range(cols)] for y in range(rows)] 

        matrix[0][0] = True
        matrix[0][1] = True
        matrix[1][1] = True
        matrix[1][2] = True

        self.matrix = matrix

class SquarePiece(Piece):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x=position_x, position_y=position_y, color=color)

        # Create matrix and initialize each box
        rows, cols = 2, 2
        matrix = [[True for x in range(cols)] for y in range(rows)] 

        self.matrix = matrix

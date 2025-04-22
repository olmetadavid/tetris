from pieces import Piece
from factory import Factory
from functools import reduce
import pygame

class Board:
    def __init__(self, pygame, window_padding, board_score_height, width, height, grid_width, grid_height, cube_width):
        super().__init__()
        
        self.pygame = pygame
        
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREY = (100, 100, 100)
        
        self.velocity_timer = 1000
        
        self.board_score_height = board_score_height
        
        self.window_padding = window_padding
        self.width = width
        self.height = height
        
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cube_width = cube_width
        
        self.start_position_x = self.grid_width // 2
        self.start_position_y = 0
        
        self.margins = 2
        
        self.active_shape = None
        
        self.pieces_factory = Factory()
        
        self.end_game = False
        self.score_total = 0
        
        # Create grid to store if a cube of piece is store in it, and its color
        rows, cols = self.grid_height, self.grid_width
        self.grid = [[{'ticked': False, 'color': self.BLACK} for x in range(cols)] for y in range(rows)] 
        
        pygame.time.set_timer(pygame.USEREVENT, self.velocity_timer)
    
    def draw(self, canvas):
        """ Draw board game """
        
        # Draw board
        canvas.fill(self.BLACK)
        self.pygame.draw.line(canvas, self.WHITE, [self.window_padding, self.window_padding + self.board_score_height], [self.window_padding, self.height - self.window_padding], 1)
        self.pygame.draw.line(canvas, self.WHITE, [self.window_padding, self.height - self.window_padding], [self.width - self.window_padding, self.height - self.window_padding], 1)
        self.pygame.draw.line(canvas, self.WHITE, [self.width - self.window_padding, self.height - self.window_padding], [self.width - self.window_padding, self.window_padding + self.board_score_height], 1)
        
        if not self.end_game:
            
            # Draw active shape
            if self.active_shape == None:
                
                self.current_position_x = self.start_position_x
                self.current_position_y = self.start_position_y
                
                self.active_shape = self.pieces_factory.create_piece(self.current_position_x, self.current_position_y, (60, 125, 210))
                
                # TODO: End of the game
                if self.is_collided(self.active_shape):
                    print('END OF THE GAME')
                    self.end_game = True
            
            self.draw_piece(canvas=canvas, piece=self.active_shape)
        
        self.draw_grid(canvas=canvas)
        
        self.draw_score(canvas=canvas)
    
        return True
    
    def draw_score(self, canvas):
        font = pygame.font.SysFont('Comic Sans MS', 48)
        label = font.render(f'Score {self.score_total}', 1, (255, 255, 255))
        canvas.blit(label, (50, 20))
    
    def draw_grid(self, canvas):
        
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                if col['ticked'] == True:
                    self.pygame.draw.polygon(canvas, col['color'], self.create_cube(self.get_position_x(col_index), self.get_position_y(row_index)), 0)
                    
    def before_drawing_piece(self, piece: Piece):
        
        # Case of left of board 
        if piece.position_x < 0:
            piece.position_x += 1
        
        # Case of right of board
        if (piece.position_x + len(piece.matrix[0])) > len(self.grid[0]):
            piece.position_x -= 1
            
        # Case of bottom of board
        if piece.position_y + len(piece.matrix) > self.grid_height:
            self.save_piece(piece)
        else:
            # Case of collision
            collided = self.is_collided(piece=piece)
            if collided:
                self.save_piece(piece=piece)
        
    def save_piece(self, piece):
    
        # Reward y axis with 1
        position_y = piece.position_y - 1
        
        for row_index, row in enumerate(piece.matrix):
            for col_index, col in enumerate(row):
                grid_square = self.grid[position_y + row_index][piece.position_x + col_index]
                if grid_square['ticked'] == False: 
                    if col:
                        self.grid[position_y + row_index][piece.position_x + col_index] = {
                            'ticked': True,
                            'color': piece.color
                        }
        
        self.active_shape = None
        
        # Remove completed line
        self.remove_completed_lines()
        
    def remove_completed_lines(self):
        new_grid = []
        number_removed = 0 
        
        # Remove lines recreating new grid without these lines
        for row_index, row in enumerate(self.grid):
            
            ticked = list(map(lambda a: a['ticked'], row))
            all_ticked = reduce(lambda a, b: a and b, ticked)
                    
            if not all_ticked:
                new_grid.append(row)
            else:
                number_removed += 1

        # Add score
        if number_removed > 0:
            self.score(number_of_lines=number_removed)

            # Insert new lines at the begining of the grid        
            for i in range(number_removed):
                new_grid.insert(0, [{'ticked': False, 'color': self.BLACK} for x in range(self.grid_width)])
                
            self.grid = new_grid

    def is_collided(self, piece):
        for row_index, row in enumerate(piece.matrix):
            for col_index, col in enumerate(row):
                grid_square = self.grid[piece.position_y + row_index][piece.position_x + col_index]
                
                if col and grid_square['ticked']:
                    return True
        return False
    
    def after_drawing_piece(self, piece: Piece):
        pass
    
    def create_cube(self, x, y):
        """ Create a cube of piece """
        
        return [
            [x + self.margins, y + self.margins],
            [x + self.cube_width - self.margins, y + self.margins],
            [x + self.cube_width - self.margins, y + self.cube_width - self.margins],
            [x + self.margins, y + self.cube_width - self.margins]
        ]

    def draw_piece(self, canvas, piece: Piece):
        """ Draw piece of game """
        
        self.before_drawing_piece(piece=piece)
        
        # If the active shape has been removed, don't try to draw it
        if self.active_shape == None:
            return
        
        shapes = []
        
        position_y = self.get_position_y(piece.position_y)
        for row in piece.matrix:
            position_x = self.get_position_x(piece.position_x)
            for col in row:
                if col:
                    shapes.append(self.create_cube(position_x, position_y))
                position_x += self.cube_width
            
            position_y += self.cube_width
        
        for shape in shapes:
            self.pygame.draw.polygon(canvas, self.active_shape.color, shape, 0)
        
        self.after_drawing_piece(piece=piece)
            
    def move_down(self):
        if self.active_shape != None:
            self.active_shape.position_y += 1
        
    def move_left(self):
        if self.active_shape != None:
            self.active_shape.position_x -= 1
        
    def move_right(self):
        if self.active_shape != None:
            self.active_shape.position_x += 1
                
    def rotate(self):
        if self.active_shape != None:
            self.active_shape.rotate()

    def get_position_y(self, position_y):
        return self.board_score_height + self.window_padding + (position_y * self.cube_width)

    def get_position_x(self, position_x):
        return self.window_padding + (position_x * self.cube_width)
    
    def score(self, number_of_lines):
        self.score_total += number_of_lines * number_of_lines
        
        if self.score_total % 10:
            self.velocity_timer -= 100
            pygame.time.set_timer(pygame.USEREVENT, self.velocity_timer)

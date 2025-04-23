# Tetris

This is a tetris like (test of PyGame python library: https://www.pygame.org)

# How to start

Create virtual env, install requirements and start the game: 

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
python3 main.py
deactivate
```

# Screenshot

![alt text](doc/images/screenshot1.png "Screenshot")

# High Level Design

```mermaid
---
title: Payloads
---
classDiagram
    class ABC
    <<Abstract>> ABC

    namespace pieces {
        class Piece {
            - position_x
            - position_y
            - color
            - matrix
            rotate()
        }
        class IPiece
        class TPiece
        class LRightPiece
        class LLeftPiece
        class SRightPiece
        class SLeftPiece
        class SquarePiece
    }

    class Factory {
        - pieces_class
        - pieces_colors
        create_piece()
    }

    class Board {
        - velocity_timer
        - board_score_height
        - window_padding
        - width
        - height
        - grid_width
        - grid_height
        - cube_width
        - start_position_x
        - start_position_y
        - margins
        - active_shape
        - pieces_factory
        - end_game
        - score_total
        - grid
        draw()
        draw_score()
        before_drawing_piece()
        save_piece()
        remove_completed_lines()
        is_collided()
        after_drawing_piece()
        create_cube()
        draw_piece()
        move_down()
        move_left()
        move_right()
        rotate()
        get_position_y()
        get_position_x()
        score()
    }

    ABC <|-- Piece : extends
    Piece <|-- IPiece : extends
    Piece <|-- TPiece : extends
    Piece <|-- LRightPiece : extends
    Piece <|-- LLeftPiece : extends
    Piece <|-- SRightPiece : extends
    Piece <|-- SLeftPiece : extends
    Piece <|-- SquarePiece : extends

    Factory --> Piece : create

    Board o-- Piece : manage
```
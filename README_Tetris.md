# Tetris Game

A simple Tetris clone built using Python and Pygame. This project demonstrates the core mechanics of Tetris, including piece movement, rotation, line clearing, and score tracking.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a fully functional Tetris game created with Python and Pygame. It aims to replicate the traditional Tetris experience, including randomized tetromino generation, grid-based movement, row clearing, and a scoring system. It's a fun project that demonstrates how to handle 2D game logic, simple rendering, and event-driven programming.

## Features

- **Grid-based gameplay**: Traditional Tetris mechanics with a 10x20 grid.
- **Tetromino shapes**: Includes all standard Tetris pieces.
- **Piece rotation**: Rotate pieces in real-time.
- **Score system**: Earn points for clearing rows.
- **High score tracking**: Keeps track of the highest score during the session.
- **Smooth animations**: Handles piece movement and rendering.
- **Randomized Tetrominoes**: Each tetromino is generated randomly to simulate the original game.

## Installation

1. Make sure you have Python installed (Python 3.6 or higher is recommended).
2. Install the `pygame` library by running:
    ```bash
    pip install pygame
    ```
3. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tetris-game.git
    ```
4. Navigate to the project folder:
    ```bash
    cd tetris-game
    ```
5. Run the game:
    ```bash
    python tetris.py
    ```

## How to Play

- **Move Left**: Press the left arrow key to move the piece left.
- **Move Right**: Press the right arrow key to move the piece right.
- **Move Down**: Press the down arrow key to drop the piece faster.
- **Rotate**: Press the up arrow key to rotate the piece.
- **Quit**: Press the close button or ESC to exit the game.

Your goal is to fit the falling tetrominoes together to complete rows. When a row is completed, it disappears, and you earn points. The game ends when the pieces reach the top of the grid.

## Game Mechanics

### Grid and Tetrominoes

- The game grid is 10 blocks wide and 20 blocks tall.
- Each tetromino is made up of four blocks and falls from the top of the grid.
- Tetrominoes can be moved left, right, and down. They can also be rotated.

### Collision Detection

- Collision detection is handled by checking the position of the tetromino against the walls of the grid and other locked tetrominoes.

### Scoring

- Every time a row is completely filled with blocks, it gets cleared, and the player is awarded points.
- The number of points depends on the number of rows cleared at once:
  - 1 row = 100 points
  - 2 rows = 200 points
  - 3 rows = 300 points
  - 4 rows = 400 points

### Game Over

- The game ends when new tetrominoes can no longer be placed on the grid due to lack of space.

## Code Structure

The game consists of several core functions and classes:

### 1. **Tetromino Class**

This class handles the creation, movement, and rotation of the tetromino pieces.

- **`__init__(self, x, y)`**: Initializes a tetromino at the given position with a random shape and color.
- **`rotate(self)`**: Rotates the tetromino.
- **`get_shape(self)`**: Retrieves the current shape of the tetromino based on its rotation state.

### 2. **Grid and Drawing Functions**

- **`create_grid(locked_positions={})`**: Creates the 10x20 grid and updates it with locked positions of tetrominoes.
- **`draw_grid(surface, grid)`**: Draws the game grid and locked tetrominoes.
- **`draw_tetromino(surface, tetromino)`**: Draws the current tetromino on the screen.

### 3. **Game Loop**

The `main()` function contains the game loop, handling events, moving tetrominoes, checking for collisions, and updating the display:

- **`clock.tick()`**: Regulates the speed of the game.
- **`pygame.event.get()`**: Listens for keyboard input.
- **`valid_move()`**: Checks whether a tetromino can be moved to a new position.

### 4. **Score System**

- **`draw_score(surface, score, high_score)`**: Displays the current score and the high score on the screen.
- **`clear_rows(grid, locked)`**: Clears any fully filled rows, updating the locked positions and increasing the score.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests if you'd like to improve the game or add new features!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


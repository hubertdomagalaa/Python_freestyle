# Snake Game - Pygame Project

Welcome to the **Snake Game** project! This project is a simple yet classic version of the Snake game, implemented using Python and Pygame. The player controls a snake that grows in length each time it eats food, and the game ends when the snake collides with the wall or itself.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Code Breakdown](#code-breakdown)
5. [Future Improvements](#future-improvements)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- **Responsive Controls**: Move the snake using the arrow keys.
- **Dynamic Gameplay**: Snake speeds up as the game progresses.
- **Food Spawn Mechanism**: Food appears randomly, and the snake grows each time it eats.
- **End Game Logic**: The game ends if the snake collides with itself or the boundaries of the screen.
- **Restart Option**: After losing, the player can restart by pressing 'C' or quit by pressing 'Q'.

## Installation

To run the game locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/snake-game-pygame.git
   cd snake-game-pygame
   ```

2. **Install dependencies:**
   You need to have [Python](https://www.python.org/downloads/) and [Pygame](https://www.pygame.org/wiki/GettingStarted) installed. To install Pygame, use:
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   After installing the dependencies, run the game with:
   ```bash
   python snake_game.py
   ```

## How to Play

- **Start the game**: The game automatically starts when the script is run.
- **Move the snake**: Use the arrow keys to change the snake's direction.
- **Objective**: Eat the red food that appears on the screen. Each time you eat, the snake grows.
- **Game over**: The game ends if the snake hits the boundaries of the screen or itself.
- **Restart or Quit**: After losing, press 'C' to play again or 'Q' to quit.

## Code Breakdown

### 1. **Initializing Pygame**

```python
pygame.init()
```
This line initializes the Pygame library, which sets up everything we need to use its functions.

### 2. **Setting Up the Game Window**

```python
width = 800
height = 600
window = pygame.display.set_mode((width, height))
```
We create an 800x600 window for the game. The `set_mode()` function from Pygame creates a display surface that will represent the game area.

### 3. **Colors and Game Properties**

The game uses basic colors (black, white, red, green) and properties such as the snake block size and speed:

```python
snake_block = 20
snake_speed = 15
```

### 4. **The Snake Function**

```python
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])
```
This function draws each segment of the snake on the screen using a list `snake_list` that stores the positions of all the snake segments.

### 5. **Message Function**

```python
def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])
```
This function renders and displays a message on the screen when the game is over.

### 6. **Main Game Loop**

The core logic of the game resides in the `gameLoop()` function. Here are the key steps:

- **Event Handling**: This section checks for player input and game events like quitting the game or moving the snake.

  ```python
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
  ```

- **Snake Movement**: Depending on the player's input, the snake's direction changes:

  ```python
  if event.key == pygame.K_LEFT:
      x1_change = -snake_block
      y1_change = 0
  ```

- **Boundary and Collision Detection**: The game checks if the snake hits the walls or itself.

  ```python
  if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
      game_close = True
  ```

- **Food Consumption and Snake Growth**: When the snake eats the food, its length increases, and new food is generated.

  ```python
  if x1 == foodx and y1 == foody:
      length_of_snake += 1
  ```

### 7. **Game Over and Restart Logic**

If the game ends, a message is displayed, and the player is given the option to restart or quit:

```python
message("You Lost! Press Q-Quit or C-Play Again", RED)
```

## Future Improvements

- **Score Tracking**: Add a scoring system to keep track of the player's progress.
- **Sound Effects**: Introduce sound effects for eating food and losing the game.
- **Multiple Levels**: Include levels with increasing difficulty, such as faster snake speed or obstacles on the screen.
- **Pause Functionality**: Implement a pause option during gameplay.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you find bugs or want to add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




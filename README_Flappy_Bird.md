# Flappy Bird Game

![Flappy Bird](flappy_bird.png)

The Flappy Bird Game is a Python implementation using the Pygame library, featuring a simple yet addictive gameplay where the player controls a bird, guiding it through gaps between pipes without colliding. This README provides an overview of the game structure, mechanics, and setup instructions.

## Table of Contents

- [Introduction](#introduction)
- [Game Features](#game-features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Mechanics](#game-mechanics)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a clone of the classic Flappy Bird game, built using Python and Pygame. It includes the basic elements of the original game, such as bird movement, pipe generation, collision detection, and scoring mechanics.

## Game Features

- **Bird Control**: Control the bird's altitude by pressing the spacebar to flap.
- **Pipes**: Pipes move from right to left across the screen at varying heights.
- **Scoring**: Earn points by successfully passing through gaps between pipes.
- **Collision Detection**: Game ends if the bird collides with the pipes or goes out of bounds (top or bottom of the screen).
- **Simple and Addictive Gameplay**: Easy to learn but challenging to master.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/flappy-bird-game.git
   cd flappy-bird-game
   ```

2. **Install Pygame**:
   If Pygame is not already installed, install it using pip:
   ```bash
   pip install pygame
   ```

## Usage

1. **Run the Game**:
   Navigate to the project directory and run the main script:
   ```bash
   python main.py
   ```

2. **Game Controls**:
   - Press `SPACEBAR` to flap and navigate the bird through the gaps between pipes.
   - Avoid collision with the pipes to keep the game running and earn points by passing through gaps.

## Game Mechanics

### Components

- **Bird (`Bird` class)**:
  - Controlled by player input (`flap` method).
  - Falls under gravity (`GRAVITY`) and can flap upwards with a set strength (`FLAP_STRENGTH`).

- **Pipes (`Pipe` class)**:
  - Generated at random heights with a gap (`PIPE_GAP`) between them.
  - Move from right to left (`PIPE_SPEED`).

- **Scoring**:
  - Earn points (`score`) by passing through gaps between pipes.
  - Game ends when the bird collides with a pipe or goes out of bounds.

### Classes and Functions

- **`Bird` Class**: Manages bird's position, velocity, and drawing.
- **`Pipe` Class**: Handles pipe generation, movement, and drawing.
- **`game_loop` Function**: Main game loop that updates game state, handles user input, and renders the game.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


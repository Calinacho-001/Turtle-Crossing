# Turtle Crossing 🐢🚗

## Description

Turtle Crossing is an exciting Python game where the player controls a turtle, navigating through traffic by dodging moving cars. The objective is to reach the top of the screen without colliding with any cars. Each time the player successfully crosses, the level increases, making the game progressively harder. 

This project demonstrates **object-oriented programming (OOP)** with classes for the player, cars, scoreboard, and game mechanics, all built using Python’s `turtle` graphics module.

## Features

- **Player Control**: Move the turtle forward using the Up arrow key.
- **Randomized Cars**: Cars appear at random positions on the screen and move toward the player.
- **Increasing Difficulty**: As the player progresses, the speed of the cars increases.
- **Level Tracking**: The current level is displayed at the top of the screen, increasing each time the player crosses the finish line.
- **Game Over**: The game ends if the player collides with a car, displaying a "GAME OVER" message.

## Requirements

- Python 3.x
- `turtle` graphics module (pre-installed with Python)

## How to Play

1. **Start the Game**:
   - Run the `main.py` script to start the game.

2. **Control the Turtle**:
   - Press the **Up arrow key** to move the turtle forward.

3. **Cross the Finish Line**:
   - Successfully dodge cars and reach the top of the screen to increase your level.

4. **Game Over**:
   - If the turtle collides with a car, the game ends and displays "GAME OVER."

5. **Reset**:
   - The game automatically resets when the player reaches the finish line and increases the difficulty.

## Code Structure

### Files Breakdown

Here is a breakdown of each file and its purpose in the game:

---

### `main.py`

- **Purpose**: This is the main file that runs the game. It initializes the screen, player, car manager, and scoreboard, and manages the game loop.
- **Key Functionality**:
  - Controls the flow of the game and handles player movements.
  - Detects collisions with cars and updates the score.
  - Increases difficulty by speeding up the cars after each successful crossing.

---

### `player.py`

- **Purpose**: This file defines the `Player` class, representing the turtle that the player controls.
- **Key Functions**:
  - `move_up()`: Moves the turtle forward.
  - `go_to_start()`: Resets the turtle to the starting position.
  - `is_at_finish()`: Checks if the turtle has reached the top of the screen (finish line).

---

### `car_manager.py`

- **Purpose**: This file defines the `CarManager` class, responsible for creating and managing the moving cars.
- **Key Functions**:
  - `create_cars()`: Randomly creates cars at random vertical positions.
  - `move_cars()`: Moves all cars across the screen.
  - `level_up()`: Increases the car speed when the player reaches a new level.

---

### `scoreboard.py`

- **Purpose**: This file defines the `Scoreboard` class, which tracks and displays the player's level.
- **Key Functions**:
  - `update_scoreboard()`: Displays the current level at the top of the screen.
  - `plus_score()`: Increases the level by one and updates the scoreboard.
  - `game_over()`: Displays a "GAME OVER" message when the player loses.

---

## How to Run

1. Clone or download the project files.
2. Make sure Python 3.x is installed on your computer.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the game:

```bash
python main.py
```


## Future Improvements

- **Sound Effects**: Add sound effects for events like collisions or level-ups.
- **New Obstacles**: Introduce new types of obstacles or enemies to increase the challenge.
- **Player Skins**: Allow the player to choose from different turtle skins.
- **Leaderboard**: Track high scores and display a leaderboard for the best players.

## Credits

This project was created as an exercise to demonstrate object-oriented programming (OOP) principles and basic game development using Python's `turtle` graphics module.

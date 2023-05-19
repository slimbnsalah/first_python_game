# Game of the Goose
This is a Python implementation of the classic board game "Game of the Goose." The project demonstrates my programming skills in Python.

## Game Description
The Game of the Goose is a turn-based race game where players roll dice and move their pieces along a game board. The objective is to be the first player to reach the final case and win the game.

## Project Details
The game is developed using Python and incorporates various Python data structures and programming techniques. Here's an overview of the key components and features:

- Game Board: The main game board is represented by a list where each element corresponds to a specific case on the board. Players' positions are tracked using the list indices.
- Dice Rolling: Random numbers are generated to simulate dice rolls. The game uses the randint() function from the random module to generate dice values.
- Player Movement: Players can move their pieces based on the sum of the dice roll. The game utilizes list manipulation techniques to update players' positions on the board.
- Special Cases: The game includes special cases such as 'Bridge', 'Prison', 'Hotel'... These cases trigger specific actions or restrictions on players' movement.
- Win Condition: The game continues until one player reaches the final case, indicating the winner. The program then displays the winner's name.

More rules can be found in this link: mastersofgames.com/rules/goose-game-rules.htm

## Getting Started
To run the game on your local machine, follow these steps:

1. Ensure you have Python installed on your system.
1. Clone this repository to your local machine.
1. Open a terminal or command prompt and navigate to the project directory.
1. Run the command <code>python main.py</code> to start the game.
1. Follow the on-screen instructions to play the game.

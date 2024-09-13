# Slot Machine

This is a simple command-line slot machine game written in Python. Players can deposit money, place bets on multiple lines, and spin the slot machine to try their luck. The game will calculate winnings based on the symbols that appear in the slot machine.

## Features

- Deposit money to play the game.
- Place bets on up to 3 lines.
- Spin the slot machine and see the results.
- Calculate winnings based on the symbols that appear.
- Continue playing until you run out of balance or choose to quit.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/erenyavuzs/Slot-Machine.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Slot-Machine
    ```

## Usage

1. Run the `main.py` script:
    ```bash
    python3 main.py
    ```
2. Follow the on-screen instructions to:
   - Deposit money
   - Select the number of lines to bet on
   - Set the bet amount per line
   - Spin the slot machine and check for winnings.

## Explanation of Line Selection

- The game allows you to bet on **up to 3 lines**
  - **Line 1**: The top row.
  - **Line 2**: The middle row.
  - **Line 3**: The bottom row.
  
- **Betting options**:
  - Enter `1` to bet on Line 1 (the top row only).
  - Enter `2` to bet on Line 1 and Line 2 (top and middle rows).
  - Enter `3` to bet on all three rows (top, middle, and bottom).

- After selecting the number of lines, the bet amount for each line will be entered.

- The slot machine spins, and the result is displayed. If symbols on the selected lines match, winnings are calculated based on the value of the symbols and your bet.

## Example Output

```bash
What would you like to deposit? $100
Enter the number of lines to bet on (1-3)? 3
What would you like to bet on each line? $5
You are betting $5 on 3 lines. Total bet is equal to: $15

7   | BAR | cherries
BAR |  7  | lemon
BAR | BAR | cherries

You won $0!
You won on lines: 

Current balance is $85
Press enter to play (q to quit).

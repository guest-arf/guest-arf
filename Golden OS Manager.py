import os
import subprocess


def calculator():
    print("Welcome to calculator.")
    print("Options: +, -, *, /, Quit")

    while True:
        option = input("Calculator > ").strip()
        if option.lower() == "quit":
            break

        if option not in "+-*/":
            print("Invalid option. Please enter one of +, -, *, / or Quit.")
            continue

        try:
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
            continue

        if option == "+":
            print(f"Result: {num1 + num2}")
        elif option == "-":
            print(f"Result: {num1 - num2}")
        elif option == "*":
            print(f"Result: {num1 * num2}")
        elif option == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")

    print("Exiting calculator.")


def text_editor():
    print("Welcome to the text editor.")
    print("Options: 1. Create new file  2. Edit existing file  3. Quit")

    while True:
        option = input("Text Editor > ").strip()

        if option == "3":
            print("Exiting text editor.")
            break

        if option not in ["1", "2"]:
            print("Invalid option. Please choose 1, 2 or 3.")
            continue

        file_path = input("Enter the file path: ")
        if option == "1" and os.path.exists(file_path):
            overwrite = input(f"File '{file_path}' already exists. Overwrite? (yes/no): ")
            if overwrite.lower() != "yes":
                continue

        try:
            with open(file_path, "w") as file:
                print("Enter text (type 'EXIT' on a new line to save and exit):")
                while True:
                    line = input()
                    if line.upper() == "EXIT":
                        break
                    file.write(line + "\n")
            print("File saved successfully.")
        except Exception as e:
            print(f"Error while writing to file: {e}")
            continue


def tictactoe():
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(board, player):
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]],
        ]
        return [player, player, player] in win_conditions

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {players[turn]}, enter row (0, 1, 2): "))
            col = int(input(f"Player {players[turn]}, enter col (0, 1, 2): "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Row and column must be between 0 and 2.")

            if board[row][col] == " ":
                board[row][col] = players[turn]
                if check_winner(board, players[turn]):
                    print_board(board)
                    print(f"Player {players[turn]} wins!")
                    break
                turn = (turn + 1) % 2
            else:
                print("Invalid move. Cell is already taken.")
        except (IndexError, ValueError) as e:
            print(f"Error: {e}. Please enter valid row/column numbers.")

        if all(cell != " " for row in board for cell in row):
            print("It's a tie!")
            break


def file_explorer():
    def list_directory(path):
        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    print(f"{'DIR' if entry.is_dir() else 'FILE'}: {entry.name}")
        except Exception as e:
            print(f"Error reading directory: {e}")

    current_path = os.getcwd()
    print(f"Current Directory: {current_path}")

    while True:
        list_directory(current_path)
        print("Commands: cd <dir>, up, execute <file>, quit")
        command = input("File Explorer > ").split()

        if not command:
            print("Invalid command.")
            continue

        if command[0] == "quit":
            break

        elif command[0] == "cd" and len(command) > 1:
            new_path = os.path.join(current_path, command[1])
            if os.path.isdir(new_path):
                current_path = new_path
                print(f"Changed directory to: {current_path}")
            else:
                print("Directory not found.")

        elif command[0] == "up":
            current_path = os.path.dirname(current_path)
            print(f"Changed directory to: {current_path}")

        elif command[0] == "execute" and len(command) > 1:
            execute_file(os.path.join(current_path, command[1]))

        else:
            print("Invalid command.")


def execute_file(file_path):
    """Executes the given file based on its extension."""
    if os.path.isfile(file_path):
        try:
            _, file_extension = os.path.splitext(file_path)
            if file_extension == ".py":
                # Execute Python file
                subprocess.run(["python", file_path], check=True)
            elif os.name == "nt" and file_extension == ".exe":
                # Execute Windows executable
                os.system(file_path)
            else:
                # Attempt to open file with system default program
                if os.name == "nt":  # Windows
                    os.startfile(file_path)
                elif os.name == "posix":  # macOS/Linux
                    subprocess.run(["open", file_path] if "darwin" in os.uname() else ["xdg-open", file_path])
            print(f"Executed file: {file_path}")
        except Exception as e:
            print(f"Error executing file: {e}")
    else:
        print("File not found.")


def main_menu():
    print("Welcome to Golden OS Manager!")
    while True:
        print("\nCommands")
        print("file_read: Read a file")
        print("calculator: Use calculator")
        print("text_editor: Use text editor")
        print("tictactoe: Play Tic Tac Toe")
        print("file_explorer: Open file explorer")
        print("execute: Execute a file")
        print("quit: Exit the Golden OS Manager")

        option = input("GoldenOS > ").strip()

        if option == "file_read":
            try:
                file_path = input("File Path: ")
                with open(file_path, "r") as file:
                    print(file.read())
            except Exception as e:
                print(f"Error reading file: {e}")
        elif option == "calculator":
            calculator()
        elif option == "text_editor":
            text_editor()
        elif option == "tictactoe":
            tictactoe()
        elif option == "file_explorer":
            file_explorer()
        elif option == "execute":
            file_path = input("Enter the file path to execute: ")
            execute_file(file_path)
        elif option == "quit":
            print("Exiting Golden OS Manager...")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main_menu()

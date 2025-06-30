from tabulate import tabulate


def main():

    board = board_state()

    pieces = pieces_dict()

    coordinates = board_coordinates()

    white_format = white_format_input(pieces)

    white_position = white_input(board, pieces, coordinates, white_format)

    black_format = black_format_input(pieces, coordinates, board)

    black_position = black_input(board, pieces, coordinates, black_format)

    taken_pieces = taking(board, white_format)


# Function returns empty board (nested list) and used for later board state updates.
# First row and last column represents the indices of the real chess board.
def board_state():
    return [
        ["8", " ", " ", " ", " ", " ", " ", " ", " "],
        ["7", " ", " ", " ", " ", " ", " ", " ", " "],
        ["6", " ", " ", " ", " ", " ", " ", " ", " "],
        ["5", " ", " ", " ", " ", " ", " ", " ", " "],
        ["4", " ", " ", " ", " ", " ", " ", " ", " "],
        ["3", " ", " ", " ", " ", " ", " ", " ", " "],
        ["2", " ", " ", " ", " ", " ", " ", " ", " "],
        ["1", " ", " ", " ", " ", " ", " ", " ", " "],
        ["X", "a", "b", "c", "d", "e", "f", "g", "h"],
    ]


# Returns a dictionry (nested dict) with mapped piece abbreviations (keys) to piece name and color.
def pieces_dict():
    return {
        "wP": {"name": "pawn", "color": "white"},
        "wR": {"name": "rook", "color": "white"},
        "bP": {"name": "pawn", "color": "black"},
        "bR": {"name": "rook", "color": "black"},
        "bN": {"name": "knight", "color": "black"},
        "bB": {"name": "bishop", "color": "black"},
        "bQ": {"name": "queen", "color": "black"},
        "bK": {"name": "king", "color": "black"},
    }


#Returns a dictionary that maps traditional chess indices to board indices of the nested list.
def board_coordinates():
    return {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "8": 0,
        "7": 1,
        "6": 2,
        "5": 3,
        "4": 4,
        "3": 5,
        "2": 6,
        "1": 7,
    }


# Prompts the user to input white piece and its coordinate.
# Then function validates, if the format of the input is correct.
# Then returns a tuple (piece, place).
def white_format_input(pieces):
    while True:
        try:
            piece, place = (
                input(
                    "Choose white piece between pawn and rook with\n"
                    "its coordinate on the board, e.g.: pawn a5 \n",
                )
                .strip()
                .lower()
                .split(" ")
            )
            if piece not in [info["name"] for info in pieces.values() if info["color"] == "white"]:
                print("\nWrong piece name.\n")
                continue
            if len(place) != 2:
                print("\nInvalid coordinate format.\n")
                continue
            if place[0] not in "abcdefgh":
                print("\nInvalid coordinate format.\n")
                continue
            if place[1] not in "12345678":
                print("\nInvalid coordinate format.\n")
                continue

            return piece, place

        except ValueError:
            print("\nInvalid input format.\n")
            continue


# Prompts the user to input black pieces (up to 16 or until 'done').
# Validates the format of the input.
# Returns a temporary list of tuples for the black pieces added.
def black_format_input(pieces, coordinates, board):
    temp_black_list = []
    used_black_pieces = set()
    while True:
        try:
            input_check = input(
                "Choose any black pieces (up to 16) with\n"
                "its coordinates on the board, e.g.: knight a5\n"
                "if finished input 'done'.\n",
            )
            if input_check.strip().lower() == "done":
                if len(temp_black_list) > 0:
                    return temp_black_list
                else:
                    print("\nYou need at least one black piece.\n")
                    continue

            piece, place = input_check.strip().lower().split(" ")

            if piece not in [info["name"] for info in pieces.values() if info["color"] == "black"]:
                print("\nWrong piece name.\n")
                continue
            if len(place) != 2:
                print("\nInvalid coordinate format.\n")
                continue
            if place[0] not in "abcdefgh":
                print("\nInvalid coordinate format.\n")
                continue
            if place[1] not in "12345678":
                print("\nInvalid coordinate format.\n")
                continue

            if len(temp_black_list) == 16:
                print("\nYou have reached a maximum input of 16 black pieces.\n")
                return temp_black_list

            row, column = b_coordinate_conversion(place, coordinates)

            if board[row][column] != " ":
                print("\nThis square is not empty.\n")
                continue

            if place in used_black_pieces:
                print("\nThis square is not empty.\n")
                continue

            used_black_pieces.add(place)
            temp_black_list.append((piece, place))
            print(f"\n{piece} {place} was added successfully!\n")

        except ValueError:
            print("\nInvalid input format.\n")
            continue


# Converts white piece coordinate to board indices.
def w_coordinate_conversion(coordinates, white_format):
    piece, place = white_format
    column = coordinates[place[0]]
    row = coordinates[place[1]]
    return row, column


# Converts black piece coordinate to board indices.
def b_coordinate_conversion(place, coordinates):
    column = coordinates[place[0]]
    row = coordinates[place[1]]
    return row, column


# Places white piece(its abbreviation) on the board.
def white_input(board, pieces, coordinates, white_format):
    row, column = w_coordinate_conversion(coordinates, white_format)
    piece, place = white_format
    for key, info in pieces.items():
        if info["name"] == piece and info["color"] == "white":
            abbrv = key
            break
    board[row][column] = abbrv
    print("\nWhite piece was added successfully:")
    print(tabulate([white_format], headers=["Piece", "Position"], tablefmt="grid"))
    print()
    return board


# Places white all black pieces on the board (based on the temp list).
def black_input(board, pieces, coordinates, black_format):
    temp_black_list = black_format
    for piece, place in temp_black_list:
        row, column = b_coordinate_conversion(place, coordinates)
        for key, info in pieces.items():
            if info["name"] == piece and info["color"] == "black":
                abbrv = key
                break
        board[row][column] = abbrv
    print("\nBlack pieces were added successfully:")
    print(tabulate(temp_black_list, headers=["Piece", "Position"], tablefmt="grid"))
    print()
    return board


# This function check what black pieces (if any) white piece has captured.
# Then prints the result and the board.
def taking(board, white_format):
    white_piece = ""
    for x, row in enumerate(board):
        for y, abbrv in enumerate(row):
            if abbrv == "wP" or abbrv == "wR":
                white_piece = (x, y)
                break
        if white_piece != "":
            break

    captures = []

    if abbrv == "wP":
        row, column = white_piece
        if row - 1 >= 0 and column - 1 >= 1:
            if board[row - 1][column - 1] != " ":
                captured_piece = board[row - 1][column - 1]
                its_coordinate = board[8][column - 1] + board[row - 1][0]
                captures.append((captured_piece, its_coordinate))
        if row - 1 >= 0 and column + 1 <= 8:
            if board[row - 1][column + 1] != " ":
                captured_piece = board[row - 1][column + 1]
                its_coordinate = board[8][column + 1] + board[row - 1][0]
                captures.append((captured_piece, its_coordinate))

    if abbrv == "wR":
        row, column = white_piece

        up_row = row - 1

        while up_row >= 0:
            if board[up_row][column] != " ":
                captured_piece = board[up_row][column]
                its_coordinate = board[8][column] + board[up_row][0]
                captures.append((captured_piece, its_coordinate))
                break
            else:
                up_row -= 1

        down_row = row + 1

        while down_row < 8:
            if board[down_row][column] != " ":
                captured_piece = board[down_row][column]
                its_coordinate = board[8][column] + board[down_row][0]
                captures.append((captured_piece, its_coordinate))
                break
            else:
                down_row += 1

        left_column = column - 1

        while left_column >= 1:
            if board[row][left_column] != " ":
                captured_piece = board[row][left_column]
                its_coordinate = board[8][left_column] + board[row][0]
                captures.append((captured_piece, its_coordinate))
                break
            else:
                left_column -= 1

        right_column = column + 1

        while right_column <= 8:
            if board[row][right_column] != " ":
                captured_piece = board[row][right_column]
                its_coordinate = board[8][right_column] + board[row][0]
                captures.append((captured_piece, its_coordinate))
                break
            else:
                right_column += 1

    if captures == []:
        print("No pieces were captured!\n")
        print(tabulate(board, tablefmt="grid"))
    else:
        print(f"White piece {white_format} can take these black pieces:")
        print(tabulate(captures, headers=["Captured piece", "Place"], tablefmt="grid"))
        print(tabulate(board, tablefmt="grid"))


if __name__ == "__main__":
    main()

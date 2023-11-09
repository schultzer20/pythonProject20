from collections import deque


def print_labyrinth(lab, path=None):
    # Determine the number of rows and columns in the labyrinth
    rows = len(lab)
    cols = len(lab[0])

    # numbers at the top
    print("", end="")
    for col in range(cols):
        if col == 0:
            print(f"{col:2}", end="")  # right-aligned with space before the number
        else:
            print(f"{col:1}", end="")  # just number, no space
    print()

    for row, row_data in enumerate(lab):
        print(f"{row:1}", end="")  # number on the left
        for col, cell in enumerate(row_data):
            if path and (row, col) in path:
                print("X", end="")  # path marking
            elif cell == ' ':
                print(" ", end="")  # Empty space
            else:
                print("█", end="")  # Character █ for walls
        print(f"{row:2}", end="")  # number on the right
        print()

    # numbers at the bottom
    print("", end="")
    for col in range(cols):
        if col == 0:
            print(f"{col:2}", end="")  # right-aligned with space before the number
        else:
            print(f"{col:1}", end="")  # just number, no space
    print()


def prompt_integer(message: str) -> int:
    while True:
        input_number = input(message)
        while input_number.isdigit():
            return int(input_number)
        print("Please enter a valid number.")


def prompt_user_for_location(name: str) -> tuple:
    print(f"For {name} location")
    row = prompt_integer(f"Row of {name}: ")
    col = prompt_integer(f"Column of {name}: ")
    return (row, col)


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    rows = len(lab)
    cols = len(lab[0])
    row, col = location
    return 0 <= row < rows and 0 <= col < cols and lab[row][col] == " "


#  input: labyrinth + start tuple + end tuple --> return: list of tuples (start tuple, ....., end tuple)
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]):  # -> list[tuple[int, int]]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([deque([start])])  # start path
    v = set()  # all locations visited

    while q:
        path = q.popleft()
        last = path[-1]

        if last == end:
            return list(path)
        if last not in v:
            v.add(last)

            for move in moves:
                next_x, next_y = last[0] + move[0], last[1] + move[1]
                next_location = (next_x, next_y)

                if is_traversable(lab, next_location):
                    new_path = deque(path)
                    new_path.append(next_location)
                    q.append(new_path)


# input labyrinth with spaces and █ for walls
lab = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████",
]

print_labyrinth(lab)
# prompt for 2 tuples
start_location = prompt_user_for_location("start")
print(f"Start location: {start_location}")  # start_location = tuple

end_location = prompt_user_for_location("end")
print(f"End location: {end_location}")  # end_location = tuple

result = bfs(lab, start_location, end_location)
print(result)

print_labyrinth(lab, result)

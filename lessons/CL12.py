"""basic syntax of list"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_name: str = ""  # literal
my_name: str = str()  # constructor

my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94]

game_points.append(102)

game_points.pop(2)

game_points[1] = 72


def display(list: list[int]) -> None:
    idx: int = 0
    while idx < len(list):
        print(list[idx])
        idx += 1


display(list=[1, 2, 3, 4, 5])

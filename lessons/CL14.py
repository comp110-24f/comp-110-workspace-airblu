a: str = "24"
b: str = a
a += "6"
# print(b)

c: list[int] = [2, 4]
d: list[int] = c
c.append(6)
# print(d)


def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


# display([1, 2, 3])


def odds_list(min: int, max: int) -> list[int]:
    "spits out all odds btwn min and max"
    odds: list[int] = []
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    return odds


global_odds: list[int] = odds_list(2, 6)
# print(global_odds)


def remove_first(xs: list[str]):
    xs.pop(0)


course: list[str] = ["Comp", "110"]
remove_first(course)
# print(course)

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
# print(y)


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1


def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


msg: list[str] = ["Hello", "World"]
print(msg)
view(msg)
print(msg)

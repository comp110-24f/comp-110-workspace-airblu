def jump(x: int) -> int:
    if x == 1:
        x = around(x - 2)
    print("jump")
    return x + 1


def around(x: int) -> int:
    while x > 0:
        return jump(x - 1)
    print("around")
    return 109


print(around(2))

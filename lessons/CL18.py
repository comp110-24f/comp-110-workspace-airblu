"""exchange: dict[str, float] = {"CNY": 7.10, "GBP": 0.77, "DKK": 6.86}


ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}  # trailing comma helps read alledgedly, help when adding to list alledgedly

print(len(ice_cream))

ice_cream["mint"] = 10

mint_orders: int = ice_cream["mint"]
print(mint_orders)

ice_cream.pop("strawberry")

my_dict: dict[int, str] = {8: "dog", 1: "cat", 10: "mouse", 15: "bird", 0: "whale"}

for x in range(0, len(my_dict)):
    print(my_dict[x])"""


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)

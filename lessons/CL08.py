"""def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    else:
        if num % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
    return num"""

# number_info(num=11)
# print(number_info(num=4))

"""def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    elif num % 2 == 0: # Better use of memory
            print("Even number.")
    else:
            print("Odd number.")
    return num"""


"""def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()"""


def get_ticket_priceB() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price


def get_ticket_priceC() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_priceB())
print(get_ticket_priceC())

print(str(3))
print(str(3))


def sum(num1: int, num2: int) -> int:
    """adds two arguments together"""
    return num1 + num2


print(sum(num1=3, num2=4))


def celsius_to_fahrenheit(degrees_c: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees_c * 9 / 5) + 32


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


x: int = 1


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price


def get_weather_report() -> str:
    weather: str = str(input("What is the weather?"))
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())


print(contains_char(input_letter(), input_word())) # type:ignore
number_instances: int = int() # type: ignore
if input_word[0] == input_letter # type: ignore
        number_instances == 1:  # type: ignore

def contains_char(input_letter, input_word) -> None:
    print("Searching for " + str(input_letter) + " in " + str(input_word))
    count: int = 0
    if input_word[0] == input_letter:
        count = count + 1
        print(str(input_letter) + " found at Index 0")
    elif input_word[1] == input_letter:
        count = count + 1
        print(str(input_letter) + " found at Index 1")
    elif input_word[2] == input_letter:
        count = count + 1
        print(str(input_letter) + " found at Index 2")
    elif input_word[3] == input_letter:
        count = count + 1
        print(str(input_letter) + " found at Index 3")
    elif input_word[4] == input_letter:
        count = count + 1
        print(str(input_letter) + " found at Index 4")
    else:
        print("Error: Character must be a single character.")
    return count 

print(contains_char(input_letter(), input_word()))
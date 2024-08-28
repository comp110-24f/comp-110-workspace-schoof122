print(str(3))
print(str(3))


def sum(num1: int, num2: int) -> int:
    """adds two arguments together"""
    return num1 + num2


print(sum(num1=3, num2=4))


def celsius_to_fahrenheit(degrees_c: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees_c * 9 / 5) + 32

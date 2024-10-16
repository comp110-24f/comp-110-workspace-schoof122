my_numbers: list[float] = list()
print(my_numbers)
my_numbers.append(1.5)
print(my_numbers)


game_points: list[int] = [102, 86, 94]
game_points[1] = 72
game_points.append(72)
print(game_points)


x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(y)
print(x)


pet_names: list[str] = ["Louie", "Bo", "Bear"]
for pet in pet_names:
    print("Good boy, " + (pet) + ("!"))


def get_name(n: str) -> str:
    return n

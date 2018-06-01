snake = "*"

while len(snake) > 0:
    print(snake)
    char = str(input(""))
    if char == "+":
        snake +="*"
    if char == "-":
        snake = snake[:-1]

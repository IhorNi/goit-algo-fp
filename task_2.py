import turtle
import math


def draw_pythagoras_tree(branch_length, level, angle=45):
    if level == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(angle)
        new_length = branch_length / math.sqrt(2)  # Explicit calculation
        draw_pythagoras_tree(new_length, level - 1, angle)
        turtle.right(angle * 2)
        draw_pythagoras_tree(new_length, level - 1, angle)
        turtle.left(angle)
        turtle.backward(branch_length)


def main():
    waiting_for_input = True
    while waiting_for_input:
        try:
            recursion_level = int(input("Введіть рівень рекурсії (1-9): "))
            if 1 <= recursion_level <= 9:
                waiting_for_input = False
            else:
                print("Для цілей прикладу рівень рекурсії має бути в межах від 1 до 9.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")
    turtle.speed('fastest')
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()
    turtle.left(90)
    draw_pythagoras_tree(150, recursion_level)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()

import turtle


def draw_pythagorean_tree(t, length, angle, depth):
    if depth == 0:
        return
    t.forward(length * depth)
    t.left(angle)
    draw_pythagorean_tree(t, length, angle, depth-1)
    t.right(2 * angle)
    draw_pythagorean_tree(t, length, angle, depth-1)
    t.left(angle)
    t.backward(length * depth)


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(0, -200)
t.pendown()
t.left(90)

depth = int(
    input("Enter the recursion depth: "))

draw_pythagorean_tree(t, 10, 45, depth)

t.hideturtle()
screen.mainloop()

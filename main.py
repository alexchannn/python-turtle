import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Chaos Theory - Fractal Tree")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.color("white")
t.penup()
t.setpos(0, -300)
t.setheading(90)
t.pendown()

def draw_fractal_tree(branch_length, angle):
    if branch_length < 2:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        draw_fractal_tree(branch_length * 0.7, angle)
        t.left(angle * 2)
        draw_fractal_tree(branch_length * 0.7, angle)
        t.right(angle)
        t.backward(branch_length)

draw_fractal_tree(200, 30)

turtle.done()

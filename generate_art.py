import turtle
import random

def main():
    window = turtle.Screen()
    window.setup(width=800, height=600, startx=10, starty=0.5)
    window.colormode(255)

    joe = turtle.Turtle()
    joe.shape("turtle")

    recaman(joe)

    turtle.done()

def recaman(turt):
    scale = 2  # This isn't a turtle module setting.  This is just for us.

    # Move the little buddy over to the left side to give him more room to work
    turt.penup()
    turt.setpos(-390, 0)
    turt.pendown()
    turt.speed(0)

    current = 0
    iterations = set()

    r = 255
    g = 0
    b = 0
    for step in range(1,256):

        #Change color of pen
        if b <= 0
            if g <= 255 and r >= 255:
                g += 3
            else:
                pass

            elif r <= 0 and g >= 255:
                b += 3
            else:
                pass

        if g >= 255 and b >= 255:
            g -= 3
        else:
            pass

        if g <= 0 and b >=255:
            r += 3
        else:
            pass

        if r >= 255 and b >= 255:
            b -= 3
        else:
            pass

        if r <= 0 and b >= 255:


        elif 
        turt.pencolor((r,g,b))
        print(turt.pencolor())

        backward = current - step

        if backward > 0 and backward not in iterations:
            turt.setheading(90)
            turt.circle(scale * step/2, 180)
            current = backward
            iterations.add(current)
        else:
            turt.setheading(270)
            turt.circle(scale * step/2, 180)
            current += step
            iterations.add(current)


if __name__ == "__main__":
    main()
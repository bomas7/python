import turtle
import time


class Turtle(turtle.Turtle):

    def a(self, size):
        self.left(90)
        self.circle(-size/4, 180)
        self.forward(size*.9)
        self.sety(self.ycor()+size/10)
        self.right(90)
        self.forward(size/4)
        self.circle(-size/4, 180)
        self.forward(size/4)
        

if __name__ == '__main__':
    tester = Turtle()
    tester.a()
    time.sleep(2)

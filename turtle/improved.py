import turtle

class Turtle(turtle.Turtle):

    def a(self):
        self.circle(-10, 90)
        self.forward(20)
        self.circle(-10, 360)

if __name__ == '__main__':
tester = Turtle()
tester.a()
delay = input('')

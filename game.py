from turtle import *


class Sprite(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.ht()
        self.shape('turtle')
        self.penup()
        self.color(color)
        self.goto(x, y)
        self.st()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)
        self.telep()
        if not self.check():
            self.goto(self.xcor(), self.ycor() - 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)
        self.telep()
        if not self.check():
            self.goto(self.xcor(), self.ycor() + 10)

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())
        self.telep()
        if not self.check():
            self.goto(self.xcor() - 10, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())
        self.telep()
        if not self.check():
            self.goto(self.xcor() + 10, self.ycor())

    def check(self):
        global wall_cors
        for cors in wall_cors:
            wall_x, wall_y = cors
            if abs(self.xcor() - wall_x) < 5 and abs(self.ycor() - wall_y) < 5:
                return False
        if self.xcor() == -230 and self.ycor() == -210:
            self.win()
        return True

    def win(self):
        self.write('Победа!!!', font=('Verdana', 14, 'normal'))
        done()
        exit()

    def is_close(self, enemy):
        if self.distance(enemy) < 5:
            self.write('Проигрыш!', font=('Verdana', 14, 'normal'))
            done()
            exit()

    def telep(self):
        if self.xcor() == -190 and self.ycor() == -90:
            self.ht()
            self.goto(-100, -210)
            self.st()
        if self.xcor() == 100 and self.ycor() == -60:
            self.ht()
            self.goto(-100, -210)
            self.st()


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.pensize(10)
        self.penup()
        self.speed(20)

    def move_gor(self, x, y, step):
        self.goto(x, y)
        self.pendown()
        self.fd(step)
        self.penup()

    def move_ver(self, x, y, step):
        self.goto(x, y)
        self.pendown()
        self.left(90)
        self.fd(step)
        self.penup()
        self.right(90)


class Enemies(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('classic')
        self.color('maroon')
        self.penup()
        self.ht()
        self.goto(x, y)
        self.st()

    def move1(self, x, y, x_step, y_step):
        self.goto(x + x_step, y + y_step)

    def is_close(self, t):
        if self.distance(t) < 10:
            t.write('Проигрыш!', font=('Verdana', 14, 'normal'))
            done()
            exit()


class Teleport(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.penup()
        self.shape('circle')
        self.color(color)
        self.goto(x, y)
        self.st()


wall = Walls()
bgcolor('dark sea green')

walls = {1: (200, 240, -470), 2: (270, 240, -480),
         3: (162, 180, -378), 4: (-270, 240, -480),
         5: (-216, 120, 108), 6: (-216, 180, -300),
         7: (-54, 120, 54), 8: (-108, 120, -240),
         9: (-108, 60, 54), 10: (0, 120, -120),
         11: (54, 60, 54), 12: (54, 180, -120),
         13: (108, 120, 108), 14: (162, 120, -120),
         15: (162, 60, 54), 16: (54, 0, -240),
         17: (-54, 0, 216), 18: (-54, 0, -60),
         19: (216, 0, 54), 20: (-162, 60, -180),
         21: (162, -60, 54), 22: (0, -60, -60),
         23: (0, -120, 162), 24: (216, -60, -120),
         25: (-216, -120, 54), 26: (-54, -120, -60),
         27: (-108, -120, 54), 29: (-270, -180, 270),
         31: (108, -180, 54), 33: (-270, -240, 540)}

wall_cors = []

for key, value in walls.items():
    x, y, step = value
    if key % 2 != 0:
        wall.move_gor(x, y, step)
        if step < 0:
            for i in range(x, x + step - 1, -1):
                wall_cors.append((i, y))
        else:
            for i in range(x, x + step + 1):
                wall_cors.append((i, y))
    else:
        wall.move_ver(x, y, step)
        for i in range(y, y + step - 1, -1):
            wall_cors.append((x, i))
wall_cors = tuple(wall_cors)

player = Sprite('sea green', 230, 210)
player.left(180)

enemy1 = Enemies(-120, 150)
enemy2 = Enemies(250, 20)
enemy3 = Enemies(-230, -150)

end_player = Sprite('dark green', -230, -210)
end_player.left(180)

t1 = Teleport(-190, -90, 'cornflower blue')
t2 = Teleport(100, -60, 'cornflower blue')
t3 = Teleport(-100, -210, 'light pink')

scr = player.getscreen()

scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_left, 'Left')

while True:
    while enemy1.xcor() < 180 and enemy2.ycor() < 190 and enemy3.xcor() < 50:
        enemy1.move1(enemy1.xcor(), 150, 3, 0)
        enemy1.is_close(player)

        enemy2.move1(250, enemy2.ycor(), 0, 3)
        enemy2.is_close(player)

        enemy3.move1(enemy3.xcor(), -150, 3, 0)
        enemy3.is_close(player)
    while enemy1.xcor() > -120 and enemy2.ycor() > 20 and enemy3.xcor() > -210:
        enemy1.move1(enemy1.xcor(), 150, -3, 0)
        enemy1.is_close(player)

        enemy2.move1(250, enemy2.ycor(), 0, -3)
        enemy2.is_close(player)

        enemy3.move1(enemy3.xcor(), -150, -3, 0)
        enemy3.is_close(player)


from tkinter import *
import random

WIDTH = 500
HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_SIZE = 2

class snake_game():
    class body():
        def __init__(self):
            self.coordinates = []
            self.squares = []
        def create(self,BODY_SIZE, SPACE_SIZE, canvas):

            for i in range(0, BODY_SIZE):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                        fill="#002FFF", tag="snake")
                self.squares.append(square)
            return canvas

    class apple():
        def __init__(self):
            self.coordinates = NONE
        def generate(self, WIDTH, SPACE_SIZE, HEIGHT, canvas):
            x = random.randint(0, 
                    int((WIDTH / SPACE_SIZE)-1)) * SPACE_SIZE
            y = random.randint(0, 
                    int((HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y +
                            SPACE_SIZE, fill="#FFFFFF", tag="food")
            return canvas


    def __init__(self, width=500, height=500, speed=100, space=20, body=2):

        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = speed
        self.SPACE_SIZE = space
        self.BODY_SIZE = body
        self.SNAKE = self.body()
        self.FRUIT = self.apple()
        self.direction = "down"
        self.score = 0

    def run_game(self):
        windows = Tk()
        windows.title("snake game with AI")

        label = Label(windows, text="Points:{}".format(self.score), 
                    font=('consolas', 20))
        label.pack()
        canvas = Canvas(windows, bg="#000000", 
                height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()
        windows.update()

        window_width = windows.winfo_width()
        window_height = windows.winfo_height()
        screen_width = windows.winfo_screenwidth()
        screen_height = windows.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        windows.geometry(f"{window_width}x{window_height}+{x}+{y}")

        windows.bind('<Left>', 
                    lambda event: self.change_directions('left'))
        windows.bind('<Right>', 
                    lambda event: self.change_directions('right'))
        windows.bind('<Up>', 
                    lambda event: self.change_directions('up'))
        windows.bind('<Down>', 
                    lambda event:self.change_directions('down'))
        
        canvas = self.SNAKE.create(self.BODY_SIZE, self.SPACE_SIZE, canvas)
        canvas = self.FRUIT.generate(self.WIDTH, self.SPACE_SIZE, self.HEIGHT, canvas)

        self.tick(label, canvas, windows)
        windows.mainloop()

    def tick(self, label, canvas, windows):
        x, y = self.SNAKE.coordinates[0]
        print(x,y)
        if self.direction == "up":
            y -= self.SPACE_SIZE
        elif self.direction == "down":
            y += self.SPACE_SIZE
        elif self.direction == "left":
            x -= self.SPACE_SIZE
        elif self.direction == "right":
            x += self.SPACE_SIZE
        self.SNAKE.coordinates.insert(0, (x,y))
        square = canvas.create_rectangle(x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, fill="#002FFF")
        self.SNAKE.squares.insert(0, square)
        if x == self.FRUIT.coordinates[0] and y == self.FRUIT.coordinates[1]:
            self.score += 1
            label.config(text="Points:{}".format(self.score))
            canvas.delete("food")
            canvas = self.FRUIT.generate(self.WIDTH, self.SPACE_SIZE, self.HEIGHT, canvas)
        else:
            del self.SNAKE.coordinates[-1]
            canvas.delete(self.SNAKE.squares[-1])
            del self.SNAKE.squares[-1]
        if self.collision():
            canvas.delete(ALL)
            canvas.create_text(canvas.winfo_width()/2, 
                                canvas.winfo_height()/2,
                                font=('consolas', 70), 
                                text="GAME OVER", fill="red", 
                                tag="gameover")
        else:
            windows.after(self.SPEED, self.tick(label, canvas, windows))

    def collision(self):
        
        x, y = self.SNAKE.coordinates[0]
        if x < 0 or x >= self.WIDTH:
            return True
        elif y < 0 or y >= self.HEIGHT:
            return True
        for part in self.SNAKE.coordinates[1:]:
            if x == part[0] and y == part[1]:
                return True
        return False

    def change_directions(self, new_direction):
        
        if new_direction == 'left':
            if self.direction != 'right':
                self.direction = new_direction
        elif new_direction == 'right':
            if self.direction != 'left':
                self.direction = new_direction
        elif new_direction == 'up':
            if self.direction != 'down':
                self.direction = new_direction
        elif new_direction == 'down':
            if self.direction != 'up':
                self.direction = new_direction


game = snake_game()
game.run_game()
import pygame
import time
import random

class snake_game():

    def __init__(self):
        self.snake_speed = 15
        self.window_x = 250
        self.window_y = 250

        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        # self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10,  random.randrange(1, (self.window_y//10)) * 10]
        self.fruit_position = [150,150]
        self.direction = "RIGHT"
        self.change_to = "RIGHT"

        pygame.init()
        pygame.display.set_caption('Snakes Game')
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

        self.score = 0
        self.run = True
    
    def show_score(self):
            
        score_font = pygame.font.SysFont("times new roman", 20)
        score_surface = score_font.render('Score : ' + str(self.score), True, self.white)
        score_rect = score_surface.get_rect()

        self.game_window.blit(score_surface, score_rect)

    def game_over(self):

        _font = pygame.font.SysFont('times new roman', 50)
        _surface = _font.render('Your Score is : ' + str(self.score), True, self.red)
        _rect = _surface.get_rect()
        _rect.midtop = (self.window_x/2, self.window_y/4)
        self.game_window.blit(_surface, _rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        self.run = False
        # quit()

    def run_loop(self):
        fruit_spawn = True
        while self.run :
            
            # print(self.snake_position, self.snake_body)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        self.change_to = 'RIGHT'


            if self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

            # Moving the snake
            if self.direction == 'UP':
                self.snake_position[1] -= 10
            if self.direction == 'DOWN':
                self.snake_position[1] += 10
            if self.direction == 'LEFT':
                self.snake_position[0] -= 10
            if self.direction == 'RIGHT':
                self.snake_position[0] += 10

            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            self.snake_body.insert(0, list(self.snake_position))
            if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
                self.score += 10
                fruit_spawn = False
            else:
                self.snake_body.pop()
                
            if not fruit_spawn:
                self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, 
                                random.randrange(1, (self.window_y//10)) * 10]
                while(self.fruit_position in self.snake_body):
                    self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, 
                                random.randrange(1, (self.window_y//10)) * 10]
                
            fruit_spawn = True
            self.game_window.fill(self.black)
            
            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, self.green,
                                pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.game_window, self.blue, pygame.Rect(
                self.fruit_position[0], self.fruit_position[1], 10, 10))

            # Game Over conditions
            if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x-10:
                self.game_over()
            if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y-10:
                self.game_over()

            # Touching the snake body
            for block in self.snake_body[1:]:
                if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                    self.game_over()
            
            if(not self.run):
                break

            # displaying score continuously
            self.show_score()

            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.fps.tick(self.snake_speed)

if __name__ == "__main__":
    sg = snake_game()
    sg.run_loop()
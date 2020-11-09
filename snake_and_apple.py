import pygame
from pygame.locals import *  # Import all the event types used for operating the program. Eg, QUIT,KEYDOWN,etc.
import time  # Import time module so that the snake keeps on moving
import random  # Imported to generate a Random number for the positions of apple.

size = 40
BG_color = (52, 235, 195)


class Apple:  # Class for Snake's Apple

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("C:/Program Files/resources/apple.jpg").convert()
        self.x = size * 3
        self.y = size * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 11) * size
        self.y = random.randint(1, 11) * size


class Snake:  # Class for our snake

    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(
            "C:/Program Files/resources/block.jpg").convert()  # Loads our img in block variable.
        self.length = length
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'up'

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):  # Increase the length of snake on eating apple.
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'up':
            self.y[0] -= size
        elif self.direction == 'down':
            self.y[0] += size
        elif self.direction == 'left':
            self.x[0] -= size
        elif self.direction == 'right':
            self.x[0] += size
        self.draw()


class Game:  # This is our game class

    def __init__(self):  # Constructor
        pygame.init()  # Initializes the pygame module.
        pygame.mixer.init()  # Initialise the mixer library to enter music.
        self.play_background_music()  # Plays background music.
        self.surface = pygame.display.set_mode((500, 500))  # Creates a screen of dimensions 500X500.
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial', 15)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (400, 10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 15)
        message = font.render(f"Game Over! Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(message, (175, 200))
        message2 = font.render(f"Press Enter to play again", True, (255, 255, 255))
        self.surface.blit(message2, (175, 150))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def reset(self):  # Reset on losing
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        self.play_background_music()

    def render_background(self):
        bg = pygame.image.load("C:/Program Files/resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play_background_music(self):
        pygame.mixer.music.load("C:/Program Files/resources/bg_music_1.mp3")  # Load the BG music
        pygame.mixer.music.play(-1, 0)  # -1 means music will always be played and 0 means it'll be played from start.

    def play_sound(self, sound):  # Play ding on eating apple and crash on losing.
        if sound == 'ding':
            sound = pygame.mixer.Sound("C:/Program Files/resources/ding.mp3")
        elif sound == 'crash':
            sound = pygame.mixer.Sound("C:/Program Files/resources/crash.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):  # Defines the Gameplay
        self.render_background()
        self.display_score()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        # Snake colliding with Apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
        # Snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise Exception("Game Over")

    def is_collision(self, x1, y1, x2, y2):  # Outcomes when snake collides with 1) Apple 2) Itself
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def run(self):  # Class method
        running = True  # Create a boolean variable. Our window will keep on running until this bool variable is false.
        pause = False
        while running:  # Our loop will run till the time running is True.
            for event in pygame.event.get():  # running a for loop to chose when our program terminates
                if event.type == KEYDOWN:  # If we press any then the following statements/cond will be executed
                    if event.key == K_ESCAPE:  # If we press thr ESC key our window will go off
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:  # If we press the 'UP' key block will move down by 10 px
                            self.snake.move_up()
                        if event.key == K_DOWN:  # If we press the 'DOWN' key our block moves down by 10 px
                            self.snake.move_down()
                        if event.key == K_LEFT:  # If we press the 'LEFT' key the block moves left by 10 px
                            self.snake.move_left()
                        if event.key == K_RIGHT:  # If we press the 'RIGHT' key the block moves right by 10 px
                            self.snake.move_right()
                elif event.type == QUIT:  # If we press the 'X' sign our window will terminate.
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(.2)


if __name__ == "__main__":
    game = Game()
    game.run()

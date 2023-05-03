import pygame
from random import randint
from enum import Enum
from collections import namedtuple

# general config
BLOCK_SIZE = 20
SPEED = 10

# RGB colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
PURPLE1 = (40,20,71)
PURPLE2 = (136,68,238)
BLACK = (0, 0, 0)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

pygame.init()
font = pygame.font.SysFont('arial', 25)

class SnakeGame:
    
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        
        # init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # init game  state
        self.direction = Direction.RIGHT

        self.head = Point(self.width/2, self.height/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = randint(0, (self.width-BLOCK_SIZE )// BLOCK_SIZE)*BLOCK_SIZE
        y = randint(0, (self.height-BLOCK_SIZE )// BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self):
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
            
        # move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head)

        # chekc if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        
        # place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        # update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # return game over and score
        return game_over, self.score
    
    def _is_collision(self):
        # hits bounddary
        if self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.height - BLOCK_SIZE or self.head.y < 0:
            
            return True
        
        # hit itself
        if self.head in self.snake[1:]:
            
            return True
        
        return False
    
    def _update_ui(self):
        self.display.fill(BLACK)

        # painting snake
        for point in self.snake:
            pygame.draw.rect(self.display, PURPLE1, pygame.Rect(point.x, point.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, PURPLE2, pygame.Rect(point.x+4, point.y+4, 12, 12))

        # painting food
        pygame.draw.rect(self.display, BLUE, (self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f"Score: {self.score}", True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
    
    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE        

        self.head = Point(x, y)

if __name__ == '__main__':
    game = SnakeGame()

    # game loop
    while True:
        game_over, score = game.play_step()

        if game_over:
            break
    
    print(f'Final Score {score}')

    pygame.quit()
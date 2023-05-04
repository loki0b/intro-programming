import pygame
from random import randint
from enum import Enum
from collections import namedtuple
import numpy as np

# general config
BLOCK_SIZE = 20
SPEED = 50

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

class SnakeGameAI:
    
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        
        # init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        # init game  state
        self.direction = Direction.RIGHT

        self.head = Point(self.width/2, self.height/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0


    def _place_food(self):
        x = randint(0, (self.width-BLOCK_SIZE )// BLOCK_SIZE)*BLOCK_SIZE
        y = randint(0, (self.height-BLOCK_SIZE )// BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self, action):
        self.frame_iteration += 1
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        # move
        self._move(action) # update the head
        self.snake.insert(0, self.head)

        # chekc if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score 
        
        # place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        # update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # return game over and score
        return reward, game_over, self.score
    

    def is_collision(self, point=None):
        if point is None:
            point = self.head
        # hits bounddary
        if point.x > self.width - BLOCK_SIZE or point.x < 0 or point.y > self.height - BLOCK_SIZE or point.y < 0:
            
            return True
        
        # hit itself
        if point in self.snake[1:]:
            
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
    

    def _move(self, action):
        # [straight, right, left]
        
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        index = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_direction = clock_wise[index] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (index + 1) % 4
            new_direction = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (index - 1) % 4
            new_direction = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_direction

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE        

        self.head = Point(x, y)

import pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen,):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('///home/gulkayir/Pictures/redd.jpg').convert()
        self.x = 0,1
        self.y = 0,1

    def draw(self):
        self.surface.fill((104,130,213))
        self.surface.blit(block,(block_x,block_y))
        pygame.display.flip()

        self.parent_screen.blit(self.block,(self.x,self.y))

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((104,130,213))
        self.snake = Snake(self.surface)
        self.snake.draw()
    
    def run(self):
        pass





if __name__ == '__main__':
    game = Game()
    game.run()

    
    
    surface.blit(block,(block_x,block_y))

    pygame.display.flip()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            
            elif event.type == QUIT:
                running = False


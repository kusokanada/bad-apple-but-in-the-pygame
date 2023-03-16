#このファイルでインポートを使用します。
import pygame, sys
from pygame.locals import *
windowHeight = 600
windowWidth = 900

def main():
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Test')
    background = pygame.image.load('background.jpg')
    screen.blit(background, (0,0))
    face = pygame.image.load('text.gif')
    b = screen.blit(face, (300, 300))

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if b.collidepoint(x, y):
                    face = pygame.image.load('background.jpg')
                    b = screen.blit(face, (300, 300))
                else: 
                    face = face = pygame.image.load('text.gif')
                    b = screen.blit(face, (300, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if b.collidepoint(x, y):
                    print("button has been clicked")

        pygame.display.update()

if __name__ == '__main__': 
    main()
import pygame
import sys

pygame.init()

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prikaz slike")

image_path = r"assets\MainMenu.png"
try:
    background = pygame.image.load(image_path)
except pygame.error as e:
    print(f"Ne mogu da učitam sliku: {e}")
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()

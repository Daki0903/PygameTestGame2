import pygame
import sys

pygame.init()

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

image_path = r"assets\MainMenu.png"
try:
    background = pygame.image.load(image_path)
except pygame.error as e:
    print(f"Cannot load image: {e}")
    pygame.quit()
    sys.exit()

font = pygame.font.SysFont("arial", 40)
small_font = pygame.font.SysFont("arial", 30)

def show_credits():
    screen.fill((0, 0, 0))
    text1 = font.render("Made by Daki0903", True, (255, 255, 255))
    text2 = small_font.render("Collaborator: JohanLiebert363", True, (255, 255, 255))
    screen.blit(text1, (screen_width // 2 - text1.get_width() // 2, 400))
    screen.blit(text2, (screen_width // 2 - text2.get_width() // 2, 460))
    pygame.display.flip()
    pygame.time.wait(3000)

def start_game():
    screen.fill((50, 50, 50))
    text = font.render("Game Started", True, (0, 255, 0))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

running = True
on_menu = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game()
            elif event.key == pygame.K_c:
                show_credits()

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()

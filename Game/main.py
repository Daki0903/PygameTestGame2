import pygame
import sys

pygame.init()

screen_width, screen_height = 1000, 800
if screen_width > 1600 or screen_height > 1200:
    raise ValueError("Width and height must be less than 1600 and 1200, respectively.")

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

image_path = r"Web\MainMenu.png"
try:
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (screen_width, screen_height))
except pygame.error as e:
    print(f"Cannot load image: {e}")
    pygame.quit()
    sys.exit()

font = pygame.font.SysFont("arial", 40)
small_font = pygame.font.SysFont("arial", 30)

def show_credits():
    screen.fill((0, 0, 0))
    text1 = font.render("Made by Daki0903", True, (255, 255, 255))
    text2 = font.render("Collaborator: JohanLiebert363", True, (255, 255, 255))
    screen.blit(text1, (screen_width // 2 - text1.get_width() // 2, 400))
    screen.blit(text2, (screen_width // 2 - text2.get_width() // 2, 460))
    pygame.display.flip()
    pygame.time.wait(3000)
    
def show_options():
    global screen_width, screen_height, screen, background  # Move this to the top!
    in_options = True
    while in_options:
        screen.fill((0, 0, 0))
        text = font.render("Options Menu", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - 60))
        option1 = small_font.render("1: Change Resolution", True, (255, 255, 255))
        option2 = small_font.render("2: Change Volume", True, (255, 255, 255))
        exit_text = small_font.render("ESC: Back to Menu", True, (255, 255, 255))
        screen.blit(option1, (screen_width // 2 - option1.get_width() // 2, screen_height // 2))
        screen.blit(option2, (screen_width // 2 - option2.get_width() // 2, screen_height // 2 + 40))
        screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, screen_height // 2 + 80))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_options = False
                elif event.key == pygame.K_1:
                    # Change resolution example
                    screen_width, screen_height = 1280, 720
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    background = pygame.transform.scale(background, (screen_width, screen_height))
                elif event.key == pygame.K_2:
                    print("Volume changed (placeholder)")   


            elif event.key == pygame.K_ESCAPE:
                on_menu = not on_menu

    if on_menu:
        screen.blit(background, (0, 0))
        title = font.render("Main Menu", True, (255, 255, 255))
        start_text = small_font.render("Press Enter to Start", True, (255, 255, 255))
        credits_text = small_font.render("Press C for Credits", True, (255, 255, 255))
        options_text = small_font.render("Press O for Options", True, (255, 255, 255))
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 200))
        screen.blit(credits_text, (screen_width // 2 - credits_text.get_width() // 2, 250))
        screen.blit(options_text, (screen_width // 2 - options_text.get_width() // 2, 300))

    pygame.display.flip()

running = True
on_menu = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if on_menu:
                if event.key == pygame.K_RETURN:
                    # Start game logic here
                    pass
                elif event.key == pygame.K_c:
                    show_credits()
                elif event.key == pygame.K_o:
                    show_options()
            if event.key == pygame.K_ESCAPE:
                running = False

    if on_menu:
        screen.blit(background, (0, 0))
        title = font.render("Main Menu", True, (255, 255, 255))
        


    pygame.display.flip()

pygame.quit()

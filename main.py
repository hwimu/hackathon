import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

FPS = 60

SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("pygame test")

clock = pygame.time.Clock()
running = True

class scene_title :
    def __init__(self):
        SCREEN.fill((30,30,30))

    def handle_event(self, event):
        pass

    def draw(self):
        pass

current_screen = scene_title()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        new_screen = current_screen.handle_event(event)
        if new_screen:
            current_screen = new_screen

        current_screen.draw()

    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.update
pygame.quit()

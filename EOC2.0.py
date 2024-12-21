import pygame
pygame.init()


screen_width, screen_height = 950, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Emu Otori Clicker")


emuherself = pygame.image.load("Images\other\emu.png") 



button_rect = emuherself.get_rect(center=(screen_width // 2, screen_height // 2))


PINK = (255, 192, 203)


button_pressed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_pressed = True


        if event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False

    screen.fill(PINK)

    if button_pressed:
        pressed_rect = button_rect.move(3, 3) 
        screen.blit(emuherself, pressed_rect.topleft)
    else:
        # Draw the normal button
        screen.blit(emuherself, button_rect.topleft)

    # Update display
    pygame.display.flip()

pygame.quit()
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the size of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the caption of the screen
pygame.display.set_caption("Dashboard")

# Set the font for the text
font = pygame.font.Font(None, 25)

# Create the text for the buttons
button1_text = font.render("Button 1", True, WHITE)
button2_text = font.render("Button 2", True, WHITE)

# Set the positions for the buttons and text
button1_rect = pygame.Rect(50, 50, 100, 50)
button2_rect = pygame.Rect(50, 150, 100, 50)
button1_text_rect = button1_text.get_rect(center=button1_rect.center)
button2_text_rect = button2_text.get_rect(center=button2_rect.center)

# Create the circle for the status indicator
circle_radius = 25
circle_center = (500, 75)
circle_color = GREEN

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on button 1 or button 2
            if button1_rect.collidepoint(event.pos):
                circle_color = GREEN
            elif button2_rect.collidepoint(event.pos):
                circle_color = RED

    # Fill the background with black
    screen.fill(BLACK)

    # Draw the buttons
    pygame.draw.rect(screen, WHITE, button1_rect)
    pygame.draw.rect(screen, WHITE, button2_rect)
    screen.blit(button1_text, button1_text_rect)
    screen.blit(button2_text, button2_text_rect)

    # Draw the status indicator
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


#importing module  
import pypyodbc  
import pygame
import sys # for exiting 
from pygame.locals import *

#creating connection Object which will contain SQL Server Connection  
# connection = pypyodbc.connect('Driver={SQL Server};Server=cypress.csil.sfu.ca;Database=vrc1354;uid=vrc1;pwd=66Q6afF6eag7A7fd')  
  
#print("Connection Successfully Established")  
#closing connection  
#connection.close()
#----------------------------
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CMPT354 Assignment 7 Database Application")

# Basic colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)
RED = (215,120,0)
LIGHT_BLUE = (100, 100, 255)


# Fonts
font = pygame.font.Font(None, 32)

# Button attributes
button_color = BLUE
button_hover_color = LIGHT_BLUE
button_rect = pygame.Rect(300, 250, 200, 80)  # (x, y, width, height)

# GUI functions
def display_text(text, position, font, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_button(rect, text, font, color=WHITE, bg=GRAY):
    pygame.draw.rect(screen,bg,rect)
    display_text(text, (rect.x + 10, rect.y + 5), font, color)

def draw_input_box(rect, active, text, font):
    color = BLUE if active else GRAY
    pygame.draw.rect(screen, color, rect, 2)
    display_text(text, (rect.x + 5, rect.y + 5), font)


# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("button clicked")
    #mouse pos
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        current_button_color = button_hover_color
    else:
        current_button_color = button_color

    screen.fill(WHITE)
    pygame.draw.rect(screen, current_button_color, button_rect)
    # Render button text
    text_surface = font.render("button_text", True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()

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
BLACK = (0, 0, 0) #black
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)
RED = (215,120,0)
LIGHT_BLUE = (100, 100, 255)

# Fonts
font = pygame.font.Font(None, 32)

# Screen properties
screen_rect = screen.get_rect()
center_of_screen = screen_rect.center


# Button attributes
BUTTON_COLOUR = BLUE
BUTTON_HOVER_COLOUR = LIGHT_BLUE
button_rect = pygame.Rect(300, 250, 200, 80)  # (x, y, width, height)

# Menu -----------------------------
# Login Objects
login_button = pygame.Rect(center_of_screen, 250, 100, 50)
login_button.x = center_of_screen + 155
user_id_field = pygame.Rect(center_of_screen, 250, 200, 50)
user_id_field.x = center_of_screen - 200

# Business Objects
business_search_button = pygame.Rect(300, 250, 200, 80)
business_search_field = pygame.Rect(300, 250, 200, 80)


# User Objects 

# ----------------------------------


# GUI functions
def display_text(text, position, font, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_button(rect, text, font, font_color=BLACK, button_color=BUTTON_COLOUR):
    pygame.draw.rect(screen,button_color,rect)
    display_text(text, (rect.x + 10, rect.y + 5), font, font_color)

def display_input_box(rect, active, text, font):
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
        current_button_color = BUTTON_HOVER_COLOUR
    else:
        current_button_color = BUTTON_COLOUR

    screen.fill(WHITE)

    #display_button(button_rect, "test", font, BLACK, current_button_color) # test button
    display_button(login_button, "login", font, BLACK, current_button_color)
    display_input_box(user_id_field, active=True, text="Enter ID", font=font)
    
    # Render button text
    # text_surface = font.render("button_text", True, BLACK)
    # text_rect = text_surface.get_rect(center=button_rect.center)
    # screen.blit(text_surface, text_rect)
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
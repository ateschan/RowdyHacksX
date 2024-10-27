
import pygame

screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)


def fluxCapacitor():

    

    pygame.draw.rect(screen, "red", 
    pygame.Rect(screen.get_width()/2 - 155, 350, 
    50, 175), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    rightTube = pygame.draw.rect(screen, "green", 
    pygame.Rect(screen.get_width()/2 + 135, 350, 
    50, 175), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)


    
    pygame.draw.rect(screen, "yellow", 
    pygame.Rect(screen.get_width()/2 - 15, 525, 
    50, 175), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)
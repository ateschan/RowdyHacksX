
import pygame

screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)


def fluxCapacitor():
    pygame.draw.rect(screen, "black", 
    pygame.Rect(screen.get_width()/2 - 50, 260, 
    20, 220), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)
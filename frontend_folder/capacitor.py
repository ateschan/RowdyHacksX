
import pygame

def fluxCapacitor(screen):

    surf1 = pygame.Surface((50,220), pygame.SRCALPHA, 32)
    pygame.draw.rect(surf1, "grey", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    pygame.draw.rect(surf1, "aqua", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=3, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    surf2 = pygame.Surface((50,220), pygame.SRCALPHA, 32)
    pygame.draw.rect(surf2, "grey", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    pygame.draw.rect(surf2, "aqua", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=3, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    surf3 = pygame.Surface((50,220), pygame.SRCALPHA, 32)
    pygame.draw.rect(surf3, "grey", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    pygame.draw.rect(surf3, "aqua", 
    pygame.Rect(0, 0, 
    50, 220), 
    width=3, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)
    

    surf3 = pygame.transform.rotate(surf3, -45)
    surf2 = pygame.transform.rotate(surf2, 45)

    screen.blit(surf1, (screen.get_width()/2 - 25,520))
    screen.blit(surf2, (screen.get_width()/2 - 205,300))
    screen.blit(surf3, (screen.get_width()/2 + 20,300))#yellow

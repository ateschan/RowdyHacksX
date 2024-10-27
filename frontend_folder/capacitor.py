
import pygame
from .waves import generate_wave


def fluxCapacitor( screen, waveform1, waveform2, waveform3):

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
    

    clip_rect = pygame.Rect(0, 0, 200, 500)
    surf1.set_clip(clip_rect)
    surf2.set_clip(clip_rect)
    surf3 = pygame.transform.rotate(surf3, -45)
    surf2 = pygame.transform.rotate(surf2, 45)
    waveform1.scroll(1,0)
    waveform2.scroll(-1,0)
    waveform3.scroll(-1,0)

    #surf1.blit(pygame.transform.rotate(waveform1, 45), (screen.get_width()/2, screen.get_height()/2 + 400))
    #surf2.blit(pygame.transform.rotate(waveform2, -45), (screen.get_width()/2, -screen.get_height()/2 + 400))
    #surf3.blit(pygame.transform.rotate(waveform3, 90), (screen.get_width()/2 - waveform3.get_height()/2, 520))
    surf1.blit(pygame.transform.rotate(waveform1, 90), (0, 0))
    surf2.blit(pygame.transform.rotate(waveform2, -45), (0,0))
    rotated_waveform = pygame.transform.rotate(waveform3, 45)
    rect = rotated_waveform.get_rect()
    surf3.blit(pygame.transform.rotate(waveform3, 45), (0,-rect.height + 190))
    
    surf2 = pygame.transform.flip(surf2, True, True)
    screen.blit(surf1, (screen.get_width()/2 - 25,520))
    screen.blit(surf2, (screen.get_width()/2 - 205,300))
    screen.blit(surf3, (screen.get_width()/2 + 20,300))#yellow

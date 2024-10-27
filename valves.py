import pygame

def fluxValves(screen):

    # Bottom Valve
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2,715), 45)
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2 + 140,728), 20)
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(screen.get_width()/2, 715, 
    150, 25), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    #  Top Left Valve
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2 - 175,325), 45)
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2 - 175,470),20 )
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(screen.get_width()/2 - 187, 330, 
    25, 150), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    #  Top RightValve
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2 + 175,330), 45)
    pygame.draw.circle(screen,(166,5,5), (screen.get_width()/2 + 173,470), 20)
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(screen.get_width()/2 + 160, 330, 
    25, 150), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

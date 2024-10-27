import pygame

def fluxValves(screen):

    # Bottom Valve
    pygame.draw.circle(screen,(166,5,5), (800,715), 50)
    pygame.draw.circle(screen,(166,5,5), (920,728), 20)
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(780, 715, 
    150, 25), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    #  Top Left Valve
    pygame.draw.circle(screen,(166,5,5), (625,325), 50)
    pygame.draw.circle(screen,(166,5,5), (625,470),20 )
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(615, 330, 
    25, 150), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)

    #  Top RightValve
    pygame.draw.circle(screen,(166,5,5), (975,330), 50)
    pygame.draw.circle(screen,(166,5,5), (975,470), 20)
    pygame.draw.rect(screen, (182,152,30), 
    pygame.Rect(960, 330, 
    25, 150), 
    width=0, 
    border_radius=15, 
    border_top_left_radius=-1, 
    border_top_right_radius=-1, 
    border_bottom_left_radius=-1, 
    border_bottom_right_radius=-1)
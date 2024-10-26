import pygame
pygame.font.init()

#Text stuff
font = pygame.font.SysFont('./frontend_folder/terminus.ttf', 40)
textTop = font.render('DISCONNECT CAPACITOR DRIVE', True, "white", "brown3")
textBottom = font.render('BEFORE OPENING', True, "white", "brown3")
textTopRect = textTop.get_rect()
textBottomRect = textBottom.get_rect()

#Edit resolution here...
screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)

def render_frontend():
    #bg
    screen.fill("orange")
    textTopRect.center = (screen.get_width()/2, 150)
    textBottomRect.center = (screen.get_width()/2, 190)

    #After bg
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(screen.get_width()/2 - 350, 120, 
                    700, 750), 
                    width=0, 
                    border_radius=15, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    #Black Outer Tubing
    pygame.draw.rect(screen, "black", 
                    pygame.Rect(screen.get_width()/2 - 300, 
                    220, 600, 600), 
                    width=35, border_radius=30, 
                    border_top_left_radius=-1,
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    #Inside box 
    pygame.draw.rect(screen, (25,31,61), 
                    pygame.Rect(screen.get_width()/2 - 250, 
                    270, 500, 500), 
                    width=0, border_radius=15, 
                    border_top_left_radius=0,
                    border_top_right_radius=0, 
                    border_bottom_left_radius=0, 
                    border_bottom_right_radius=0)
    # TURD
    pygame.draw.rect(screen, "black", 
                    pygame.Rect(screen.get_width()/2 - 50, 260, 
                    20, 220), 
                    width=0, 
                    border_radius=15, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    #Top Label
    pygame.draw.rect(screen, "brown3", 
                    pygame.Rect(screen.get_width()/2 - 240, 130, 480, 40),
                    width=0, 
                    border_radius=0, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    
    #Top Label
    pygame.draw.rect(screen, "brown3", 
                    pygame.Rect(screen.get_width()/2 - 135, 170, 
                    270, 
                    40), 
                    width=0, 
                    border_radius=0, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    screen.blit(textTop, textTopRect)
    screen.blit(textBottom, textBottomRect)
    # #TOP RIGHT
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 + 290, 65), 
    #                  (screen.get_width()/2 + 250, 110), 3)
    # #TOP LEFT
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 290, 65), 
    #                  (screen.get_width()/2 - 250, 110), 3)

    # #BOTTOM LEFT
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 300, 655),
    #                  (screen.get_width()/2 - 250, 610), 3)
    # #BOTTOM RIGHT
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 + 300, 655),
    #                  (screen.get_width()/2 + 250, 610), 3)
    
    #Red Circle Left

    #Red Circle Right 

    #Red Circle Bottom

    #Yellow Tubing Left

    #Yellow Tubing Right 

    #Yellow Tubing Bottom

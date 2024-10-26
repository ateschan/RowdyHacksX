import pygame
screen = pygame.display.set_mode((1280, 720))

def render_frontend():
    #bg
    screen.fill("orange")

    #After bg
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(30, 30, 
                    screen.get_width() - 60, 
                    screen.get_height() - 60), 
                    width=0, 
                    border_radius=15, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    #tubing
    pygame.draw.rect(screen, "black", 
                    pygame.Rect(screen.get_width()/2 - 300, 
                    60, 600, 600), 
                    width=25, border_radius=7, 
                    border_top_left_radius=-1,
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    #Inside box 
    pygame.draw.rect(screen, "grey", 
                    pygame.Rect(screen.get_width()/2 - 250, 
                    110, 500, 500), 
                    width=0, border_radius=100, 
                    border_top_left_radius=0,
                    border_top_right_radius=0, 
                    border_bottom_left_radius=0, 
                    border_bottom_right_radius=0)

    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 + 290, 65), 
    #                  (screen.get_width()/2 + 230, 40), 15)
    # 
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 290, 65), 
    #                  (screen.get_width()/2 - 350, 40), 15)
    # 
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 290, 650), 
    #                  (screen.get_width()/2 - 350, 625), 15)
    # 
    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 350, 35),
    #                  (screen.get_width()/2 - 350, 630), 15)

    # pygame.draw.line(screen, "black",
    #                  (screen.get_width()/2 - 350, 40),
    #                  (screen.get_width()/2 + 230, 40), 15)

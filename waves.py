import pygame

def generate_wave(surface, wave_thickness, wave_color, data):
    pygame.draw.lines(surface, wave_color, False, data, wave_thickness)

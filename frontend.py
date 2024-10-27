import pygame
from capacitor import fluxCapacitor
from valves import fluxValves
from waves import generate_wave
from pygame import mixer 
from models.audio_file import AudioFile

#Edit resolution here...
screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
audio_path="./audio/piano.wav"

mixer.init()
mixer.music.load(audio_path) 
mixer.music.set_volume(1.0)
pygame.font.init()
audio = AudioFile(audio_path)

freq_data = []
drawing_rate = 0
print(len(audio.frames[20].data[0]))
sample_rate = 512
k = sample_rate * len(audio.frames) 
for frame in audio.frames:
    freq1 = frame.data[1:2]
    if len(freq1) > 0:
        print(len(freq1[0]))
        for sample in freq1[0]:
            freq_data.append((int(k), sample*200))
            k-=1
    else:
        for i in range(sample_rate):
            freq_data.append((int(k), 0))


#Text stuff
font = pygame.font.SysFont('./frontend_folder/terminus.ttf', 40)
textTop = font.render('DISCONNECT CAPACITOR DRIVE', True, "white", "brown3")
textBottom = font.render('BEFORE OPENING', True, "white", "brown3")
textTopRect = textTop.get_rect()
textBottomRect = textBottom.get_rect()

waveform1 = pygame.Surface((len(freq_data), 50), pygame.SRCALPHA, 32)
waveform1 = waveform1.convert_alpha()
generate_wave(waveform1, 1, "red", list(reversed(freq_data)))

waveform2 = pygame.Surface((len(freq_data), 50), pygame.SRCALPHA, 32)
waveform2 = waveform2.convert_alpha()

#waveform2 = pygame.transform.flip(waveform2, False, True)
generate_wave(waveform2, 1, "blue", freq_data)

waveform3 = pygame.Surface((len(freq_data), 50), pygame.SRCALPHA, 32)
waveform3 = waveform3.convert_alpha()
generate_wave(waveform3, 1 , "blue", freq_data)

mixer.music.play()
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
                    width=50, border_radius=30, 
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

    #Top Label
    pygame.draw.rect(screen, "brown3", 
                    pygame.Rect(screen.get_width()/2 - 240, 130, 480, 40),
                    width=0, 
                    border_radius=0, 
                    border_top_left_radius=-1, 
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    
    #Bottom Label
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

    #Pipe1 Top 
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(screen.get_width()/2 - 60, 
                    0, 120, 120), 
                    width=0, border_radius=15, 
                    border_top_left_radius=0,
                    border_top_right_radius=0, 
                    border_bottom_left_radius=0, 
                    border_bottom_right_radius=0)

    #Pipe2 Top
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(screen.get_width()/2 + 230, 
                    0, 20, 120), 
                    width=0, border_radius=15, 
                    border_top_left_radius=0,
                    border_top_right_radius=0, 
                    border_bottom_left_radius=0, 
                    border_bottom_right_radius=0)

    #Pipe3 Side1
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(screen.get_width()/2 + 300, 
                    400, 300, 120), 
                    width=0, border_radius=40, 
                    border_top_left_radius=-1,
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)
    
    #Pipe3 Side2
    pygame.draw.rect(screen, "bisque4", 
                    pygame.Rect(screen.get_width()/2 + 500, 
                    -40, 100, 520), 
                    width=0, border_radius=40, 
                    border_top_left_radius=-1,
                    border_top_right_radius=-1, 
                    border_bottom_left_radius=-1, 
                    border_bottom_right_radius=-1)

    # Capacitor
    pygame.draw.circle(screen,(210, 180, 140), (screen.get_width()/2 + 175,330), 50)
    pygame.draw.circle(screen,(210, 180, 140), (screen.get_width()/2 - 175,325), 50)
    pygame.draw.circle(screen,(210, 180, 140), (screen.get_width()/2,715), 50)
    fluxCapacitor( screen, waveform1, waveform2, waveform3)
    fluxValves(screen)

# Here we should how to draw it onto a screen.
    screen.blit(textTop, textTopRect)
    screen.blit(textBottom, textBottomRect)


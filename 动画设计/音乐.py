import pygame
pygame.mixer.init()

pygame.time.delay(1000)
s = pygame.mixer.Sound('../music/Alarm09.wav')
s.play()
pygame.time.delay(3000)
s.set_volume(0.1)
s.play(2)

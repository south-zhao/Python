import pygame
pygame.mixer.init()

pygame.time.delay(1000)
pygame.mixer.music.load('../music/1.mp3')
pygame.mixer.music.play(-1)
pygame.time.delay(3000)
if pygame.mixer.music.get_busy():
    pygame.mixer.music.pause()
    pygame.time.delay(3000)
    s = pygame.mixer.Sound('../music/1.mp3')
    s.play()
    pygame.time.delay(3000)
    pygame.mixer.music.unpause()

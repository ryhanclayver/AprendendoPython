import pygame

pygame.init()  # Inicializa o pygame

pygame.mixer_music.load('12h.mp3')  # Carrega o arquivo MP3
pygame.mixer_music.play()  # Inicia a reprodução

while pygame.mixer_music.get_busy():  # Laço enquanto a música tocar
    pygame.time.Clock().tick(10)  # Pausa por 10 seg quando música acabar

pygame.quit()  # Finaliza o pygame após 10 segundos de fim de música

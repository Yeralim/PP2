import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))

clock_face = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")  
second_hand = pygame.image.load("sec_hand.png") 

clock_center = (400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    angle_minute = -(minutes * 6 + seconds * 0.1)  
    angle_second = -(seconds * 6)  

    rot_minute = pygame.transform.rotate(minute_hand, angle_minute)
    rot_second = pygame.transform.rotate(second_hand, angle_second)

    minute_rect = rot_minute.get_rect(center=clock_center)
    second_rect = rot_second.get_rect(center=clock_center)

    
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))  
    screen.blit(rot_minute, minute_rect.topleft)  
    screen.blit(rot_second, second_rect.topleft)  

    pygame.display.flip()

pygame.quit()

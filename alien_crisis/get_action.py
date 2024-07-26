import sys


import pygame


def check_events(output):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            output[0] = mouse_x
            output[1] = mouse_y
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                output[2] = 1
            if event.key == pygame.K_a:
                output[3] = 1
            if event.key == pygame.K_s:
                output[4] = 1
            if event.key == pygame.K_d:
                output[5] = 1
            if event.key == pygame.K_q:
                output[6] = 1
            if event.key == pygame.K_r:
                output[7] = 1
            
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                output[2] = -1
            if event.key == pygame.K_a:
                output[3] = -1
            if event.key == pygame.K_s:
                output[4] = -1
            if event.key == pygame.K_d:
                output[5] = -1

    return output

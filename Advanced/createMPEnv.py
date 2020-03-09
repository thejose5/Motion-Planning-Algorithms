import pygame
from rrt import *

pygame.init()
res = 1600,1600
screen = pygame.display.set_mode(res)
screen.fill((100, 186, 100))
pygame.display.set_caption('Visualizer')
pygame.display.update()
q_st = (100,1000)
q_end = (1000,100)

# Define Obstacles
obs1 = (200,200,300,400)
obs2 = (700,600,600,600)
obs = [obs1,obs2]
pygame.draw.rect(screen,(0,0,255),obs1)
pygame.draw.rect(screen,(0,0,255),obs2)

# Display start and end point
goalRad = 20 #If the tree comes within this radius of the goal, it will be counted as a success
# pygame.draw.rect(screen,(255,0,0),q_st+(20,20))
pygame.draw.circle(screen,(255,0,0),q_st,20)
pygame.draw.circle(screen,(255,255,255),q_end,goalRad)
#pygame.draw.rect(screen,(255,255,255),q_end + (20,20))
pygame.display.update()

rrt = RRT(q_st,q_end,obs,screen,goalRad)
rrt.execRRT()

# print("Got out")
while(True):
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

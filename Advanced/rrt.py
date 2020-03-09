import pygame
import numpy as np
import math
from random import randint

class RRT:

    def __init__(self,q_st,q_end,obs,screen,goalRad):
        self.q_st = q_st
        self.q_end = q_end
        self.obs = obs
        self.tree = [q_st]
        self.path_found = False
        self.goalRad = goalRad
        self.delta = 40
        self.parent = []
        self.screen = screen

    def isColliding(self,point):
        if((point[0]>=self.obs[0][0] and point[0]<=(self.obs[0][0]+self.obs[0][2]) and point[1]>=self.obs[0][1] and point[1]<=(self.obs[0][1]+self.obs[0][3]))
            or (point[0]>=self.obs[1][0] and point[0]<=(self.obs[1][0]+self.obs[1][2]) and point[1]>=self.obs[1][1] and point[1]<=(self.obs[1][1]+self.obs[1][3]))):
            return True
        else:
            return False

    def execRRT(self):
        screen = self.screen
        print("Reached execRRT")
        while(not self.path_found):
            # Generate random point
            delta = self.delta
            ran_x = randint(0,1600) #1600 is the size of the game screen
            ran_y = randint(0,1600)
            point = (ran_x,ran_y)

            #Check if point collides with object
            if self.isColliding(point):
                continue
            q_nearest = self.closestPoint(point)

            #Find new point in the direction of point
            euc_dist = self.e_dist(q_nearest,point)#math.sqrt(math.pow((q_nearest[0]-point[0]),2)+math.pow((q_nearest[1]-point[1]),2))
            theta = math.atan2((point[1]-q_nearest[1]),(point[0]-q_nearest[0]))
            if (euc_dist<=delta):
                q_new = point
            else:
                q_new = (int(round((q_nearest[0]+delta*math.cos(theta)),0)),int(round((q_nearest[1]+delta*math.sin(theta)),0)))

            # Check if new point or new path collides with object
            if self.isColliding(q_new) or self.is_path_colliding(q_nearest,self.e_dist(q_nearest,q_new),theta):
                continue

            #Now add this point to the tree
            # print(self.tree)
            # print(self.parent)
            self.tree.append(q_new)
            self.parent.append(q_nearest)
            pygame.draw.circle(screen,[0,0,0],q_new,10)
            pygame.draw.line(screen,[0,0,0],q_nearest,q_new,5)

            #Check if new point is near goal
            # print(q_new,self.e_dist(q_new,self.q_end), self.q_end)
            pygame.display.update()
            if self.e_dist(q_new,self.q_end)<self.goalRad:
                pygame.draw.line(screen, [255, 0, 0], self.q_end, q_new, 5)
                pygame.display.update()
                self.path_found==True
                self.dispPath(self.tree,self.parent)
                break


            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     for event in pygame.event.get():
                #         if event.type == pygame.MOUSEBUTTONDOWN:
                #             break

        return 0



    def closestPoint(self,point):
        closest_pt = (17000,17000)
        for tree_pt in self.tree:
            #Find the closest point according to manhattan distance
            if(self.m_dist(closest_pt,point)>self.m_dist(tree_pt,point)):
                closest_pt = tree_pt
        return closest_pt

    def e_dist(self,p1,p2):
        dist = math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))
        return dist

    def m_dist(self,p1,p2):
        dist = (abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))
        return dist

    def is_path_colliding(self, start_pos, euc_dist, theta, epsilon=10):
        i=0
        while i<=euc_dist: #for i in range(0,euc_dist,euc_dist/epsilon):
            x_new = start_pos[0] + i * math.cos(theta)
            y_new = start_pos[1] + i * math.sin(theta)
            new_p = x_new, y_new
            if self.isColliding(new_p):
                return True
            i = i+euc_dist/epsilon
        return False

    def dispPath(self,tree,parent):
        tree.pop(0)
        i = len(tree)-1
        prt = parent[i]
        pygame.draw.line(self.screen, [255, 0, 0], tree[i], prt, 5)
        pygame.display.update()
        while prt!=self.q_st:
            i = tree.index(prt)
            prt = parent[i]
            pygame.draw.line(self.screen, [255, 0, 0], tree[i], prt, 10)
            pygame.display.update()

            # Adding a exit button in case something goes wrong
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())









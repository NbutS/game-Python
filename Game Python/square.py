import pygame
import sys


class Square():
    def __init__(self, m_pos, m_color):
        self.ori_Pos = m_pos
        self.color = m_color
        self.isClicked = False
        self.pos = m_pos
        self.img = pygame.image.load('square-16.jpg')
        self.img = pygame.transform.scale(self.img, (35, 35))

    # def ChangeColor(self):

       # self.img = pygame.Color(r, g, b)

    def GetImage(self):
        return self.img

    def GetPos(self):
        return self.pos

    def GetSize(self):
        return self.img.get_size()

    def ChangeColor(self, color):
        self.img.fill(color)

    def SetIsClick(self, isClick):
        self.isClicked = isClick

    def GetIsClick(self):
        return self.isClicked

    def ChangeAlpha(self,alpha):
        pygame.Surface.set_alpha(self.img, alpha)
    def ChangeSize(self,size):
        self.img = pygame.transform.scale(self.img,size)
    def Renew(self,location):
        self.pos = location
        self.ori_Pos = location
    def Move(self, location,dir):
        x = location[0]
        y = location[1]
        velX = dir[0]
        velY = dir[1]
        while True:
            self.pos[0] += self.pos[0] + 0.2*velX
            self.pos[1] += self.pos[1] + 0.2*velY
            if self.ori_Pos[0] < x:
                if self.pos[0] > x:
                    self.Renew(location)
                    break
            elif self.ori_Pos[0] > x:
                if self.pos[0] < x:
                    self.Renew(location)
                    break
            elif self.ori_Pos[1] > y:
                if self.pos[1] < y:
                    self.Renew(location)
                    break
            elif self.ori_Pos[1] < y:
                if self.pos[1] > y:
                    self.Renew(location)
                    break

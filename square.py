import pygame
import sys


class Square():
    def __init__(self, m_pos, m_oriPos, m_color, m_alterColor):
        self.isMoving = False
        self.ori_Pos = m_oriPos
        self.color = m_color
        self.alterColor = m_alterColor
        self.isClicked = False
        self.isBlack = False
        self.pos = m_pos
        self.img = pygame.image.load('square-16.jpg')
        self.img = pygame.transform.scale(self.img, (50, 50))

    def GetImage(self):
        return self.img

    def GetPos(self):
        return self.pos

    def GetOriPos(self):
        return self.ori_Pos

    def GetSize(self):
        return self.img.get_size()

    def ChangeColor(self):

        self.img.fill(self.alterColor)

    def SetColor(self, m_color):
        self.img.fill(m_color)

    def SetIsClick(self, isClick):
        self.isClicked = isClick

    def GetIsClick(self):
        return self.isClicked

    def ChangeAlpha(self, alpha):
        pygame.Surface.set_alpha(self.img, alpha)

    def ChangeSize(self, size):
        self.img = pygame.transform.scale(self.img, size)

    def SetIsBlack(self, isblack):
        self.isBlack = isblack

    def GetIsBlack(self):
        return self.isBlack

    def Renew(self, location, ori):
        self.SetIsBlack(True)
        self.pos = (500, 500)
        self.ori_Pos = ori
        self.SetColor((0, 0, 0))
        self.SetIsClick(False)

    def Move(self, location, dir):
        x = location[0]
        y = location[1]
        velX = dir[0]
        velY = dir[1]
        self.pos[0] = self.pos[0] + 0.02*velX
        self.pos[1] = self.pos[1] + 0.02*velY
        if self.ori_Pos[0] < x:
            if self.pos[0] > (x + self.ori_Pos[0])/2:

                ori = (x, y)
                self.Renew(location, ori)
        elif self.ori_Pos[0] > x:
            if self.pos[0] < (x + self.ori_Pos[0])/2:

                ori = (x, y)
                self.Renew(location, ori)
        elif self.ori_Pos[1] > y:
            if self.pos[1] < (y + self.ori_Pos[1])/2:

                ori = (x, y)
                self.Renew(location, ori)
        elif self.ori_Pos[1] < y:
            if self.pos[1] > (y + self.ori_Pos[1])/2:

                ori = (x, y)
                self.Renew(location, ori)

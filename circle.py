import pygame


class Circle():
    def __init__(self, m_pos):
        self.pos = m_pos
        self.img = pygame.image.load('272591.png')
        self.img = pygame.transform.scale(self.img, (8, 8))

    def GetPos(self):
        return self.pos

    def GetImage(self):
        return self.img

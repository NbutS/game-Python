import pygame


class Score():
    def __init__(self):
        self.score = 0
        self.bestScore = 0

    def GetScore(self):
        return self.score

    def GetBestScore(self):
        return self.bestScore

    def SetScore(self, m_score):
        self.score = m_score

    def SetBestScore(self, m_bestScore):
        self.bestScore = m_bestScore

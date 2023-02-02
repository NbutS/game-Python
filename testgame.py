from json import load
import sys
import pygame
import square
import circle
import Color
import Score
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
isChoosed = False
oriSize = (50, 50)
scaleSize = (40, 40)
isMoving = False
posIsChosen_1 = (0, 0)
posIsChosen_2 = (0, 0)
a, b = 0, 0
start = (135, 135)
oriPosMove_1 = (0, 0)
oriPosMove_2 = (0, 0)
squareArrays = []
arrayID = ((2, 3, 1, 4), (3, 4, 1, 2), (5, 8, 7, 6), (7, 5, 8, 6))
isSameColor = False
secondClick = False
timeCount = 0
score = Score.Score()
for i in range(0, 4):
    squareArrays.append([])
    for j in range(0, 4):
        m_pos1 = (start[0] + (oriSize[0]+3)*(i),
                  start[1] + (oriSize[1] + 3)*(j))
        m_oriPos1 = (start[0] + (oriSize[0] + 3)*(i),
                     start[1] + (oriSize[1] + 3)*(j))
        m_pos = list(m_pos1)
        m_oriPos = list(m_oriPos1)
        squareArrays[i].append(square.Square(
            m_pos, m_oriPos, Color.grey, Color.coupleColor[arrayID[i][j] - 1]))
for i in range(0, 4):
    for j in range(0, 4):
        squareArrays[i][j].GetImage().fill(Color.grey)
textFont = pygame.font.SysFont("monospace", 25, True, True)
textFont_game_over = pygame.font.SysFont("monospace", 40, True, True)
textFont_win_game = pygame.font.SysFont("monospace", 40, True, True)
delaTime = 0
Time = 100
playgame = True
wingame = False
gameover = False
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(0, 4):
                for j in range(0, 4):
                    if not squareArrays[i][j].GetIsBlack() and not squareArrays[i][j].GetIsClick() and isChoosed == False and x > squareArrays[i][j].GetPos()[0] and x < squareArrays[i][j].GetPos()[0] + oriSize[0] and y > squareArrays[i][j].GetPos()[1] and y < squareArrays[i][j].GetPos()[1] + oriSize[1]:
                        squareArrays[i][j].ChangeColor()
                        squareArrays[i][j].SetIsClick(True)
                        isChoosed = True
                        posIsChosen_1 = (i, j)
                        oriPosMove_1 = squareArrays[i][j].GetOriPos()
                    elif not squareArrays[i][j].GetIsBlack() and not squareArrays[i][j].GetIsClick() and isChoosed == True and x > squareArrays[i][j].GetPos()[0] and x < squareArrays[i][j].GetPos()[0] + scaleSize[0] and y > squareArrays[i][j].GetPos()[1] and y < squareArrays[i][j].GetPos()[1] + scaleSize[1] and not secondClick:
                        squareArrays[i][j].ChangeColor()
                        secondClick = True
                        posIsChosen_2 = (i, j)
                        squareArrays[i][j].SetIsClick(True)
                        score.SetScore(score.GetScore()+1)
                        if (arrayID[i][j] == arrayID[posIsChosen_1[0]][posIsChosen_1[1]]):
                            isSameColor = True
                            a = squareArrays[i][j].GetPos()[
                                0] - squareArrays[posIsChosen_1[0]][posIsChosen_1[1]].GetPos()[0]
                            b = squareArrays[i][j].GetPos(
                            )[1] - squareArrays[posIsChosen_1[0]][posIsChosen_1[1]].GetPos()[1]
                            oriPosMove_2 = squareArrays[i][j].GetOriPos()

    if secondClick:
        timeCount += 1
        if (timeCount > 60):
            timeCount = 0
            secondClick = False
            if isSameColor:
                isSameColor = False
                isMoving = True
            else:
                squareArrays[posIsChosen_1[0]
                             ][posIsChosen_1[1]].SetColor(Color.grey)
                squareArrays[posIsChosen_2[0]
                             ][posIsChosen_2[1]].SetColor(Color.grey)
                squareArrays[posIsChosen_1[0]
                             ][posIsChosen_1[1]].SetIsClick(False)
                squareArrays[posIsChosen_2[0]
                             ][posIsChosen_2[1]].SetIsClick(False)
                isChoosed = False

    if isMoving:
        squareArrays[posIsChosen_1[0]][posIsChosen_1[1]].Move(
            list(oriPosMove_2), (a, b))
        squareArrays[posIsChosen_2[0]][posIsChosen_2[1]].Move(
            list(oriPosMove_1), (-a, -b))
        if not squareArrays[posIsChosen_1[0]][posIsChosen_1[1]].GetIsClick() and not squareArrays[posIsChosen_2[0]][posIsChosen_2[1]].GetIsClick():
            isMoving = False
            isChoosed = False
    if (Time <= 0):
        gameover = True
        playgame = False
        wingame = False
    check = False
    for i in range(0, 4):
        for j in range(0, 4):
            if not squareArrays[i][j].GetIsBlack():
                check = True
                break
    if not check:
        wingame = True
        playgame = False
        gameover = False
    if playgame:
        delaTime += 1
        if (delaTime >= 60):
            delaTime = 0
            Time = Time - 1
        screen.fill((0, 0, 0))
        for i in range(0, 4):
            for j in range(0, 4):
                screen.blit(squareArrays[i][j].GetImage(),
                            squareArrays[i][j].GetPos())
        textTBD = textFont.render(
            "Steps: " + str(score.GetScore()), 1, (Color.blue_2))
        TextTime = textFont.render("TIME: " + str(Time), 1, (Color.red_3))
        screen.blit(textTBD, (185, 75))
        screen.blit(TextTime, (325, 15))
    elif gameover:
        game_over_text = textFont_game_over.render("GAME OVER", 2, Color.red_5)
        game_over_steps = textFont_game_over.render(
            "STEPS: " + str(score.GetScore()), 1, (Color.yellow_2))
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (135, 150))
        screen.blit(game_over_steps, (135, 200))
    elif wingame:
        win_game = textFont_win_game.render("YOU WIN", 2, Color.red_5)
        win_game_steps = textFont_win_game.render(
            "STEPS: " + str(score.GetScore()), 1, (Color.green_2))
        screen.fill((0, 0, 0))
        screen.blit(win_game, (135, 150))
        screen.blit(win_game_steps, (135, 200))
    pygame.display.update()
    clock.tick(60)

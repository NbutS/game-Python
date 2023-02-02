from json import load
import sys
import pygame
import square
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
sizeX, sizeY = 35, 35
pos1 = (50, 50)
pos2 = (150, 50)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
sq_1 = square.Square(pos1, red)
sq_2 = square.Square(pos2, green)
isChoosed = False
oriSize = (35, 35)
scaleSize = (40, 40)
sq_1.GetImage().fill(red)
sq_2.GetImage().fill(green)

print(sq_1.GetSize()[0])
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if not sq_1.GetIsClick() and x > sq_1.GetPos()[0] and x < sq_1.GetPos()[0] + oriSize[0] and y > sq_1.GetPos()[1] and y < sq_1.GetPos()[1] + oriSize[1]:

                sq_1.ChangeSize((30, 30))
                sq_1.SetIsClick(True)

            elif sq_1.GetIsClick() and x > sq_1.GetPos()[0] and x < sq_1.GetPos()[0] + scaleSize[0] and y > sq_1.GetPos()[1] and y < sq_1.GetPos()[1] + scaleSize[1]:
                sq_1.ChangeSize((35, 35))
                sq_1.SetIsClick(False)
            if not sq_2.GetIsClick() and x > sq_2.GetPos()[0] and x < sq_2.GetPos()[0] + oriSize[0] and y > sq_2.GetPos()[1] and y < sq_2.GetPos()[1] + oriSize[1]:
                sq_2.ChangeSize((30, 30))
                sq_2.SetIsClick(True)
            elif sq_2.GetIsClick() and x > sq_2.GetPos()[0] and x < sq_2.GetPos()[0] + scaleSize[0] and y > sq_2.GetPos()[1] and y < sq_2.GetPos()[1] + scaleSize[1]:
                sq_2.ChangeSize((35, 35))
                sq_2.SetIsClick(False)
    screen.fill((0, 0, 0))
    screen.blit(sq_1.GetImage(), sq_1.GetPos())
    screen.blit(sq_2.GetImage(), sq_2.GetPos())
    pygame.display.update()
    clock.tick(60)

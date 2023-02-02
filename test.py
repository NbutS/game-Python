import pygame as pg

WHITE = (255, 255, 255)
GREEN = (33, 133, 33)
RED = (255, 0, 0)
SCREEN = pg.display.set_mode((700, 500))
clock = pg.time.Clock()
cT = 140  # cycle time
cNum = 3  # cyle number


class Rectangle(pg.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.height = height
        self.color = color
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, rel_x, rel_y):
        self.rect.move_ip(rel_x, rel_y)

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)


class Rect1():

    def __init__(self, color, width, height, x, y, all_sprites):

        self.height = height
        self.selected1 = False
        self.rect = pg.Rect((x, y, width, height))
        self.rectangles = []

        for z in range(0, cNum * cT, cT):
            rect = Rectangle(color, width, height, x, self.rect.y - z + cT)
            self.rectangles.append(rect)
            all_sprites.add(rect)

    def move(self, rel_x, rel_y):
        self.rect.move_ip(rel_x, rel_y)
        for r in self.rectangles:
            r.move(rel_x, rel_y)

    def collidepoint(self, pos):
        for r in self.rectangles:
            if r.rect.collidepoint(pos):
                return True

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.collidepoint(event.pos):
                self.selected1 = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.selected1 = False
        elif event.type == pg.MOUSEMOTION:
            if self.selected1:
                self.move(0, event.rel[1])


class Connection():

    def __init__(self, rect_1, rect_2, vel):
        self.rect_1 = rect_1
        self.rect_2 = rect_2
        self.vel = vel

    def draw(self, screen):

        for r_1 in self.rect_1.rectangles:
            for r_2 in self.rect_2.rectangles:
                dist1 = r_2.rect.x - r_1.rect.x
                velocity = int(dist1 * self.vel)  # green wave angle

                A_start_x, A_start_y = r_1.rect.topright
                A_end_x, A_end_y = r_1.rect.bottomright

                B_start_x, B_start_y = r_2.rect.topleft
                B_end_x, B_end_y = r_2.rect.bottomleft

                if B_start_y < A_start_y - velocity and B_end_y > A_start_y - velocity:
                    start_pos = (A_start_x, A_start_y)
                    end_pos = (B_start_x, A_start_y - velocity)  # minus 50
                    pg.draw.aaline(screen, GREEN, start_pos, end_pos, 1)
                if B_end_y > A_end_y - velocity and B_start_y < A_end_y - velocity:
                    start_pos = (A_end_x, A_end_y-1)
                    end_pos = (B_end_x, A_end_y - 1 - velocity)  # minus 50
                    pg.draw.aaline(screen, RED, start_pos, end_pos, 1)


def main():
    pg.init()
    all_sprites = pg.sprite.Group()

    objects = [
        Rect1(GREEN, 10, 58, 55, 244, all_sprites),
        Rect1(GREEN, 10, 111, 188, 226, all_sprites),
        Rect1(RED, 10, 68, 69, 222, all_sprites),
        Rect1(RED, 10, 121, 211, 202, all_sprites), ]
    conns = [
        Connection(objects[0], objects[1], 0.1),
        Connection(objects[2], objects[3], -0.1), ]

    done = False
    clock = pg.time.Clock()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            for o in objects:
                o.handle_event(event)

        SCREEN.fill(WHITE)

        all_sprites.draw(SCREEN)

        for c in conns:
            c.draw(SCREEN)

        pg.display.update()
        clock.tick(60)
    pg.quit()


if __name__ == '__main__':
    main()

import pygame
from vgd import colors

class BouncingRectangle(object):

    def __init__(self, position, velocity, width, height, color=colors["black"]):
        self.rect = [position[0], position[1], width, height]
        self.vel = list(velocity)
        self.col = color

    def draw(self, surf):
        pygame.draw.rect(surf, self.col, self.rect)

    def move(self):
        self.rect[0] += self.vel[0]
        self.rect[1] += self.vel[1]

    def contain_within_rect(self, boundary_rect, bounciness=1.0):
        sx,sy,sw,sh = self.rect
        bx,by,bw,bh = boundary_rect

        # LEFT WALL
        if sx < bx:
            # remove me from inside the wall
            self.rect[0] = bx
            # reverse my x velocity (times bounciness)
            self.vel[0] = -self.vel[0] * bounciness
        # RIGHT WALL
        elif sx + sw > bx + bw:
            # remove me from inside the wall
            self.rect[0] = bx + bw - sw
            # reverse my x velocity (times bounciness)
            self.vel[0] = -self.vel[0] * bounciness

        # TOP WALL
        if sy < by:
            # remove me from inside the wall
            self.rect[1] = by
            # reverse my y velocity (times bounciness)
            self.vel[1] = -self.vel[1] * bounciness
        # BOTTOM WALL
        elif sy + sh > by + bh:
            # remove me from inside the wall
            self.rect[1] = by + bh - sh
            # reverse my y velocity (times bounciness)
            self.vel[1] = -self.vel[1] * bounciness

# BouncingMegaman is a *subclass* of BouncingRectangle
# ...or, BouncingRectangle is the *superclass* of BouncingMegaman
class BouncingMegaman(BouncingRectangle):

    def __init__(self, position, velocity):
        self.mm_image = pygame.image.load("images/megaman.png")
        self.mm_image = pygame.transform.scale(self.mm_image, [30,30])
        image_rect = self.mm_image.get_rect()
        # super().__init__ says "get the superclass and do its __init__ function)
        super().__init__(position, velocity, image_rect[2], image_rect[3])

    def draw(self, surf):
        surf.blit(self.mm_image, self.rect)

    # the contain_within_rect function is *inherited* from BouncingRectangle!
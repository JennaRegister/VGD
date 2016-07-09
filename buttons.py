import pygame
import pygame.font

from vgd import is_point_in_rect

pygame.init()
pygame.font.init()

class Button(object):

    def __init__(self, text, centerxy, callback, textsize=18, textcolor=(0,0,0), bgcolor=None, mouseovercolor=None, padding=0):
        # note: set bgcolor to None to have it transparent
        self.font = pygame.font.Font(None, textsize)
        self.bgcolor = bgcolor
        self.mouseovercolor = mouseovercolor
        self.pixels = self.font.render(text, True, textcolor, bgcolor)
        self.mouseover_pixels = self.font.render(text, True, textcolor, mouseovercolor)
        self.rect = self.pixels.get_rect()
        self.pad_rect = pygame.Rect(self.rect)
        self.pad_rect[2] += 2*padding
        self.pad_rect[3] += 2*padding
        self.rect.centerx = centerxy[0]
        self.rect.centery = centerxy[1]
        self.pad_rect.centerx = centerxy[0]
        self.pad_rect.centery = centerxy[1]

        self.onclick = callback

    def render(self, surf, mouse_coordinate):
        if is_point_in_rect(mouse_coordinate, self.pad_rect):
            pygame.draw.rect(surf, self.mouseovercolor, self.pad_rect)
            surf.blit(self.mouseover_pixels, self.rect)
        else:
            pygame.draw.rect(surf, self.bgcolor, self.pad_rect)
            surf.blit(self.pixels, self.rect)

    def handle_mouseup_event(self, evt):
        if is_point_in_rect(evt.pos, self.pad_rect):
            self.onclick()
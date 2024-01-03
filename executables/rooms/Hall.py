import pygame

from executables.rooms.Room import Room


class Hall(Room):
    def __init__(self, r):
        super().__init__(r)
        quad_surface = pygame.Surface(((w := self.r.constant("useful_width")) * 2,
                                       (h := self.r.constant("useful_height")) * 2))
        quad_surface.blit(self.image, (0, 0))
        quad_surface.blit(self.image, (w, 0))
        quad_surface.blit(self.image, (0, h))
        quad_surface.blit(self.image, (w, h))
        self.image = quad_surface


# --- libraries ---
import pygame
import time
import source.classes.titans as titans  # source/titans.py


def get_nearest(actual, matrix):
    for i in range(8, -1, -1):
        element = matrix[actual][i]
        if element.object:
            if element and titans.Titan.__subclasscheck__(element.object.__class__):
                return element
    return None


class Elemental:
    def __init__(self, info, path, matrix):
        self.health, self.attack_power = info[0], info[1]
        self.matrix = matrix
        self.initial_time = 0
        self.section = None
        self.pos = ()
        self.screen = self.matrix.screen
        self.image = pygame.image.load(path)

    def attack(self):
        if 0 < (time.time() - self.initial_time) % 6 < 0.05:
            temp = get_nearest(self.section.id[0], self.matrix.sections)
            if temp:
                temp.on_attack(self.attack_power)
                print("Elemental attacking", temp.id)

    def die(self):
        # Activate animation for dying
        self.section.object = None

    def update(self):
        if self.health <= 0:
            self.die()
        self.screen.blit(self.image, (self.pos[0] - 6.5, self.pos[1] - 18))


class Air(Elemental):
    def __init__(self, info, path, matrix):
        super().__init__(info, path, matrix)


class Earth(Elemental):
    def __init__(self, info, path, matrix):
        super().__init__(info, path, matrix)


class Water(Elemental):
    def __init__(self, info, path, matrix):
        super().__init__(info, path, matrix)


class Fire(Elemental):
    def __init__(self, info, path, matrix):
        super().__init__(info, path, matrix)

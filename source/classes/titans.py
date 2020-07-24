# --- libraries ---
import pygame
import time
import source.classes.elementals as elementals  # source/elementals.py


def get_nearest(actual, matrix):
    for i in range(actual[1], 9):
        element = matrix[actual[0]][i]
        if element.object:
            if element and elementals.Elemental.__subclasscheck__(element.object.__class__):
                return element
    return None


class Titan:
    def __init__(self, info, matrix, section, path, pos_y,
                 initial_time):  # Titan([health,attack_power,attack_freq],[Matrix,(id init_section)], "path", speed, pos_init) # '''Orc([50, 12, 5], [matrix, (2, 5)], "path/holi.png",  5, (x, y))'''
        self.health, self.attack_power, self.attack_freq, self.move_freq = info[0], info[1], info[2], info[3]
        self.matrix = matrix
        self.initial_time = initial_time
        self.section = section
        self.pos = (self.section.pos[0], pos_y)
        self.screen = self.matrix.screen
        self.speed = 5
        self.current_speed = self.speed
        self.image = pygame.image.load(path)
        self.attacking = False
        self.moved = False

    def move(self):
        if 0 < (time.time() - self.initial_time) % self.move_freq < 0.05:
            identifier = self.section.id
            temp = self.matrix.sections[identifier[0]][identifier[1] + 1]
            if not temp.object and self.moved:
                if temp.id[1] == 8:
                    # GameOverScreen()
                    self.section.game.gameover = True
                    return 0
                self.section.object = None
                self.section = temp
                self.section.object = self
            self.moved = True
        # Activate animation for walking

    def attack(self):
        return  # overridden

    def die(self):
        # Activate animation for dying
        self.section.object = None
        self.section.game.gems += 75

    def update(self):
        if self.section.pos != self.pos:  # titan's current section
            self.attacking = False
            self.current_speed = self.speed
        if self.section.pos <= self.pos and self.current_speed != 0:
            self.pos = (self.section.pos[0], self.section.pos[1])
            self.attacking = True
            self.current_speed = 0
            # Deactivate animation for walking
        if self.health <= 0:
            self.die()
        self.pos = (self.pos[0], self.pos[1] + self.current_speed)
        self.screen.blit(self.image, (self.pos[0] - 6.5, self.pos[1] - 18))


class Skeleton(Titan):
    def __init__(self, info, matrix, section, path, pos_y, initial_time):
        super().__init__(info, matrix, section, path, pos_y, initial_time)

    def attack(self):
        if 0 < (time.time() - self.initial_time) % self.attack_freq < 0.05:
            identifier = self.section.id
            temp = get_nearest(identifier, self.matrix.sections)
            if temp:
                temp.on_attack(self.attack_power)
                print("Skeleton attacking", temp.id)
                # Activate animation for attacking


class Elf(Titan):
    def __init__(self, info, matrix, section, path, pos_y, initial_time):
        super().__init__(info, matrix, section, path, pos_y, initial_time)

    def attack(self):
        if 0 < (time.time() - self.initial_time) % self.attack_freq < 0.05:
            identifier = self.section.id
            temp = get_nearest(identifier, self.matrix.sections)
            if temp:
                temp.on_attack(self.attack_power)
                print("Elf attacking", temp.id)
                # Activate animation for attacking


class Orc(Titan):
    def __init__(self, info, matrix, section, path, pos_y, initial_time):
        super().__init__(info, matrix, section, path, pos_y, initial_time)

    def attack(self):
        if 0 < (time.time() - self.initial_time) % self.attack_freq < 0.05:
            identifier = self.section.id
            temp = self.matrix.sections[identifier[0]][identifier[1]]
            if temp.object:
                temp.on_attack(self.attack_power)
                print("Orc attacking", temp.id)
                # Activate animation for attacking


class Dragon(Titan):
    def __init__(self, info, matrix, section, path, pos_y, initial_time):
        super().__init__(info, matrix, section, path, pos_y, initial_time)

    def attack(self):
        if 0 < (time.time() - self.initial_time) % self.attack_freq < 0.05:
            identifier = self.section.id
            temp = self.matrix.sections[identifier[0]][identifier[1]]
            if temp.object:
                temp.on_attack(self.attack_power)
                print("Dragon attacking", temp.id)
                # Activate animation for attacking

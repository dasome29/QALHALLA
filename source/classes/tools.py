# --- libraries ---
import pygame
import random
import time
import sys
import source.classes.titans as titans  # source/titans.py
import source.classes.elementals as elementals

pygame.init()  # initialize pygame modules

# -- -constants ---
gameClock = pygame.time.Clock()  # tick function arg

keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           # keyboard summary
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN, "a": pygame.K_a,
           "b": pygame.K_b, "c": pygame.K_c, "d": pygame.K_d, "e": pygame.K_e, "f": pygame.K_f, "g": pygame.K_g,
           "h": pygame.K_h, "i": pygame.K_i, "j": pygame.K_j, "k": pygame.K_k, "l": pygame.K_l, "m": pygame.K_m,
           "n": pygame.K_n, "o": pygame.K_o, "p": pygame.K_p, "q": pygame.K_q, "r": pygame.K_r, "s": pygame.K_s,
           "t": pygame.K_t, "u": pygame.K_u, "v": pygame.K_v, "w": pygame.K_w, "x": pygame.K_x, "y": pygame.K_y,
           "z": pygame.K_z, "1": pygame.K_1, "2": pygame.K_2, "3": pygame.K_3, "4": pygame.K_4, "5": pygame.K_5,
           "6": pygame.K_6, "7": pygame.K_7, "8": pygame.K_8, "9": pygame.K_9, "0": pygame.K_0}

# ---fonts---
PfefferMediaeval_font = pygame.font.Font("resources/gui/fonts/PfefferMediaeval.otf", 16)
Insula_font_15 = pygame.font.Font("resources/gui/fonts/Insula.ttf", 15)
Trajan_font_15 = pygame.font.Font("resources/gui/fonts/Trajan.otf", 15)

# ---colors---
white = (255, 255, 255)
black = (0, 0, 0)
ink_color = (40, 18, 12)
blue = (22, 46, 98)


class Section:
    def __init__(self, game, position, identifier):
        self.screen = game.screen
        self.game = game
        self.pos = position
        self.id = identifier
        self.object = None
        self.update_section()

    def update_section(self):
        if self.object:
            self.object.update()

    def on_click(self, cursor):
        name = self.object.__class__.__name__  # returns class name
        if self.object:
            if name == "Gem":
                self.game.gems += self.object.value  # adds gem value to the gem's counter
                self.object = None  # ""
            if elementals.Elemental.__subclasscheck__(self.object.__class__):
                self.object = None
        else:
            if cursor.elemental:
                self.object = cursor.elemental
                cursor.elemental = None
                self.object.section = self
                self.object.pos = self.pos
                self.object.initial_time = time.time()

    def on_attack(self, damage):
        name = type(self.object).__name__
        if name != "Gem":
            self.object.health -= damage
            pygame.mixer.music.load("resources/gui/sounds/hurt.mp3")
            pygame.mixer.music.play(0)


class Matrix:
    def __init__(self, game):
        self.screen = game.screen
        self.game = game
        self.sections = []
        self.create_matrix(0, 0, [])
        self.last_gem = 0
        self.gems = [["resources/gui/props/g5.png", 5], ["resources/gui/props/g25.png", 25],
                     ["resources/gui/props/g50.png", 50], ["resources/gui/props/g100.png", 100]]

    def create_matrix(self, i, j, templist):
        if j < 9:
            if i < 5:
                temp = Section(self.game, (116 + (i * 54), 123 + (j * 50)), (i, j))
                templist.append(temp)
                return self.create_matrix(i, j + 1, templist)
            return 0
        self.sections.append(templist)
        return self.create_matrix(i + 1, 0, [])

    def create_titan(self, titan):
        i = random.randint(0, 4)
        name = titan.__name__
        section = self.sections[i][0]
        if self.available_row(0):
            if not section.object:
                if name == "Skeleton":
                    section.object = titans.Skeleton([5, 2, 10, 3], self, section, "resources/gui/props/t-skeleton.png",
                                                     -20, time.time())
                elif name == "Elf":
                    section.object = titans.Elf([10, 3, 15, 10], self, section, "resources/gui/props/t-elf.png", -20,
                                                time.time())
                elif name == "Orc":
                    section.object = titans.Orc([20, 9, 5, 13], self, section, "resources/gui/props/t-orc.png", -20,
                                                time.time())
                elif name == "Dragon":
                    section.object = titans.Dragon([25, 12, 3, 16], self, section, "resources/gui/props/t-dragon.png",
                                                   -20, time.time())
                return section.object
            return self.create_titan(titan)
        return 0

    def create_elemental(self, elemental):
        name = elemental.__name__
        print(name)
        if self.available(0, 0):
            if name == "Air":
                return elementals.Air([12, 2], "resources/gui/props/e-air.png", self)
            elif name == "Earth":
                return elementals.Earth([14, 4], "resources/gui/props/e-earth.png", self)
            elif name == "Water":
                return elementals.Water([16, 8], "resources/gui/props/e-water.png", self)
            elif name == "Fire":
                return elementals.Fire([18, 12], "resources/gui/props/e-fire.png", self)
        return None

    def create_gem(self, object):
        i = random.randint(0, 4)
        j = random.randint(0, 8)
        section = self.sections[i][j]
        if not section.object:
            if object.__name__ == "Gem":
                section = self.sections[i][j]
                section.object = Gem(self.screen, self.gems[random.randint(0, 3)],
                                     (section.pos[0] + 10.5, section.pos[1] + 8.5))
                return
        return self.create_gem(object)

    def create_object(self, object):
        available = self.available(0, 0)
        if available:
            if object.__name__ == "Gem":
                return self.create_gem(object)
            else:
                if titans.Titan.__subclasscheck__(object):
                    return self.create_titan(object)
                else:
                    return self.create_elemental(object)
        return 0

    def available(self, i, j):
        if j < 9:
            if i < 5:
                if not self.sections[i][j].object:
                    return True
                return self.available(i, j + 1)
            return False
        return self.available(i + 1, 0)

    def get_titans(self, i, j, array):
        if j < 9:
            if i < 5:
                if titans.Titan.__subclasscheck__(self.sections[i][j].object.__class__):
                    array.append(self.sections[i][j].object)
                return self.get_titans(i, j + 1, array)
            return array
        return self.get_titans(i + 1, 0, array)

    def get_elementals(self, i, j, array):
        if j < 9:
            if i < 5:
                if elementals.Elemental.__subclasscheck__(self.sections[i][j].object.__class__):
                    array.append(self.sections[i][j].object)
                return self.get_elementals(i, j + 1, array)
            return array
        return self.get_elementals(i + 1, 0, array)

    def available_row(self, i):
        if i < 5:
            if not self.sections[i][0].object:
                return True
            return self.available_row(i + 1)
        return False

    def update(self):
        for array in self.sections:
            for section in array:
                section.update_section()


class Gem:
    def __init__(self, screen, info, position):
        self.screen = screen
        self.path = info[0]
        self.value = info[1]
        self.pos = position
        self.image = pygame.image.load(self.path)

    def update(self):
        self.screen.blit(self.image, self.pos)


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
        self.elemental = None

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()
        if self.elemental:
            self.elemental.pos = (self.left - 32, self.top - 32)
            self.elemental.screen.blit(self.elemental.image, self.elemental.pos)


class Button(pygame.sprite.Sprite):

    def __init__(self, image1, image2, x, y):
        self.normal = image1
        self.selected = image2
        self.actual_image = self.normal
        self.rect = self.actual_image.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, screen, cursor):
        if cursor.colliderect(self.rect):
            self.actual_image = self.selected
        else:
            self.actual_image = self.normal
        screen.blit(self.actual_image, self.rect)


def tick(fps):  # handle frames using the pygame clock
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == keydict["esc"]) or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gameClock.tick(fps)
    return gameClock.get_fps()


def endwait():  # close window and stop the code execution, using the esc key or with the window close button
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                waiting = False
    pygame.quit()
    exit()


# ---Clock functions---


seconds = 0
minutes = 0


def set_timer(new_minutes, new_seconds):  # Set the time of the clock
    global seconds, minutes
    seconds = new_seconds
    minutes = new_minutes


def clock():  # Input: the global variables, seconds and minutes
    global seconds, minutes  # Output: a string whit the current time in te game in format 00:00
    seconds += 1 / 30
    if seconds > 60:
        seconds = 0
        minutes += 1
        if minutes < 10 and seconds < 10:
            return "0" + str(minutes) + ":0" + str(int(seconds))
        elif minutes < 10:
            return "0" + str(minutes) + ":" + str(int(seconds))
        elif seconds < 10:
            return str(minutes) + ":0" + str(int(seconds))
        else:
            return str(minutes) + ":" + str(int(seconds))
    else:
        if minutes < 10 and seconds < 10:
            return "0" + str(minutes) + ":0" + str(int(seconds))
        elif minutes < 10:
            return "0" + str(minutes) + ":" + str(int(seconds))
        elif seconds < 10:
            return str(minutes) + ":0" + str(int(seconds))
        else:
            return str(minutes) + ":" + str(int(seconds))

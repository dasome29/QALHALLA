# --- libraries ---
import pygame
import datetime
import time
import random
import source.classes.tools as tools  # source/tools.py
import source.classes.menu as menu  # source/menu.py
import source.classes.elementals as elementals
import source.classes.titans as titans

pygame.init()  # pygame initialization


class Game:
    def __init__(self, name, screen, difficulty, gems, start_level, main_menu):
        # --- load resources ---
        self.frame_image = pygame.image.load("resources/gui/props/frame.png")
        self.save_button_image_0 = pygame.image.load("resources/gui/buttons/b0_save.png")
        self.save_button_image_1 = pygame.image.load("resources/gui/buttons/b1_save.png")
        self.muted_button_image_0 = pygame.image.load("resources/gui/buttons/b0_muted.png")
        self.muted_button_image_1 = pygame.image.load("resources/gui/buttons/b1_muted.png")
        self.c0_air = pygame.image.load("resources/gui/buttons/c0_air.png")
        self.c1_air = pygame.image.load("resources/gui/buttons/c1_air.png")
        self.c0_earth = pygame.image.load("resources/gui/buttons/c0_earth.png")
        self.c1_earth = pygame.image.load("resources/gui/buttons/c1_earth.png")
        self.c0_water = pygame.image.load("resources/gui/buttons/c0_water.png")
        self.c1_water = pygame.image.load("resources/gui/buttons/c1_water.png")
        self.c0_fire = pygame.image.load("resources/gui/buttons/c0_fire.png")
        self.c1_fire = pygame.image.load("resources/gui/buttons/c1_fire.png")

        # --- game methods ---
        self.cursor = tools.Cursor()  # Cursor, from the class Cursor in the tools py
        self.screen = screen

        # --- game variables ---
        self.name = name  # stores the battle name
        self.difficulty = difficulty  # stores the battle difficulty
        self.today = datetime.datetime.now()  # stores datetime             # configurar formato
        self.gems = gems  # stores the amount of magic runes
        self.start_level = start_level
        self.started = False
        self.moving = False
        self.gameover = False
        self.frequency = 0
        self.menu = main_menu
        # posicion de elementales (buenos)
        # posicion de titanes (malos)

        # --- save button---
        self.save_button = tools.Button(self.save_button_image_0, self.save_button_image_1, 11, 622)
        # --- muted button---
        self.muted_button = tools.Button(self.muted_button_image_0, self.muted_button_image_1, 432, 622)
        # --- air button---
        self.air_button = tools.Button(self.c0_air, self.c0_air, 99, 582)
        # ---earth button---
        self.earth_button = tools.Button(self.c0_earth, self.c0_earth, 188, 583)
        # ---water button---
        self.water_button = tools.Button(self.c0_water, self.c0_water, 272, 580)
        # ---fire button---
        self.fire_button = tools.Button(self.c0_fire, self.c0_fire, 354, 583)

        print(self.name, self.difficulty, self.today)  # eliminar
        self.load_game()  # return load_game method

    def lvl1(self):  # method, defines the settings for the level 1 screen
        self.screen_state = "lvl1"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/lvl1.jpg")  # background image
        self.level_title = "Nivel 1"  # level ID
        self.grid = tools.Matrix(self)

        self.start_game()  # run the game

    def lvl2(self):  # method, defines the settings for the level 2 screen
        self.screen_state = "lvl2"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/lvl2.jpg")
        self.level_title = "Nivel 2"  # level ID
        self.grid = tools.Matrix(self)

        self.start_game()  # run the game

    def lvl3(self):  # method, defines the settings for the level 3 screen
        self.screen_state = "lvl3"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/lvl3.jpg")  # background image
        self.level_title = "Nivel 3"  # level ID
        self.grid = tools.Matrix(self)

        self.start_game()  # run the game

    def cards_cs(self):  # method, cards control system is in charge of enabling and disabling the purchase options
        if self.gems >= 200:  # enables the four purchase options
            self.air_button = tools.Button(self.c1_air, self.c1_air, 99, 582)
            self.earth_button = tools.Button(self.c1_earth, self.c1_earth, 188, 583)
            self.water_button = tools.Button(self.c1_water, self.c1_water, 272, 580)
            self.fire_button = tools.Button(self.c1_fire, self.c1_fire, 354, 583)
        elif self.gems >= 150:  # disables the fire purchase option
            self.air_button = tools.Button(self.c1_air, self.c1_air, 99, 582)
            self.earth_button = tools.Button(self.c1_earth, self.c1_earth, 188, 583)
            self.water_button = tools.Button(self.c1_water, self.c1_water, 272, 580)
            self.fire_button = tools.Button(self.c0_fire, self.c0_fire, 354, 583)
        elif self.gems >= 100:  # disables fire and water purchase options
            self.air_button = tools.Button(self.c1_air, self.c1_air, 99, 582)
            self.earth_button = tools.Button(self.c1_earth, self.c1_earth, 188, 583)
            self.water_button = tools.Button(self.c0_water, self.c0_water, 272, 580)
            self.fire_button = tools.Button(self.c0_fire, self.c0_fire, 354, 583)
        elif self.gems >= 50:  # disables fire,water and earth purchase options
            self.air_button = tools.Button(self.c1_air, self.c1_air, 99, 582)
            self.earth_button = tools.Button(self.c0_earth, self.c0_earth, 188, 583)
            self.water_button = tools.Button(self.c0_water, self.c0_water, 272, 580)
            self.fire_button = tools.Button(self.c0_fire, self.c0_fire, 354, 583)
        elif self.gems < 50:  # disables all purchase options
            self.air_button = tools.Button(self.c0_air, self.c0_air, 99, 582)
            self.earth_button = tools.Button(self.c0_earth, self.c0_earth, 188, 583)
            self.water_button = tools.Button(self.c0_water, self.c0_water, 272, 580)
            self.fire_button = tools.Button(self.c0_fire, self.c0_fire, 354, 583)

    def load_game(self):  # method, returns level according to start_level argument
        if self.start_level == "lvl1":
            self.lvl1()
        elif self.start_level == "lvl2":
            self.lvl2()
        elif self.start_level == "lvl3":
            self.lvl3()

    def entity_actions(self):
        elementals_array = self.grid.get_elementals(0, 0, [])
        for elemental in elementals_array:
            elemental.attack()
        titans_array = self.grid.get_titans(0, 0, [])
        for titan in titans_array:
            titan.attack()
            titan.move()

    # def titan_move(self, initial):
    #     titans_array = self.grid.get_titans(0, 0, [])
    #     if 7 < (time.time() - initial) % 20 < 7.05:
    #         if self.moving:
    #             for titan in titans_array:
    #                 if titan.__class__.__name__ == "Skeleton":
    #                     titan.move()
    #
    #     if 10 < (time.time() - initial) % 20 < 10.05:
    #         if self.moving:
    #             for titan in titans_array:
    #                 if titan.__class__.__name__ == "Elf":
    #                     titan.move()
    #     if 13 < (time.time() - initial) % 20 < 13.05:
    #         if self.moving:
    #             for titan in titans_array:
    #                 if titan.__class__.__name__ == "Orc":
    #                     titan.move()
    #     if 16 < (time.time() - initial) % 20 < 16.05:
    #         if self.moving:
    #             for titan in titans_array:
    #                 if titan.__class__.__name__ == "Dragon":
    #                     titan.move()
    #         self.moving = True

    def titan_attack(self, initial):
        titans_array = self.grid.get_titans(0, 0, [])
        if 7 < (time.time() - initial) % 20 < 7.05:
            if self.moving:
                for titan in titans_array:
                    if titan.__class__.__name__ == "Skeleton":
                        titan.attack()

        if 10 < (time.time() - initial) % 20 < 10.05:
            if self.moving:
                for titan in titans_array:
                    if titan.__class__.__name__ == "Elf":
                        titan.attack()
        if 13 < (time.time() - initial) % 20 < 13.05:
            if self.moving:
                for titan in titans_array:
                    if titan.__class__.__name__ == "Orc":
                        titan.attack()
        if 16 < (time.time() - initial) % 20 < 16.05:
            if self.moving:
                for titan in titans_array:
                    if titan.__class__.__name__ == "Dragon":
                        titan.attack()
            self.moving = True

    def generator(self, initial):
        if 0 < (time.time() - initial) % 30 < 0.05:
            self.grid.create_object(tools.Gem)
        if 0 < (time.time() - initial) % (30 - (30 * self.frequency)) < 0.05:
            self.grid.create_object(titans.Skeleton)
        if 50 < (time.time() - initial) % (70 - (70 * self.frequency)) < 50.05:
            if self.started:
                self.grid.create_object(titans.Elf)
            self.started = True
        if 80 < (time.time() - initial) % (90 - (90 * self.frequency)) < 80.05:
            if self.started:
                self.grid.create_object(titans.Orc)
        if 100 < (time.time() - initial) % (120 - (120 * self.frequency)) < 100.05:
            if self.started:
                self.grid.create_object(titans.Dragon)

    def start_game(self):  # method, run the game
        fps = pygame.time.Clock()
        initial = time.time()
        while True:
            pygame.display.update()
            fps.tick(30)
            if self.gameover:
                after_game = AfterGame(self.screen, self.name, int(time.time() - initial), self.menu)
                after_game.winner()
                after_game.setup()
                print("GAME OVER")
                break
            else:
                self.generator(initial)
                self.entity_actions()
                for event in pygame.event.get():
                    # stops code execution by pressing the window button or the esc key
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    # --- cursor-events ---
                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        if self.cursor.colliderect(self.save_button.rect):
                            print("save")
                        elif self.cursor.colliderect(self.muted_button.rect):
                            print("muted")
                        elif self.cursor.colliderect(self.air_button.rect) and (self.gems >= 50):
                            self.cursor.elemental = self.grid.create_object(elementals.Air)
                            self.gems -= 50
                        elif self.cursor.colliderect(self.earth_button.rect) and (self.gems >= 100):
                            self.cursor.elemental = self.grid.create_object(elementals.Earth)
                            self.gems -= 100
                        elif self.cursor.colliderect(self.water_button.rect) and (self.gems >= 150):
                            self.cursor.elemental = self.grid.create_object(elementals.Water)
                            self.gems -= 150
                        elif self.cursor.colliderect(self.fire_button.rect) and (self.gems >= 200):
                            self.cursor.elemental = self.grid.create_object(elementals.Fire)
                            self.gems -= 200

                        x, y = event.pos
                        for array in self.grid.sections:  # handles events within the matrix zone
                            for section in array:
                                location = section.pos  # get event position
                                if (location[0] < x < location[0] + 51) and (
                                        location[1] < y < location[1] + 48):  # events within the box range
                                    section.on_click(self.cursor)

                # --- graphics ---

                # --- text ---
                self.level = tools.Trajan_font_15.render(self.level_title, True, (tools.white))
                self.battlename = tools.Insula_font_15.render(self.name, True, tools.black)
                self.gems_label = tools.Insula_font_15.render(str(self.gems), True, tools.black)
                self.time = tools.Insula_font_15.render(tools.clock(), True, tools.black)
                # --- show ---
                self.screen.blit(self.background, (0, 0))
                self.grid.update()
                self.cursor.update()
                self.screen.blit(self.frame_image, (0, 0))
                self.screen.blit(self.level, (219, 39))
                self.screen.blit(self.battlename, (72, 76))
                self.screen.blit(self.gems_label, (223, 76))
                self.screen.blit(self.time, (380, 76))
                # --- update ---
                self.save_button.update(self.screen, self.cursor)
                self.muted_button.update(self.screen, self.cursor)
                self.air_button.update(self.screen, self.cursor)
                self.earth_button.update(self.screen, self.cursor)
                self.water_button.update(self.screen, self.cursor)
                self.fire_button.update(self.screen, self.cursor)

                self.cards_cs()

                if self.screen_state == "lvl1":
                    pass
                elif self.screen_state == "lvl2":
                    pass
                elif self.screen_state == "lvl3":
                    pass


class AfterGame:
    def __init__(self, screen, name, duration, main_screen):
        # --- load resources ---
        self.backgrounds = ["resources/gui/backgrounds/gameover.jpg", "resources/gui/backgrounds/winner.jpg"]
        self.shields = ["resources/gui/props/go_1.png", "resources/gui/props/go_2.png", "resources/gui/props/go_3.png",
                        "resources/gui/props/go_4.png", "resources/gui/props/go_5.png"]
        self.trophies = ["resources/gui/props/win_1.png", "resources/gui/props/win_2.png",
                         "resources/gui/props/win_3.png", "resources/gui/props/win_4.png"]
        self.button_menu_st0 = pygame.image.load("resources/gui/buttons/b0_menu.png")  # normal state image
        self.button_menu_st1 = pygame.image.load("resources/gui/buttons/b1_menu.png")  # active state image
        # --- AfterGame methods ---
        self.cursor = tools.Cursor()  # Cursor, from the class Cursor in the tools py
        # --- AfterGame variables ---
        self.screen = screen
        self.name = name
        self.time = duration
        self.main_screen = main_screen
        # --- button ---
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)

    def game_over(self):
        self.main_screen.screen_state = "game_over"
        self.background = pygame.image.load(self.backgrounds[0])
        self.shield = pygame.image.load(self.shields[random.randint(0, 4)])

    def winner(self):
        self.main_screen.screen_state = "winner"
        self.background = pygame.image.load(self.backgrounds[1])
        self.trophy = pygame.image.load(self.trophies[random.randint(0, 3)])


    def setup(self):
        while True:
            pygame.display.update()
            self.screen.blit(self.background, (0, 0))  # background
            # --- cursor events ---
            for event in pygame.event.get():
                self.cursor.update()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # --- cursor events ---
                    if self.main_screen.screen_state == "game_over":
                        if self.cursor.colliderect(self.menu_button):
                            menu.MenuScreen()
                    elif self.main_screen.screen_state == "winner":
                        if self.cursor.colliderect(self.menu_button):
                            menu.MenuScreen()
            # --- graphics ---
            if self.main_screen.screen_state == "game_over":
                self.menu_button.update(self.screen, self.cursor)
                self.screen.blit(self.shield, (195, 275))  # shield
            elif self.main_screen.screen_state == "winner":
                self.menu_button.update(self.screen, self.cursor)
                self.screen.blit(self.trophy, (195, 275))  # trophy

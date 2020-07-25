# --- libraries ---
import pygame
import source.classes.tools as tools  # source/tools.py
import source.classes.game as game  # source/game.py

pygame.init()  # initialize pygame modules


# ---game-screens---
class MenuScreen:
    def __init__(self):
        # --- load resources ---
        # --- main srceen button images ---
        self.button_play_st0 = pygame.image.load("resources/gui/buttons/b0_play.png")  # normal state image
        self.button_play_st1 = pygame.image.load("resources/gui/buttons/b1_play.png")  # active state image
        self.button_load_st0 = pygame.image.load("resources/gui/buttons/b0_load.png")  # normal state image
        self.button_load_st1 = pygame.image.load("resources/gui/buttons/b1_load.png")  # active state image
        self.button_scores_st0 = pygame.image.load("resources/gui/buttons/b0_scores.png")  # normal state image
        self.button_scores_st1 = pygame.image.load("resources/gui/buttons/b1_scores.png")  # active state image
        self.button_help_st0 = pygame.image.load("resources/gui/buttons/b0_help.png")  # normal state image
        self.button_help_st1 = pygame.image.load("resources/gui/buttons/b1_help.png")  # active state image
        self.button_credits_st0 = pygame.image.load("resources/gui/buttons/b0_credits.png")  # normal state image
        self.button_credits_st1 = pygame.image.load("resources/gui/buttons/b1_credits.png")  # active state image
        # --- menu button images ---
        self.button_menu_st0 = pygame.image.load("resources/gui/buttons/b0_menu.png")  # normal state image
        self.button_menu_st1 = pygame.image.load("resources/gui/buttons/b1_menu.png")  # active state image
        # --- help screen button images ---
        self.b_page_R = pygame.image.load("resources/gui/buttons/b_page_R.png")
        self.b_page_L = pygame.image.load("resources/gui/buttons/b_page_L.png")
        self.b_page_0 = pygame.image.load("resources/gui/buttons/b_page_0.png")
        # --- difficulty screen button images ---
        self.button_easy_0 = pygame.image.load("resources/gui/buttons/b0_difficulty.png")  # normal state image
        self.button_easy_1 = pygame.image.load("resources/gui/buttons/b1_easy.png")  # active state image
        self.button_regular_0 = pygame.image.load("resources/gui/buttons/b0_difficulty.png")  # normal state image
        self.button_regular_1 = pygame.image.load("resources/gui/buttons/b1_regular.png")  # active state image
        self.button_hard_0 = pygame.image.load("resources/gui/buttons/b0_difficulty.png")  # normal state image
        self.button_hard_1 = pygame.image.load("resources/gui/buttons/b1_hard.png")  # active state image
        # --- player screen button images ---
        self.button_start_game_st0 = pygame.image.load("resources/gui/buttons/b0_game.png")  # normal state image
        self.button_start_game_st1 = pygame.image.load("resources/gui/buttons/b1_game.png")  # active state image
        self.next_window_0 = pygame.image.load("resources/gui/buttons/b0_next.png")  # normal state image
        self.next_window_1 = pygame.image.load("resources/gui/buttons/b1_next.png")  # active state image

        self.screen = pygame.display.set_mode((500, 700))  # screen size graphic method
        self.cursor = tools.Cursor()  # cursor graphic method from tools.py
        self.update_screen = pygame.display.update()
        self.difficulty = None
        self.name_text = ""
        self.gems = 0

        self.screen_state = "menu"

        self.number_page = 0

    def menu(self):
        self.screen_state = "menu"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/menu.jpg")  # background image
        # --- buttons ---
        # "INICIAR BATALLA" button graphic method from tools
        self.play_button = tools.Button(self.button_play_st0, self.button_play_st1, 132, 305)
        # "REANUDAR BATALLA" button graphic method from tools
        self.load_button = tools.Button(self.button_load_st0, self.button_load_st1, 132, 370)
        # "HISTORIAL DE BATALLAS" button graphic method from tools
        self.scores_button = tools.Button(self.button_scores_st0, self.button_scores_st1, 132, 435)
        # "AYUDA" button graphic method from tools
        self.help_button = tools.Button(self.button_help_st0, self.button_help_st1, 132, 500)
        # "CREDITOS" button graphic method from tools
        self.credits_button = tools.Button(self.button_credits_st0, self.button_credits_st1, 132, 565)

    def load(self):
        self.screen_state = "load_game"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/load.jpg")  # background image
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)

    def scores(self):
        self.screen_state = "scores"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/scores.jpg")  # background image
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375,
                                        15)  # Button graphic method from tools

    def help(self):
        self.screen_state = "help"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/help.jpg")  # background image
        self.number_page = 0  # stores the current book page
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)
        self.left_button = tools.Button(self.b_page_0, self.b_page_L, 17, 175)  # Button to go previous page
        self.right_button = tools.Button(self.b_page_0, self.b_page_R, 257, 175)  # button to go next page

    def credits(self):
        self.screen_state = "credits"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/credits.jpg")  # background image
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)

    def select_difficulty(self):
        self.screen_state = "select_difficulty"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/power.jpg")  # background image
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)
        # "MONJE - MAESTRO - AVATAR" button graphic method from tools
        self.easy_button = tools.Button(self.button_easy_1, self.button_easy_0, 127, 318)
        self.regular_button = tools.Button(self.button_regular_1, self.button_regular_0, 217, 318)
        self.hard_button = tools.Button(self.button_hard_1, self.button_hard_0, 308, 318)
        # "SIGUIENTE" button graphic method from tools
        self.next_window_button = tools.Button(self.next_window_0, self.next_window_1, 200, 462)

    def player(self):
        self.screen_state = "player"  # screen ID
        self.background = pygame.image.load("resources/gui/backgrounds/player.jpg")  # background image
        # --- buttons ---
        # "MENU" button graphic method from tools
        self.menu_button = tools.Button(self.button_menu_st0, self.button_menu_st1, 375, 15)
        # "JUGAR" button graphic method from tools
        self.game_button = tools.Button(self.button_start_game_st0, self.button_start_game_st1, 197, 464)
        # --- entry-text ---
        self.name_text = "INSERTE NOMBRE DE BATALLA"  # instruction text
        self.name = ""

    def check_box(self, name):  # method, checks data entered by user
        if name == "" or name == "INSERTE NOMBRE DE BATALLA":
            return False
        elif name[0] == " ":
            return self.check_box(name[1:])
        else:
            return True

    def start_game(self):
        icon = pygame.image.load("resources/gui/props/icon.png")  # window's icon image
        pygame.display.set_icon(icon)  # window's icon
        pygame.display.set_caption("QALHALLA")  # window's title
        fps = pygame.time.Clock()  # handle events using the pygame-clock

        while True:
            pygame.display.update()
            self.screen.blit(self.background, (0, 0))  # background
            fps.tick(30)

            for event in pygame.event.get():
                self.cursor.update()
                #  stops code execution by pressing the window button or the esc key
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # --- events ---
                # --- key-events ---
                elif self.screen_state == "player" and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:  # erase character
                        self.name_text = self.name_text[:-1]
                        self.name = self.name[:-1]
                    elif len(self.name) < 10 and (not event.key == pygame.K_RETURN):  # checks the name length
                        self.name += event.unicode  # records a letter in the name constant
                        self.name_text = self.name  # deletes the instruction text "Inserte nombre de batalla"

                # --- cursor events ---
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen_state == "menu":
                        if self.cursor.colliderect(self.play_button):
                            menu_screen.select_difficulty()
                        elif self.cursor.colliderect(self.load_button):
                            menu_screen.load()
                        elif self.cursor.colliderect(self.scores_button):
                            menu_screen.scores()
                        elif self.cursor.colliderect(self.help_button):
                            menu_screen.help()
                        elif self.cursor.colliderect(self.credits_button):
                            menu_screen.credits()
                    elif self.screen_state == "load_game":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()
                    elif self.screen_state == "scores":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()
                    elif self.screen_state == "help":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()
                        elif self.cursor.colliderect(self.right_button) and (self.number_page < 6):
                            self.number_page += 1
                        elif self.cursor.colliderect(self.left_button) and (self.number_page > 0):
                            self.number_page -= 1

                    elif self.screen_state == "credits":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()

                    elif self.screen_state == "select_difficulty":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()
                        elif self.cursor.colliderect(self.easy_button):
                            self.difficulty = "Monje"
                            # Redraw the difficulty buttons
                            self.easy_button = tools.Button(self.button_easy_1, self.button_easy_1, 127, 318)
                            self.regular_button = tools.Button(self.button_regular_0, self.button_regular_0, 217, 318)
                            self.hard_button = tools.Button(self.button_hard_0, self.button_hard_0, 308, 318)

                        elif self.cursor.colliderect(self.regular_button):

                            self.difficulty = "Maestro"

                            self.easy_button = tools.Button(self.button_easy_0, self.button_easy_0, 127, 318)
                            self.regular_button = tools.Button(self.button_regular_1, self.button_regular_1, 217, 318)
                            self.hard_button = tools.Button(self.button_hard_0, self.button_hard_0, 308, 318)

                        elif self.cursor.colliderect(self.hard_button):

                            self.difficulty = "Avatar"

                            self.easy_button = tools.Button(self.button_easy_0, self.button_easy_0, 127, 318)
                            self.regular_button = tools.Button(self.button_regular_0, self.button_regular_0, 217, 318)
                            self.hard_button = tools.Button(self.button_hard_1, self.button_hard_1, 308, 318)

                        elif self.cursor.colliderect(self.next_window_button) and isinstance(self.difficulty, str):
                            self.screen_state = "player"
                            menu_screen.player()

                    elif self.screen_state == "player":
                        if self.cursor.colliderect(self.menu_button):
                            menu_screen.menu()

                        elif self.cursor.colliderect(self.game_button) and self.check_box(self.name_text):
                            tools.set_timer(0, 0)  # set the timer to 00:00

                            self.gems = 250
                            self.start_level = "lvl1"
                            self.screen_state = "game"

            # --- graphics ---
            if self.screen_state == "menu":
                self.play_button.update(self.screen, self.cursor)
                self.load_button.update(self.screen, self.cursor)
                self.scores_button.update(self.screen, self.cursor)
                self.help_button.update(self.screen, self.cursor)
                self.credits_button.update(self.screen, self.cursor)
            elif self.screen_state == "load_game":
                self.menu_button.update(self.screen, self.cursor)
            elif self.screen_state == "scores":
                self.menu_button.update(self.screen, self.cursor)

                # ---Help graphics elemtens---
            elif self.screen_state == "help":

                self.book_image = pygame.image.load("resources/gui/props/book_" + str(self.number_page) + ".png")
                self.menu_button.update(self.screen, self.cursor)
                self.screen.blit(self.book_image, (17, 175))
                self.left_button.update(self.screen, self.cursor)
                self.right_button.update(self.screen, self.cursor)

            elif self.screen_state == "credits":
                self.menu_button.update(self.screen, self.cursor)

            elif self.screen_state == "player":
                self.menu_button.update(self.screen, self.cursor)
                self.game_button.update(self.screen, self.cursor)
                text = tools.PfefferMediaeval_font.render(self.name_text, True, tools.ink_color)  # battle's name text
                self.screen.blit(text, (132, 338))

            elif self.screen_state == "select_difficulty":
                self.easy_button.update(self.screen, self.cursor)
                self.regular_button.update(self.screen, self.cursor)
                self.hard_button.update(self.screen, self.cursor)
                self.menu_button.update(self.screen, self.cursor)
                self.next_window_button.update(self.screen, self.cursor)

            elif self.screen_state == "game":
                game.Game(self.name_text, self.screen, self.difficulty, self.gems, self.start_level, self)


menu_screen = MenuScreen()
menu_screen.menu()
menu_screen.start_game()

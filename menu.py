from game import Game
import config as c
import sys
from button import Button
from text_object import TextObject
import colors
import pygame
import sqlite3


class Menu(Game):
    def __init__(self):
        super().__init__('Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.menu_buttons = []
        self.nick = [i for i in open("name_user.txt", "r")][0]
        self.user_text = TextObject(c.screen_width - 100, 30, lambda: self.nick, colors.WHITE, c.font_name, c.font_size)
        self.user_text.draw(self.surface)
        self.objects.append(self.user_text)
        self.user_rec = TextObject(20, 30, lambda: str(0), colors.WHITE, c.font_name, c.font_size)
        self.user_rec.draw(self.surface)
        self.objects.append(self.user_rec)
        self.input = pygame.Rect(c.screen_width - 120, 30, 100, 30)
        self.input_nick = ""
        self.active = False

    c = 0
    def create_menu(self, c_menu):
        def on_play(button):
            c_menu.game_over = False
            if self.c == 0:
                c_menu.create_menu()
                self.c += 1
            c_menu.run()

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False

        
        
        start_btns = (('PLAY', on_play), ('QUIT', on_quit))

        def handle_input_box(type, pos):
            if type == pygame.MOUSEBUTTONDOWN:
                if self.input.collidepoint(pos):
                    self.active = not self.active
                else:
                    self.active = False
                    self.input_nick = ""
                    self.objects.remove(self.user_text)
                    self.user_text = TextObject(c.screen_width - 100, 30, lambda: self.nick, colors.WHITE, c.font_name, c.font_size)
                    self.user_text.draw(self.surface)
                    self.objects.append(self.user_text)
            

        self.mouse_handlers.append(handle_input_box)

        for i, (text, click_handler) in enumerate(start_btns):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       padding=5)

            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_nick = self.input_nick[:-1]
                    elif event.key == 13:
                        self.nick = self.input_nick
                        txt = open("name_user.txt", "w")
                        txt.write(self.nick)
                        txt.close()
                        with sqlite3.connect("achivements") as con:
                            cur = con.cursor()
                            res = cur.execute("""select name from users""").fetchall()
                            res = [i[0] for i in res]
                            if self.nick not in res:
                                cur.execute("""insert into users (name) values("{}")""".format(self.nick))
                                cur.execute("""insert into scores (id_user, max_score) values(
                                            (select id_user from users where name = "{}"), 0)""".format(self.nick))
                    else:
                        self.input_nick += event.unicode                   
                    self.objects.remove(self.user_text)
                    self.user_text = TextObject(c.screen_width - 100, 30, lambda: self.input_nick, colors.WHITE, c.font_name, c.font_size)
                    self.user_text.draw(self.surface)
                    self.objects.append(self.user_text)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)
            
    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
            self.handle_events()
            self.update()
            self.draw()
            if self.active:
                pygame.draw.rect(self.surface, colors.WHITE, self.input, 2)
            else:
                pygame.draw.rect(self.surface, colors.BLACK, self.input, 2)
                
            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def update(self):
        super().update()
        with sqlite3.connect("achivements") as con:
            cur = con.cursor()
            res = cur.execute("""select max_score from scores 
                              where id_user = (select id_user from users 
                              where name = "{}")""".format(self.nick)).fetchall()
            self.objects.remove(self.user_rec)
            self.user_rec = TextObject(20, 30, lambda: str(res[0][0]), colors.WHITE, c.font_name, c.font_size)
            self.user_rec.draw(self.surface)
            self.objects.append(self.user_rec)


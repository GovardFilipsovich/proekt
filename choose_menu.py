from menu import Menu
from levels_menu import Levels_menu
import config as c
from button import Button
from arcade import Arcade
from text_object import TextObject
import colors

class Choose_menu(Menu):
    def __init__(self):
        super().__init__()
        

    def create_menu(self):
        def on_arcade(button):
            breakout = Arcade()
            self.game_over = False
            breakout.__init__()
            breakout.is_game_running = True
            breakout.start_level = True
            breakout.run()

        def on_levels(button):
            if self.c == 0:
                l_menu = Levels_menu()
                l_menu.create_menu()
            l_menu.run()


        def on_menu(button):
            self.game_over = True
            self.is_game_running = False



        start_btns = (('Arcade', on_arcade), ('Levels', on_levels), ('Menu', on_menu))
        local_config = ([300, 250, 80, 50], [400, 250, 80, 50], [350, 305, 80, 50])

        for i, (text, click_handler) in enumerate(start_btns):
            b = Button(*local_config[i],
                       text,
                       click_handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def update(self):
        super().update()
        self.objects.remove(self.user_text)
        self.nick = [i for i in open("name_user.txt", "r")][0]
        self.user_text = TextObject(c.screen_width - 100, 30, lambda: self.nick, colors.WHITE, c.font_name, c.font_size)
        self.user_text.draw(self.surface)
        self.objects.append(self.user_text)

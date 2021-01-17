from game import Game
import config as c
from button import Button
from choose_menu import Choose_menu
class Menu(Game):
    def __init__(self):
        super().__init__('Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.menu_buttons = []

    def create_menu(self):
        def on_play(button):
            self.game_over = False
            menu = Choose_menu()
            menu.create_menu()
            menu.run()

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False

        start_btns = (('PLAY', on_play), ('QUIT', on_quit))

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
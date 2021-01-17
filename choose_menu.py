from game import Game
import config as c
from button import Button
from arcade import Arcade

class Choose_menu(Game):
    def __init__(self):
        super().__init__('Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.menu_buttons = []

    def create_menu(self):
        def on_arcade(button):
            breakout = Arcade()
            self.game_over = False
            breakout.__init__()
            breakout.is_game_running = True
            breakout.start_level = True
            breakout.run()

        def on_levels(button):
            pass

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

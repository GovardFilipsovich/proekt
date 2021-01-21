from menu import Menu
from button import Button
from image_button import Image_button
from levels import Levels
import config as c
levels = {1:[[-1,5,5,5,5,5,5,-1],
               [5,5,-1,5,5,-1,5,5],
               [5,-1,-1,5,5,-1,-1,5],
               [-1,5,-1,5,5,-1,5,-1],
               [5,5,-1,-1,-1,-1,5,5]],
          2:[[-1,-1,-1,5,5,-1,-1,-1], 
               [-1,5,5,5,5,5,5,-1], 
               [5,5,5,5,5,5,5,5], 
               [5,5,5,5,5,5,5,5], 
               [-1,-1,-1,5,5,-1,-1,-1], 
               [-1,-1,-1,5,5,-1,-1,-1],
               [-1,-1,5,5,5,5,-1,-1]],
          3:[[5,-1,-1,-1,5,-1,-1,-1,5],
             [-1,5,-1,5,1,5,-1,5,-1],
             [-1,-1,5,1,1,1,5,-1,-1],
             [-1,5,5,1,5,1,5,5,-1],
             [-1,5,5,1,5,1,5,5,-1],
             [-1,-1,5,1,1,1,5,-1,-1],
             [-1,5,-1,5,1,5,-1,5,-1],
             [5,-1,-1,-1,5,-1,-1,-1,5]],
          4:[[1, -1, -1, -1, -1, -1, -1, -1, 1], 
             [5,1,5,-1,-1,-1,5,1,5],
             [-1,5,1,-1,3,-1,1,5,-1],
             [-1,-1,5,1,-1,1,5,-1,-1], 
             [-1,-1,-1,5,1,5,-1,-1,-1], 
             [-1,-1,-1,0,1,0,-1,-1,-1], 
             [-1,-1,-1,-1,0,-1,-1,-1,-1]],
          5:[[-1,-1,5,5,-1,-1,-1,5,3,3],
             [-1,5,1,1,5,-1,-1,-1,5,3],
             [5,1,1,1,1,5,-1,-1,-1,5],
             [5,1,1,1,1,5],
             [5,1,1,1,1,5],
             [5,1,1,1,1,5],
             [5,1,1,1,1,5],
             [-1,5,1,1,5],
             [-1,-1,5,5]]}

class Levels_menu(Menu):
    def __init__(self):
        super().__init__()

    def create_menu(self):

        def on_back(button):
            self.game_over = True
            self.is_game_running = False

        def on_level(button):
            con = levels[button.num]
            breakout = Levels(con)
            self.game_over = False
            breakout.is_game_running = True
            breakout.start_level = True
            breakout.run()

        b = Button(0, c.screen_height - c.menu_button_h,
                       c.menu_button_w,
                       c.menu_button_h,
                       'Back',
                       on_back,
                       padding=5)
        x = 150
        y = 90
        count = 0
        for i in range(len(levels.keys())):
            b1 = Image_button(x + count * (150 + 10), y,
                           150,
                           150,
                           "images/level_{}.png".format(str(i + 1)),
                           on_level,
                           padding=5)
            count += 1
            if i == 2:
                count = 0
                x = 220
                y += 160
            self.objects.append(b1)
            self.menu_buttons.append(b1)
            self.mouse_handlers.append(b1.handle_mouse_event)


        self.objects.append(b)
        self.menu_buttons.append(b)
        self.mouse_handlers.append(b.handle_mouse_event)
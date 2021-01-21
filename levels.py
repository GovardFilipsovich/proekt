from breakout import Breakout
from game import Game
import config as c
import pygame
import colors
import os
from brick import Brick

special_effects = dict(
    long_paddle=(colors.ORANGE,
                 lambda g: g.paddle.bounds.inflate_ip(c.paddle_width // 2, 0),
                 lambda g: g.paddle.bounds.inflate_ip(+c.paddle_width // 2, 0)),
    slow_ball=(colors.AQUAMARINE2,
               lambda g: g.change_ball_speed(2),
               lambda g: g.change_ball_speed(-1)),
    tripple_points=(colors.DARKSEAGREEN4,
                    lambda g: g.set_points_per_brick(3),
                    lambda g: g.set_points_per_brick(1)),
    extra_life=(colors.GOLD1,
                lambda g: g.add_life(),
                lambda g: None))

assert os.path.isfile('sound_effects/brick_hit.wav')

class Levels(Breakout):
    def __init__(self, config):
        Game.__init__(self, 'Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.sound_effects = {name: pygame.mixer.Sound(sound) for name, sound in c.sounds_effects.items()}
        self.reset_effect = None
        self.effect_start_time = None
        self.score = 0
        self.lives = c.initial_lives
        self.start_level = False
        self.paddle = None
        self.bricks = None
        self.ball = None
        self.menu_buttons = []
        self.is_game_running = False
        self.create_objects(config)
        self.points_per_brick = 1

    def create_objects(self, config):
        self.create_bricks(config)
        self.create_paddle()
        self.create_ball()
        self.create_labels()

    def create_bricks(self, config):
        w = c.brick_width
        h = c.brick_height
        brick_count = c.screen_width // (w + 1)
        offset_x = (c.screen_width - brick_count * (w + 1) // 2 ) // 2

        bricks = []
        for row, i in enumerate(config):
            for col, j in enumerate(i):
                if j != -1:
                    effect = None
                    brick_color = c.brick_color
                    index = j
                    if index < len(special_effects):
                        brick_color, start_effect_func, reset_effect_func = list(special_effects.values())[index]
                        effect = start_effect_func, reset_effect_func

                    brick = Brick(offset_x + col * (w + 1),
                                  c.offset_y + row * (h + 1),
                                  w,
                                  h,
                                  brick_color,
                                  effect)
                    bricks.append(brick)
                    self.objects.append(brick)
        self.bricks = bricks
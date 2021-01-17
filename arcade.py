from breakout import Breakout

class Arcade(Breakout):
    def update(self):
        if not self.bricks:
            self.create_bricks()
            return
        super().update()
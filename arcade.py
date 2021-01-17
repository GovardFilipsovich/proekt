from breakout import Breakout

class Arcade(Breakout):
    count = 0
    sc = -1
    def update(self):
        if not self.bricks:
            self.create_bricks()
            sp = self.ball.speed
            self.objects.remove(self.ball)
            self.create_ball()
            self.ball.speed = sp
            return
        super().update()
        print(self.ball.speed, self.score)
        if self.score % 5 == 0 and self.sc != self.score:
            self.sc = self.score
            self.ball.speed = (self.ball.speed[0], self.ball.speed[1] + 1)
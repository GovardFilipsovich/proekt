from breakout import Breakout
import sqlite3

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
        if self.game_over:
            with sqlite3.connect("achivements") as con:
                cur = con.cursor()
                name = [i for i in open("name_user.txt", "r")][0]
                res = cur.execute("""select max_score from scores 
                                  where id_user = (select id_user from users 
                                  where name = "{}") """.format(name)).fetchone()
                print(res)
                if self.score > res[0]:
                    cur.execute("""update scores set max_score = {} 
                                where id_user = (
                                select id_user from users where name = "{}")""".format(self.score, name))
        if self.score % 5 == 0 and self.sc != self.score:
            self.sc = self.score
            self.ball.speed = (self.ball.speed[0], self.ball.speed[1] + 1)
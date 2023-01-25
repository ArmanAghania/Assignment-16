import random
import arcade
from ball import Ball
from rocket import Rocket

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title='Arcade Pong V1.0')
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.player1 = Rocket(40, self.height//2, arcade.color.RED, "Mo Lang")
        self.player2 = Rocket(self.width - 40, self.height//2, arcade.color.BLUE, 'Arman')
        self.ball = Ball(self)
        self.playerlist = arcade.SpriteList()
        self.playerlist.append(self.player1)
        self.playerlist.append(self.player2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width - 30, self.height - 30, arcade.color.BLUE, border_width=10)
        arcade.draw_line(self.width//2, 30, self.width//2, self.height - 30, arcade.color.WHITE, line_width=10)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        arcade.draw_text(f'Player Score: {self.player1.score}       Computer Score: {self.player2.score}',30, 30, arcade.color.BLACK, 30, 1, 'left', "calibri", True)

        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player1.height < y < self.height - self.player1.height:
            self.player1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player2.move(self, self.ball)

        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30:
            self.ball.change_y *= -1

        if abs(self.ball.center_x - self.width//2) < self.width//4:
            self.ball.allow_hit = True
    
        if arcade.check_for_collision_with_list(self.ball, self.playerlist) and self.ball.allow_hit:
            self.ball.change_x *= -1
            self.ball.allow_hit = False

        if self.ball.center_x < 0:
            self.player2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width:
            self.player1.score += 1
            del self.ball
            self.ball = Ball(self)

game = Game()
arcade.run()
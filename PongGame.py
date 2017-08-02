
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from elements.ball import Ball
from elements.paddle import Paddle


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(20, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    
    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)


        # bounce off top and bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < self.x) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        
        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(20, 0))
        
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-20, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/6.0)
        return game


if __name__ == "__main__":
    PongApp().run()


from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class Paddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):

        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
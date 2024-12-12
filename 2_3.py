import pyxel
import pymunk

WIDTH, HEIGHT = 160, 120
INIT_POS = WIDTH // 2, 0
FPS = 30
BALL_PROPERTY = 1, float('inf') #0 質量, 慣性モーメント

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS, title="自由落下運動")
        self.space = pymunk.Space() #1
        self.space.gravity = (0, 900) #2
        self.create_ball(*INIT_POS)
        pyxel.run(self.update, self.draw)

    def create_ball(self, x, y):
        self.ball = pymunk.Body(*BALL_PROPERTY) #3
        self.ball.position = (x, y) #4
        self.space.add(self.ball) #5

    def update(self):
        if self.ball.position[1] > HEIGHT:
            self.create_ball(*INIT_POS)
        self.space.step(1 / FPS) #6

    def draw(self):
        pyxel.cls(0)
        x, y = self.ball.position #7
        pyxel.circ(x, y, 5, 8)

App()
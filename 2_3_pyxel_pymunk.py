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
        self.ball_body = pymunk.Body(*BALL_PROPERTY) #3
        self.ball_body.position = (x, y) #4
        self.space.add(self.ball_body) #5

    def update(self):
        self.space.step(1 / FPS) #6
        if self.ball_body.position[1] > HEIGHT:
            self.create_ball(*INIT_POS)

    def draw(self):
        pyxel.cls(0)
        x, y = self.ball_body.position #7
        pyxel.circ(x, y, 5, 8)

App()
import pyxel

WIDTH, HEIGHT = 160, 120
INIT_POS = WIDTH // 2, 0
FPS = 30

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS, title="等速運動")
        self.create_ball(*INIT_POS)
        pyxel.run(self.update, self.draw)

    def create_ball(self, x, y):
        self.ball_pos = (x, y)

    def update(self):
        if self.ball_pos[1] > HEIGHT:
            self.create_ball(*INIT_POS)
        if self.ball_pos:
            self.ball_pos = self.ball_pos[0], self.ball_pos[1] + 3

    def draw(self):
        pyxel.cls(0)
        x, y = self.ball_pos
        pyxel.circ(x, y, 5, 8)

App()

import pyxel
import pymunk
import numpy as np

WIDTH, HEIGHT = 160, 120
FPS = 60
BALL_PROPERTY = 1, 30  # 質量, 慣性モーメント
BALL_POS = 10, HEIGHT - 25
BALL_RADIUS = 5
IMPULSE = (100, -400)
IMPACT_POS = -18 # -20：下～ボール～上：10

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS)
        self.space = pymunk.Space()  # 物理空間の作成
        self.space.gravity = (0, 900)  # 重力を設定
        self.space.damping = 0.5
        self.balls = list()
        self.create_ground()
        pyxel.run(self.update, self.draw)

    def create_ball(self):
        ball_body = pymunk.Body(*BALL_PROPERTY)  # ボールの動的ボディを作成
        ball_body.position = BALL_POS  # ボールの初期位置を設定
        ball_shape = pymunk.Circle(ball_body, 5)  # ボールを円形として定義
        ball_shape.elasticity = 0.9  # 反射係数を設定
        ball_shape.friction = 1.0 # 摩擦係数を設定（ボールと地面の摩擦）
        self.space.add(ball_body, ball_shape)
        self.balls.append(ball_body)

        # ボールにインパルスを加えて勢いよく発射
        ball_body.apply_impulse_at_local_point(IMPULSE, (0, -IMPACT_POS))

    def create_ground(self):
        # 地面を静的なボックスとして定義
        ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 静的ボディ
        ground_body.position = (WIDTH / 2, HEIGHT - 5)  # ボックスの中心位置を設定
        ground_shape = pymunk.Poly.create_box(ground_body, (WIDTH, 10))  # ボックスを作成
        ground_shape.elasticity = 0.8  # 反射係数を設定
        ground_shape.friction = 1.0  # 摩擦係数を設定（地面とボールの摩擦）
        self.space.add(ground_body, ground_shape)
        self.ground_shape = ground_shape

    def update(self):
        self.space.step(1 / FPS)  # 時間ステップの更新        

        if not pyxel.frame_count % (2 * FPS):
            self.create_ball()

    def draw(self):
        pyxel.cls(0)  # 画面をクリア
        for ball_body in self.balls:
            x, y = ball_body.position  # ボールの位置を取得
            angle = ball_body.angle
            rx, ry = x + BALL_RADIUS * np.cos(angle), y + BALL_RADIUS * np.sin(angle) 
            pyxel.circ(x, y, BALL_RADIUS, 7)  # ボールを描画
            pyxel.line(x, y, rx, ry, 8)
        x0, y0, x1, y1 = self.ground_shape.bb 
        pyxel.rect(x0, y0, x1 - x0, y1 - y0, 11)  # 地面を描画

App()

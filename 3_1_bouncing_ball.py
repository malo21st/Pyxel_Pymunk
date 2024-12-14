import pyxel
import pymunk

WIDTH, HEIGHT = 160, 120
INIT_POS = WIDTH // 2, 0
FPS = 60
BALL_PROPERTY = 1, float('inf')  # 質量, 慣性モーメント
STOP_THRESHOLD = 0.1  # ボールが止まったとみなす速度の閾値

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS)
        self.space = pymunk.Space()  # 物理空間の作成
        self.space.gravity = (0, 900)  # 重力を設定
        self.create_ball(*INIT_POS)
        self.create_ground()
        pyxel.run(self.update, self.draw)

    def create_ball(self, x, y):
        self.ball_body = pymunk.Body(*BALL_PROPERTY)  # ボールの動的ボディを作成
        self.ball_body.position = (x, y)  # ボールの初期位置を設定
        self.ball_shape = pymunk.Circle(self.ball_body, 5)  # ボールを円形として定義
        self.ball_shape.elasticity = 0.9  # 反射係数を設定
        self.space.add(self.ball_body, self.ball_shape)

    def create_ground(self):
        # 地面を静的なボックスとして定義
        self.ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 静的ボディ
        self.ground_body.position = (WIDTH / 2, HEIGHT - 5)  # ボックスの中心位置を設定
        self.ground_shape = pymunk.Poly.create_box(self.ground_body, (WIDTH, 10))  # ボックスを作成
        self.ground_shape.elasticity = 0.8  # 反射係数を設定
        self.space.add(self.ground_body, self.ground_shape)

    def reset_ball_position(self):
        self.ball_body.position = INIT_POS  # ボールの位置を初期化
        self.ball_body.velocity = (0, 0)  # ボールの速度をリセット

    def update(self):
        self.space.step(1 / FPS)  # 時間ステップの更新        
        # ボールが止まったかどうかを確認
        if abs(self.ball_body.velocity.y) < STOP_THRESHOLD:
            self.reset_ball_position()

    def draw(self):
        pyxel.cls(0)  # 画面をクリア
        ball_x, ball_y = self.ball_body.position  # ボールの位置を取得
        pyxel.circ(ball_x, ball_y, 5, 8)  # ボールを描画
        left, bottom, right, top = self.ground_shape.bb  # 地面の位置を取得
        pyxel.rect(left, bottom, right - left, top - bottom, 11)  # 地面を描画

App()
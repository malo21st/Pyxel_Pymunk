import pyxel
import pymunk
from pymunk import Vec2d

# 初期設定
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
TRIANGLE_RADIUS = 6
BALL_MASS = 10
PADDLE_WIDTH = 24
PADDLE_HEIGHT = 4
BLOCK_WIDTH = 16
BLOCK_HEIGHT = 8
FPS = 60
PI = 3.1415926535

class BreakoutGame:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS, title="Triangle Breakout")
        # pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS, display_scale=2, title="Triangle Breakout")
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.init_game_objects()
        pyxel.run(self.update, self.draw)

    def init_game_objects(self):
        # 正三角形のボールを作成
        self.triangle_body = pymunk.Body(1, pymunk.moment_for_poly(BALL_MASS, self.create_triangle_points()))
        self.triangle_body.position = (0, SCREEN_HEIGHT + 10)
        self.triangle_shape = pymunk.Poly(self.triangle_body, self.create_triangle_points())
        self.triangle_shape.elasticity = 1.0
        self.space.add(self.triangle_body, self.triangle_shape)

        # パドル
        self.paddle_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.paddle_body.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10)
        self.paddle_shape = pymunk.Poly.create_box(self.paddle_body, (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.paddle_shape.elasticity = 1.0
        self.space.add(self.paddle_body, self.paddle_shape)

        # 壁
        static_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        walls = [
            pymunk.Segment(static_body, (0, 0), (0, SCREEN_HEIGHT), 1),  # 左の壁
            pymunk.Segment(static_body, (0, 0), (SCREEN_WIDTH, 0), 1),  # 上の壁
            pymunk.Segment(static_body, (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 1),  # 右の壁
        ]
        for wall in walls:
            wall.elasticity = 1.0
        self.space.add(static_body, *walls)

        # ブロック
        self.blocks = []
        for i in range(8):  # 横に8個
            for j in range(5):  # 縦に5段
                x = 10 + i * (BLOCK_WIDTH + 2)
                y = 20 + j * (BLOCK_HEIGHT + 2)

                block_body = pymunk.Body(body_type=pymunk.Body.STATIC)
                block_body.position = (x, y)
                block_shape = pymunk.Poly.create_box(block_body, (BLOCK_WIDTH, BLOCK_HEIGHT))
                block_shape.elasticity = 1.0
                block_shape.color = pyxel.COLOR_RED + j  # 色を設定（Pyxel描画用）
                self.space.add(block_body, block_shape)
                self.blocks.append((block_body, block_shape))

    def update(self):
        # パドル操作
        x = pyxel.mouse_x
        self.paddle_body.position = (
            max(PADDLE_WIDTH // 2, min(x, SCREEN_WIDTH - PADDLE_WIDTH // 2)),
            SCREEN_HEIGHT - 10,
        )

        # ゲーム更新
        self.space.step(1 / FPS)

        # ボールが画面外に出た場合のリセット
        if self.triangle_body.position.y > SCREEN_HEIGHT:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                self.triangle_body.position = (self.paddle_body.position[0], SCREEN_HEIGHT - 20)
                self.triangle_body.velocity = Vec2d(50, -50)

        # 衝突後にブロックを削除
        for block_body, block_shape in self.blocks:
            if self.triangle_shape.shapes_collide(block_shape).points:
                self.blocks.remove((block_body, block_shape))
                self.space.remove(block_body, block_shape)

    def create_triangle_points(self):
        """正三角形の頂点を計算する"""
        angle_step = 2 * PI / 3  # 120度ごと
        return [
            Vec2d(TRIANGLE_RADIUS, 0).rotated(i * angle_step)
            for i in range(3)
        ]
    
    def draw(self):
        pyxel.cls(0)
        # ボール
        ## 三角形の現在の回転角度を取得
        angle = self.triangle_body.angle
        points = [
            (self.triangle_body.position + p.rotated(angle))
            for p in self.create_triangle_points()
        ]
        ## 三角形を描画
        pyxel.tri(
            *points[0], *points[1], *points[2],
            pyxel.COLOR_WHITE
        )
        # パドル
        x, y, _, _ = self.paddle_shape.bb
        pyxel.rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT, pyxel.COLOR_YELLOW)
        # ブロック
        for _, shape in self.blocks:
            x, y, _, _ = shape.bb
            pyxel.rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, shape.color)

# ゲーム開始
BreakoutGame()
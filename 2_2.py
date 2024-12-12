import pymunk

INIT_POS = 80, 0
FPS = 30
BALL_PROPERTY = 1, float('inf') #0 質量, 慣性モーメント

# 物理空間の生成
space = pymunk.Space() #1
space.gravity = (0, 900) #2

# ボールの生成
ball = pymunk.Body(*BALL_PROPERTY) #3
ball.position = INIT_POS #4
space.add(ball) #5

# 物理シミュレーションの実行
for _ in range(10):
    space.step(1 / FPS) #6
    x, y = ball.position #7
    print(f"Ball Position: {x}, {y}")
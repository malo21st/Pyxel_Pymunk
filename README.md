# Pyxel Advent Calendar 2024  
## 15日目　Pyxel × Pymunkで物理シミュレーションを始めよう！  
- Qiita記事：https://qiita.com/malo21st/items/32b7865e7c78d4ac2741  
---

### 関連記事：Web版PyxelでPymunkを使用したい時は、こちらが参考になります。
- 「Pyxel × Pymunkで物理シミュレーションを始めよう！」を Webで動かしたい🌎
  - https://qiita.com/Kazuhito/items/cf7f2e0f42f47e611f3e  
---

**0. Pymunkのご紹介**
  - https://www.viblo.se/projects/pymunk/  

**1. PyxelとPymunkの準備**
  - Pyxel  
    - https://github.com/kitao/pyxel/tree/main  
  - Pymunk  
    - https://www.pymunk.org/en/latest/  

**2. アプリケーションの基本構成**  
  - 2.1 Pyxelの基本構成  
    - 2_1_pyxel.py  
  - 2.2 Pymunkの基本構成  
    - 2_2_pymunk.py  
  - 2.3 PyxelとPymunkの統合  
    - 2_3_pyxel_pymunk.py  

**3. 基礎から応用へ**  
  - 3.1 跳ねるボール  
    - 3_1_bouncing_ball.py  
  - 3.2 ボールを動かす  
    - 3_2_impulse_ball.py  
    - 3_2_shot_bullet.py  3_2_shot_bullet.pyxres  
      こちらのコードをPyxelに移植しました。  
      https://github.com/viblo/pymunk/blob/master/pymunk/examples/box2d_vertical_stack.py
      <img src="/gif/3_2_shot_bullet.gif" width="300">  
  - 3.3 ゲームへの応用  
    - 3_3_breakout_nrm.py  
    - 3_3_breakout_tri.py  
      <img src="/gif/3_3_breakout_tri.gif" width="300">

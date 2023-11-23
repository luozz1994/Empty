import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置游戏窗口大小
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Mario")

# 加载游戏资源
bg_image = pygame.image.load("background.png")
mario_image = pygame.image.load("mario.png")

# 设置玩家初始位置
mario_x = 400
mario_y = 500

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制游戏场景
    screen.blit(bg_image, (0, 0))
    screen.blit(mario_image, (mario_x, mario_y))

    # 更新屏幕显示
    pygame.display.flip()

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
# 初始化游戏并创建一个屏幕对象 
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环 
    while True:
    # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        # 让最近绘制的屏幕可见 
        gf.update_screen(ai_settings,screen,ship)
run_game()

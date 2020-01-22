import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from score_board import Scoreboard
def run_game():
# 初始化游戏并创建一个屏幕对象 
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群  
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 初始化游戏统计信息
    stats = GameStats(ai_settings)
    pygame.display.set_caption("Alien Invasion")
    # 创建play按钮
    play_button = Button(ai_settings, screen, 'PLAY')
    # 记分牌
    sb = Scoreboard(ai_settings,screen,stats)
    # 开始游戏的主循环 
    while True:
    # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button,sb)
        if(stats.game_active):
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets,sb)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets, sb)
        # 让最近绘制的屏幕可见 
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)

run_game()

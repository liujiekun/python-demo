import pygame
from pygame.sprite import Sprite
import math
class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen): 
      """初始化外星人并设置其起始位置""" 
      super(Alien, self).__init__() 
      self.screen = screen 
      self.ai_settings = ai_settings
      # 加载外星人图像，并设置其rect属性
      self.image = pygame.image.load('alien_invasion/images/alien.png') 
      self.rect = self.image.get_rect()
      # 每个外星人最初都在屏幕左上角附近 
      self.rect.x = self.rect.width 
      self.rect.y = self.rect.height
      # 存储外星人的准确位置 
      self.x = float(self.rect.x)
      self.y = float(self.rect.y)
    def blitme(self): 
      """在指定位置绘制外星人"""
      self.screen.blit(self.image, self.rect)
    def check_fleet_edges(self): 
      """如果外星人位于屏幕边缘，就返回True""" 
      screen_rect = self.screen.get_rect()
      if (self.rect.right >= screen_rect.right or self.rect.left <= 0):
        return True
    def update(self):
      """向右向下移动外星人"""
      self.x+=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
      self.rect.x=self.x
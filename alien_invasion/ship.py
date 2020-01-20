import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if (self.move_left and self.rect.left>0):
            self.center -= self.ai_settings.ship_speed_factor
        elif (self.move_right and self.rect.right<self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        elif(self.move_up and self.rect.bottom>self.rect.height):
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        elif(self.move_down and self.rect.bottom<self.screen_rect.bottom):
            self.rect.bottom += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def ship_center(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
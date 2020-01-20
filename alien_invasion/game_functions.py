import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y)

def check_key_down(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #向右移动飞船 
        ship.move_right=True
    elif event.key == pygame.K_LEFT:
        #向左移动飞船 
        ship.move_left=True
    elif event.key == pygame.K_UP:
        #向左移动飞船 
        ship.move_up=True
    elif event.key == pygame.K_DOWN:
        #向左移动飞船 
        ship.move_down=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_key_up(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #向右移动飞船 
        ship.move_right=False
    elif event.key == pygame.K_LEFT:
        #向左移动飞船 
        ship.move_left=False
    elif event.key == pygame.K_UP:
        #向左移动飞船 
        ship.move_up=False
    elif event.key == pygame.K_DOWN:
        #向左移动飞船 
        ship.move_down=False

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 绘制敌人
    aliens.draw(screen)
    
    # 如果游戏处于非活动状态，就绘制Play按钮 
    if not stats.game_active:
        button.draw_button()

    # 让最近绘制的屏幕可见 
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        # 如果子弹已经到达屏幕顶端，就从Group中删除
        if(bullet.rect.bottom<=0):
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens)==0:
        bullets.empty()
        # 游戏加速
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    if(len(bullets)<ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_numbers_aliens_x(ai_settings,screen):
    alien = Alien(ai_settings,screen)
    alien_with = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_with
    numbers_aliens_x = int(available_space_x/(2*alien_with))
    return numbers_aliens_x

def get_number_aliens_y(ai_settings,screen,ship):
    alien = Alien(ai_settings,screen)
    alien_height = alien.rect.height
    available_space_y = ai_settings.screen_height - 2*alien_height-ship.rect.height
    numbers_aliens_y = int(available_space_y/(2*alien_height))
    return numbers_aliens_y

def create_aliens(num_y,num_x,ai_settings,screen,aliens):
    for alien_number_y in range(num_y):
        for alien_number_x in range(num_x):
            #创建一个外星人，并将其加入当前行
            alien=Alien(ai_settings,screen)
            alien_with = alien.rect.width
            alien_heigth=alien.rect.height
            alien.x=alien_with+2*alien_with*alien_number_x
            alien.y=alien_heigth+2*alien_heigth*alien_number_y
            alien.rect.x=alien.x
            alien.rect.y=alien.y
            aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    numbers_aliens_x = get_numbers_aliens_x(ai_settings,screen)
    numbers_aliens_y = get_number_aliens_y(ai_settings,screen,ship)
    create_aliens(numbers_aliens_y,numbers_aliens_x,ai_settings,screen,aliens)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if(alien.check_fleet_edges()):
            change_fleet_direction(ai_settings,aliens)
            break
            
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, ship, aliens, bullets):
    if(stats.ships_left>0):
        stats.ships_left -= 1
        
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 重新创建新外星人，并将飞船放置到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.ship_center()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if(alien.rect.bottom >=screen_rect.bottom):
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        # print('Ship hits!!!')
        ship_hit(ai_settings,screen,stats,ship,aliens,bullets)
    check_aliens_bottom(ai_settings, screen,stats, ship, aliens, bullets)
        
def check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    if(play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active):
        
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 游戏重置
        stats.reset_stats()
        stats.game_active = True


        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        
        # 重新创建新外星人，并将飞船放置到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.ship_center()


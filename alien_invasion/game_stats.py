class GameStats():
  def __init__(self,ai_settings):
    self.ai_settings = ai_settings
    self.reset_stats()
    # 标识游戏处于启动状态
    self.game_active = True
  
  def reset_stats(self):
    self.ships_left = self.ai_settings.ships_left
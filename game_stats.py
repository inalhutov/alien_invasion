class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        # Рекорд не должен сбрасываться
        self.high_score = 0
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

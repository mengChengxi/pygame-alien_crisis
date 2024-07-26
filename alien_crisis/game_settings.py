class Game_settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bullet_speed_factor = 20
        self.bullet_limit = 10
        self.alien_speed = 0.001

        self.bg_color = (255, 255, 250)
        self.ship_speed_factor = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 251, 181, 27
        self.fire_frequency = 10

        self.alien_creat_frequency = 50
        self.alien_speed_factor = 0.5

        self.abullet_width = 20
        self.abullet_height = 20

        self.abullet_color = 255, 0, 0
        self.alien_fire = 100

        self.blood = 5
        self.blood_add = 5

from Class.Entity.Character.Character import Character, pygame
from Functions.Controls.Keyboard.keyboard_pressed import keyboard_pressed
from Functions.Controls.Mouse.mouse_pressed import mouse_pressed
from Class.Entity.Enemy.Enemy import Enemy


class Knight(Character):
    def __init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates, _damage):
        Character.__init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates)
        self._damage = _damage
        self._delay = 0
        self._gender = "knight/"
        self._facing_right = False
        self._facing_left = False
        self._hitbox_sword = pygame.Rect(self._g_point[0], self._g_point[1], 100, 20)

    def sword(self, win):
        if keyboard_pressed() == "right":
            self._facing_right = True
            self._facing_left = False
        elif keyboard_pressed() == "left":
            self._facing_right = False
            self._facing_left = True
        else:
            self._facing_right = False
            self._facing_left = False

        if self._facing_left:
            pygame.draw.rect(win, (255, 180, 12), (self._g_point[0]-20, self._g_point[1]+25, -50, 15), 0)
            self._hitbox_sword = pygame.Rect(self._g_point[0], self._g_point[1], -50, 15)
        elif self._facing_right or not self._facing_left and not self._facing_right:
            pygame.draw.rect(win, (255, 180, 12), (self._g_point[0]+20, self._g_point[1]+25, 50, 15), 0)
            self._hitbox_sword = pygame.Rect(self._g_point[0], self._g_point[1], 50, 15)

        if not self._hitbox_sword.collidelist(Enemy.enemy_hitlist) == -1 and self._delay == 0 and mouse_pressed() == "right":
            num = self._hitbox.collidelist(Enemy.enemy_hitlist)
            Enemy.enemy_list[num].health -= self._damage
            self._delay = 50

        if not self._delay == 0:
            self._delay -= 1

    def update(self, win):
        self.movement()
        self.collisions()
        self.draw(win)
        self.sword(win)

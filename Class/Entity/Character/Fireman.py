from Class.Entity.Character.Character import Character, pygame
from Class.Entity.Projectile.RoundedProj import RoundedProj
from Functions.Controls.Mouse.mouse_pressed import mouse_pressed


class Fireman(Character):
    def __init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates, _damage):
        Character.__init__(self, _w, _h, _m, _g, _health, _speed, _shooting_rates)
        self._gender = "fireman/"
        self._damage = _damage
        self._delay = 0

    def shooting(self):
        if self._shoot_loop >= 0:
            self._shoot_loop += 1
        if self._shoot_loop > self._shooting_rates:
            self._shoot_loop = self._shooting_rates

        if mouse_pressed() == "right" and len(RoundedProj.proj_list) <= 25 and self._shoot_loop == self._shooting_rates:
            RoundedProj(_x=self._g_point[0], _y=self._g_point[1], _v=3, _radius=10,
                        _orientationX=(pygame.mouse.get_pos()[0] - self._g_point[0]) / 30,
                        _orientationY=-(pygame.mouse.get_pos()[1] - self._g_point[1]) / 30, _damage=self._damage)
            self._shoot_loop = 0

    def update(self, win):
        self.hud(win)
        self.movement()
        self.collisions()
        self.shooting()
        self.draw(win)

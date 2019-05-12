from math import floor
from Class.Entity.Projectile.Projectile import Projectile
from Class.Terrain.Block import Block
from Class.Entity.SpecialEntity.Teleporter import Teleporter
from Class.Entity.Enemy.Enemy import Enemy
from Functions.map_choice import map_choice
from Functions.Controls.Mouse.mouse_position import mouse_position
from Functions.change_heroes import *

if raspberry:
    from Functions.Server.client import *

VALUE = 0
LAST = 1

def update_game(win, count, delay):
    MAP = Character.charact_list[0].map
    win.fill((0, 0, 0))
    global VALUE
    global LAST

    map_choice(MAP, VALUE)

    if LAST == MAP:
        VALUE += 1
    else:
        VALUE = 0
    LAST = MAP

    pygame.draw.circle(win, (28, 28, 28), (floor(Character.charact_list[0].g_point[0]) + 20, floor(Character.charact_list[0].g_point[1])), MOUSER, 0)

    for obj in Block.block_list:
        obj.update(win)
    for obj in Projectile.proj_list:
        obj.update(win)
    for obj in Teleporter.teleporter_list:
        obj.update(win)
    for obj in Enemy.enemy_list:
        obj.update(win)
    for obj in Character.charact_list:
        obj.update(win)

    mouse_position()
    if delay == 0:
        switch_heroes()
        delay += 1000

    if not delay == 0:
        delay -= 1

    #   update each second
    if raspberry:
        if count == 120:
            msgx = "actu"
            Sock.send(msgx.encode())

    pygame.display.update()

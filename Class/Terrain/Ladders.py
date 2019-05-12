from Class.Terrain.Block import Block
from Assets.load_textures import *


class Ladders(Block):
    def __init__(self, _x, _y, _w, _h, _texture):
        Block.__init__(self, _x, _y, _w, _h, _texture, _no_texture=True, _is_trav_right=True, _is_trav_left=True, _is_trav_top=True, _is_trav_bottom=True)
        self._block_type = "Ladders"
        self._color = (255, 255, 0)

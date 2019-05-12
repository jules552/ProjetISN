from Class.Terrain.Block import Block


class BlockEnd(Block):
    def __init__(self, _x, _y, _w, _h, _texture):
        Block.__init__(self, _x, _y, _w, _h, _texture, _is_trav_right=True, _is_trav_left=True, _is_trav_top=True, _is_trav_bottom=True, _no_texture=True)
        self._block_type = "BlockEnd"
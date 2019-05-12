from Assets.load_textures import *
from Class.Terrain.BlockEnd import BlockEnd
from Class.Entity.Enemy.Enemy import Enemy
from Class.Terrain.Block import Block
from Class.Terrain.Ladders import Ladders


def map_choice(MAP, VALUE):

    if MAP == 1 and VALUE == 0:
        Block(2000, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=mountain, _resize=(True, 200), _parallaxe=(True, 4))
        Block(800, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=mountain, _resize=(True, 200), _parallaxe=(True, 3))
        Block(1200, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=mountain, _resize=(True, 200), _parallaxe=(True, 2))

        Block(1200, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=tree, _resize=(True, 200), _parallaxe=(True, 1.5))

        Block(1350, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=tree2, _resize=(True, 200), _parallaxe=(True, 1.8))

        Block(2000, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=True, _is_trav_bottom=True, _texture=tree3, _resize=(True, 200), _parallaxe=(True, 1.2))

        Block(500, 0, 0, 0, _is_no_collision=True, _texture=fond)

        Block(500, 430, 2260, 50, _texture=nothing)
        Block(2890, 430, 2280, 50, _texture=nothing)
        Block(5275, 430, 2280, 50, _texture=nothing)

        Block(855, 360, 270, 200, _texture=nothing)

        Block(1900, 360, 560, 200, _texture=nothing)
        Block(3880, 360, 460, 150, _texture=nothing)
        Block(4310, 290, 560, 150, _texture=nothing)

        Block(2015, 200, 80, 50, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2095, 300, 65, 50, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2160, 250, 80, 50, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2240, 295, 40, 50, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(1705, 105, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2600, 365, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2680, 325, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
        Block(2540, 410, 80, 30, _is_trav_right=True, _is_trav_left=True,
              _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)

        Enemy(1200, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")
        Enemy(3000, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")
        Enemy(5600, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")

        Enemy(1900, 230, 100, 100, tikiWalkLeftRush, tikiWalkRightRush, (True, 200), _health=100, _gender="/Tiki/Rush")
        Enemy(2900, 300, 100, 100, tikiWalkLeftRush, tikiWalkRightRush, (True, 200), _health=100, _gender="/Tiki/Rush")

        BlockEnd(6300, 200, 100, 100, _texture=tree2)

    if MAP == 2 and VALUE == 0:

        for obj in Block.block_list:
            obj.delete()
        for obj in Enemy.enemy_list:
            obj.delete()

        Block(500, -2500, 0, 0, _is_no_collision=True, _texture=fond2)

        Block(450, -4500, 50, 5000, _texture=nothing)
        Block(980, -4500, 50, 5000, _texture=nothing)

        Block(480, 480, 500, 50, _texture=nothing)

        Block(620, 60, 500, 50, _texture=nothing)
        Block(920, 5, 500, 100, _texture=nothing)

        Block(700, -765, 500, 50, _texture=nothing)
        Block(330, -300, 500, 50, _texture=nothing)

        Block(620, -1400, 500, 50, _texture=nothing)
        Block(920, -1455, 500, 100, _texture=nothing)

        Block(450, -970, 600, 40, _texture=nothing)
        Block(450, -2120, 600, 40, _texture=nothing)

        Ladders(500, -4500, 100, 5000, _texture=nothing)
        Ladders(880, -4500, 100, 5000, _texture=nothing)



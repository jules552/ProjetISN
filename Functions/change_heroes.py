from Functions.Controls.Keyboard.keyboard_pressed import *
from Objects.Entity.Character.Character import *
from Class.Entity.Character.Character import Character
from intValues import *
from Functions.NFC.getUID import *
if raspberry:
    from Functions.Server.client import *

def switch_heroes():
    if raspberry:
        uid = getUID()

    if keyboard_pressed() == "F1" or (nfc and uid == ['0xb0', '0xfa', '0x5b', '0x56', '0x90', '0x0']):
        Character.charact_list[0].delete()
        Fireman(_w=60, _h=120, _m=20, _g=1.4, _health=100, _speed=8, _shooting_rates=100, _damage=60)

        if raspberry:
            msgx = "fireman"
            Sock.send(msgx.encode())
            time.sleep(0.1)

    elif keyboard_pressed() == "F2" or (nfc and uid == ['0x50', '0xe2', '0x5a', '0x56', '0x90', '0x0']):
        Character.charact_list[0].delete()
        Knight(_w=60, _h=120, _m=20, _g=1.4, _health=100, _speed=8, _shooting_rates=100, _damage=60)

        if raspberry:
            msgx = "knight"
            Sock.send(msgx.encode())
            time.sleep(0.1)



import locSetting as locSetting
from eudplib import *

@EUDFunc
def f_moveLoop():
    for cPlayer in [P7, P8]:
        locSetting.f_setMissileLocations(cPlayer)
        for unit in ['Fast Missile', 'Missile', 'Slow Missile', 'Refractor', 'Trap']:
            for x in EUDLoopRange(11):
                DoActions([
                    Order(unit, cPlayer, locSetting.vFromArray[x], Move, locSetting.vToArray[x]),
                    KillUnitAt(All, unit, locSetting.vToArray[x], cPlayer)
                ])

            for y in EUDLoopRange(5):
                DoActions([
                    Order(unit, cPlayer, locSetting.hFromArray[y], Move, locSetting.hToArray[y]),
                    KillUnitAt(All, unit, locSetting.hToArray[y], cPlayer)
                ])

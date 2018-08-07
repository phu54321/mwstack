from eudplib import *
import locSetting
import patternbase
from patterns import stage
import location

@EUDFunc
def f_shootLoop():
    unit = 'Slow Missile [B]'

    for p in EUDLoopRange(6):
        if EUDIfNot()(f_playerexist(p)):
            EUDContinue()
        EUDEndIf()

        force = locSetting.f_forceFromPlayer(p)
        locSetting.f_setMissileLocations(force)

        allyFieldX, allyFieldY = location.f_getTopLeft('allyField')
        for x in EUDLoopRange(22):
            for y in EUDLoopRange(10):
                location.f_pxMoveLocation('pxmove', allyFieldX + 32 * x, allyFieldY + 32 * y, 32, 32)
                DoActions(MoveLocation('pxmove', 'Map Revealer', P12, 'pxmove'))
                if EUDIf()(Bring(p, AtLeast, 1, unit, "pxmove")):
                    patternbase.f_addPattern(p, stage.f_impl)
                    DoActions(RemoveUnitAt(1, unit, 'pxmove', p))
                EUDEndIf()
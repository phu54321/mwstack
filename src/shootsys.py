from eudplib import *
import locSetting
import patternbase
import location

from patterns import (
    stage,
    center,
    sidecenter,
    sidestage,
    single,
    moveto,
    trap,
    soy,
    blocker
)

unitPatternMap = {
    'Stage Missile [N]': stage.f_impl,
    'Center Missile [N]': center.f_impl,
    'Side Center Missile [N]': sidecenter.f_impl,
    'Side Stage Missile [N]': sidestage.f_impl,
    'Move To [N]': moveto.f_impl,

    'Missile [N]': single.f_missile_impl,
    'Fast Missile [N]': single.f_fast_impl,
    'Refractor [N]': single.f_refractor_impl,
    'Ore Slot [N]': single.f_ore_slot_impl,
    'Trap [N]': trap.f_impl,
    'Phosphorus Bomb [N]': soy.f_soy_impl,
    'Blocker [N]': blocker.f_impl,
}

@EUDFunc
def f_shootLoop():
    for p in EUDLoopRange(6):
        if EUDIfNot()(f_playerexist(p)):
            EUDContinue()
        EUDEndIf()

        force = locSetting.f_forceFromPlayer(p)
        locSetting.f_setMissileLocations(force)

        allyFieldX, allyFieldY = location.f_getTopLeft('allyField')
        for x in EUDLoopRange(22):
            for y in EUDLoopRange(10):
                location.f_pxMoveLocationDot('pxmove', allyFieldX + 32 * x + 16, allyFieldY + 32 * y + 16)
                DoActions(MoveLocation('pxmove', 'Map Revealer', P12, 'pxmove'))

                for unit, handlerModule in unitPatternMap.items():
                    if EUDIf()(Bring(p, AtLeast, 1, unit, "pxmove")):
                        if unit == 'Move To [N]':
                            patternbase.f_addPattern(p, x, y, handlerModule)
                        else:
                            patternbase.f_addPattern(p + 3, x, y, handlerModule)
                        DoActions(RemoveUnitAt(1, unit, 'pxmove', p))
                    EUDEndIf()
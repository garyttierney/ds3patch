"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.darksouls3.events import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(13600000, obj=3601950, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13600001, obj=3601951, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13600002, obj=3601952, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(13600003, obj=3601953, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunEvent(13600999)
    RunEvent(13605100)
    RunEvent(13605400, slot=0, args=(3602450,))
    RunEvent(13605400, slot=1, args=(3602451,))
    RunEvent(13605400, slot=2, args=(3602452,))
    RunEvent(13605400, slot=3, args=(3602453,))
    RunEvent(13605400, slot=4, args=(3602454,))
    RunEvent(13605400, slot=5, args=(3602455,))
    RunEvent(13605400, slot=6, args=(3602456,))
    RunEvent(13600500)
    RunEvent(13600510)
    RunCommonEvent(20000610, args=(0, 0, 0))
    RunCommonEvent(20000612, args=(0, 0))
    RunCommonEvent(20000610, args=(0, 0, 0))
    RunCommonEvent(20000611, args=(0, 0, 0, 0))
    RunEvent(13605810)
    RunEvent(13605811)
    RunEvent(13605820)
    RunCommonEvent(20000821, args=(13600800, 13600002, 3600952, 3601952))
    RunEvent(13605860)
    RunEvent(13605861)
    RunEvent(13605850)
    RunEvent(13605851)
    RunEvent(13605870)
    RunCommonEvent(20000821, args=(13600850, 13600003, 3600953, 3601953))
    RunEvent(13605200, slot=0, args=(3600200, 3602200))
    RunEvent(13605200, slot=1, args=(3600201, 3602201))
    RunEvent(13605200, slot=2, args=(3600202, 3602202))
    RunEvent(13605200, slot=3, args=(3600203, 3602203))
    RunCommonEvent(20005019, args=(3600300, 3602300, 3602301, 3602302, 0, 0, 0, 0))
    RunCommonEvent(20005019, args=(3600301, 3602303, 3602304, 3602305, 0, 0, 0, 0))
    RunEvent(13605700)
    RunEvent(13605701, event_layers=[0])
    RunEvent(13605710, event_layers=[1])
    RunEvent(13605711, event_layers=[1])
    RunEvent(13605720, event_layers=[1])
    RunEvent(13605721, event_layers=[1])
    RunEvent(13605722, event_layers=[1])
    RunEvent(13605730, event_layers=[2, 4])


def Event13600999():
    """ 13600999: Event 13600999 """
    RegisterLadder(start_climbing_flag=13600550, stop_climbing_flag=13600551, obj=3601450)
    RegisterLadder(start_climbing_flag=13600552, stop_climbing_flag=13600553, obj=3601451)


def Event13605200(_, arg_0_3: int, arg_4_7: int):
    """ 13605200: Event 13605200 """
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(arg_0_3)
    Wait(1.0)
    EnableAI(arg_0_3)


def Event13605400(_, arg_0_3: int):
    """ 13605400: Event 13605400 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4050)
    IfCharacterOutsideRegion(0, PLAYER, region=arg_0_3)
    CancelSpecialEffect(PLAYER, 4050)
    Restart()


def Event13600500():
    """ 13600500: Event 13600500 """
    EndIfThisEventSlotOn()
    EndOfAnimation(3601500, 1)
    IfObjectActivated(0, obj_act_id=3603510)
    Wait(4.0)
    ForceAnimation(3601500, 3, wait_for_completion=True)
    EnableFlag(13600500)


@RestartOnRest
def Event13600510():
    """ 13600510: Event 13600510 """
    DisableObject(3601512)
    EndIfThisEventSlotOn()
    EnableObject(3601512)
    IfCharacterInsideRegion(0, PLAYER, region=3602510)
    ForceAnimation(3601512, 1, wait_for_completion=True)
    EnableFlag(13600510)


def Event13605700():
    """ 13605700: Event 13605700 """
    RunCommonEvent(4294967295)


def Event13605701():
    """ 13605701: Event 13605701 """
    RunCommonEvent(4294967295)


def Event13605710():
    """ 13605710: Event 13605710 """
    RunCommonEvent(4294967295)


def Event13605711():
    """ 13605711: Event 13605711 """
    RunCommonEvent(4294967295)


def Event13605720():
    """ 13605720: Event 13605720 """
    RunCommonEvent(4294967295)


def Event13605721():
    """ 13605721: Event 13605721 """
    RunCommonEvent(4294967295)


def Event13605722():
    """ 13605722: Event 13605722 """
    RunCommonEvent(4294967295)


def Event13605730():
    """ 13605730: Event 13605730 """
    DisableCharacter(3605701)


def Event13605810():
    """ 13605810: Event 13605810 """
    GotoIfFlagOff(Label.L0, 13600800)
    Kill(3600800, award_souls=False)
    DisableCharacter(3600800)
    DisableAI(3600800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(3600800)
    IfFlagOn(1, 13605805)
    IfCharacterInsideRegion(1, PLAYER, region=3602800)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13600801)
    EnableAI(3600800)
    EnableBossHealthBar(3600800, name=2090)


def Event13605811():
    """ 13605811: Event 13605811 """
    EndIfFlagOn(13600800)
    IfCharacterDead(0, 3600800)
    KillBoss(3600800)
    EnableFlag(13600800)


@RestartOnRest
def Event13605820():
    """ 13605820: Event 13605820 """
    RunCommonEvent(20000800, args=(13600800, 3601800, 3602800, 13605805, 3601800, 3600800, 13600801, 3602800))
    RunCommonEvent(20000801, args=(13600800, 3601800, 3602800, 13605805, 3601800, 13605806))
    RunCommonEvent(20000820, args=(13600800, 3601800, 3, 13600801))
    RunCommonEvent(20000820, args=(13600800, 3601801, 3, 0))
    RunCommonEvent(20001830, args=(13600800, 13605805, 13605806, 3602800, 3604800))


@RestartOnRest
def Event13605850():
    """ 13605850: Event 13605850 """
    EndIfClient()
    EndIfFlagOn(13600850)
    GotoIfFlagOn(Label.L0, 13600851)
    IfCharacterInsideRegion(0, PLAYER, region=3602851)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfHost(1)
    IfFlagOff(1, 13600850)
    IfCharacterInsideRegion(1, PLAYER, region=3602850)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L1, 13605855)
    IfFlagOff(2, 13600850)
    IfCharacterInsideRegion(2, PLAYER, region=3602850)
    IfConditionTrue(0, input_condition=2)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfClient(Label.L2)
    NotifyBossBattleStart()

    # --- 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(0)
    EnableFlag(13605855)
    Restart()


@RestartOnRest
def Event13605851():
    """ 13605851: Event 13605851 """
    IfFlagOff(1, 13600850)
    IfFlagOn(1, 13605855)
    IfCharacterInsideRegion(0, PLAYER, region=3602850)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13605856)
    Restart()


@RestartOnRest
def Event13605860():
    """ 13605860: Event 13605860 """
    GotoIfFlagOff(Label.L0, 13600850)
    Kill(3600850, award_souls=False)
    DisableCharacter(3600850)
    DisableAI(3600850)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(3600850)
    GotoIfFlagOn(Label.L1, 13600851)
    IfFlagOn(1, 13605855)
    IfCharacterInsideRegion(1, PLAYER, region=3602851)
    IfConditionTrue(0, input_condition=1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 13605855)
    IfCharacterInsideRegion(1, PLAYER, region=3602850)
    IfConditionTrue(0, input_condition=1)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(13600851)
    EnableFlag(13605877)
    EnableAI(3600850)
    EnableBossHealthBar(3600850, name=5020)


def Event13605861():
    """ 13605861: Event 13605861 """
    EndIfFlagOn(13600850)
    IfCharacterDead(0, 3600850)
    KillBoss(3600850)
    EnableFlag(13600850)


@RestartOnRest
def Event13605870():
    """ 13605870: Event 13605870 """
    RunCommonEvent(20001835, args=(13600850, 13605855, 13605856, 13605877, 3604850))

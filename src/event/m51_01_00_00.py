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
    RunCommonEvent(20005500, args=(15110800, 15110000, 5110950, 5111950))
    RegisterBonfire(15110001, obj=5111951, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunEvent(15115800)
    RunEvent(15115810)
    RunEvent(15115811)
    RunEvent(15115812)
    RunEvent(15115847)
    RunEvent(15115849)
    RunCommonEvent(20005840, args=(5111800,))
    RunCommonEvent(20005841, args=(5111800,))
    RunEvent(15115850)
    RunEvent(15115860)
    RunEvent(15115889)
    RunCommonEvent(20005840, args=(5111850,))
    RunCommonEvent(20005841, args=(5111850,))
    RunEvent(15115890)
    RunEvent(15115201)
    RunCommonEvent(20005110, args=(5110300, 5112800))
    RunEvent(15115300)
    RunCommonEvent(20005351, args=(5110240, 62600240, 55110981, 1073741824))
    RunEvent(15115891)
    RunCommonEvent(20006002, args=(5110850, 1838, 1835, 1839))
    RunCommonEvent(20006031, args=(75110180, 5112801))


def Preconstructor():
    """ 50: Event 50 """
    DisableSoundEvent(5114801)
    DisableSoundEvent(5114802)
    DisableSoundEvent(5114803)
    RunEvent(15115200)
    RunEvent(15115100)


@RestartOnRest
def Event15115100():
    """ 15115100: Event 15115100 """
    EndIfFlagOn(15110800)
    SetCurrentMapCeremony(ceremony_id=0)


@RestartOnRest
def Event15115200():
    """ 15115200: Event 15115200 """
    DisableGravity(5110200)
    DisableCharacterCollision(5110200)


@RestartOnRest
def Event15115201():
    """ 15115201: Event 15115201 """
    IfCharacterBackreadEnabled(0, 5110200)
    WaitFrames(1)
    ForceAnimation(5110200, 30000, loop=True, skip_transition=True)


@RestartOnRest
def Event15115300():
    """ 15115300: Event 15115300 """
    IfFlagOff(1, 15110801)
    IfFlagOff(1, 15110300)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableCharacter(5110300)
    DisableBackread(5110300)
    DisableAnimations(5110300)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(5110300, distance=100.0)
    DisableFlag(75110200)
    IfFlagOn(-1, 15110800)
    IfCharacterInsideRegion(-1, 5110300, region=5112300)
    IfCharacterDead(-1, 5110300)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(1, 5110300)
    SkipLinesIfConditionTrue(1, 1)
    Kill(5110300, award_souls=False)
    EnableFlag(15110300)


@RestartOnRest
def Event15115800():
    """ 15115800: Event 15115800 """
    EndIfFlagOn(15110800)
    IfHealthEqual(1, 5110800, 0.0)
    IfConditionTrue(0, input_condition=1)
    Wait(2.6700000762939453)
    PlaySoundEffect(anchor_entity=5110800, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5110800, banner=BannerType.HeirOfFireDestroyed)
    DeleteVFX(5113820, erase_root_only=True)
    DeleteVFX(5113821, erase_root_only=True)
    DeleteVFX(5113822, erase_root_only=True)
    DeleteVFX(5113823, erase_root_only=True)
    EnableFlag(15110800)
    EnableFlag(6327)
    EnableFlag(9327)


@RestartOnRest
def Event15115810():
    """ 15115810: Event 15115810 """
    GotoIfFlagOff(Label.L0, 15110800)
    DisableCharacter(5115800)
    DisableAnimations(5115800)
    Kill(5115800, award_souls=False)
    DeleteVFX(5113820, erase_root_only=False)
    DeleteVFX(5113821, erase_root_only=False)
    DeleteVFX(5113822, erase_root_only=False)
    DeleteVFX(5113823, erase_root_only=False)
    DeleteVFX(5113830, erase_root_only=False)
    DeleteVFX(5113831, erase_root_only=False)
    DeleteVFX(5113832, erase_root_only=False)
    DeleteVFX(5113833, erase_root_only=False)
    DisableObject(5116820)
    EnableObject(5116821)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DeleteVFX(5113820, erase_root_only=False)
    DeleteVFX(5113821, erase_root_only=False)
    DeleteVFX(5113822, erase_root_only=False)
    DeleteVFX(5113823, erase_root_only=False)
    DeleteVFX(5113830, erase_root_only=False)
    DeleteVFX(5113831, erase_root_only=False)
    DeleteVFX(5113832, erase_root_only=False)
    DeleteVFX(5113833, erase_root_only=False)
    EnableObject(5116820)
    DisableObject(5116821)
    DisableAI(5115800)
    DisableCharacter(5110801)
    DisableAnimations(5110801)
    DisableAnimations(5110800)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=4)
    EndIfConditionTrue(-15)
    GotoIfFlagOn(Label.L1, 15110801)
    Move(5110801, destination=5112804, destination_type=CoordEntityType.Region, copy_draw_parent=5110801)
    DisableObject(5111810)
    IfPlayerInOwnWorld(9)
    IfEntityWithinDistance(9, PLAYER, 5110801, radius=120.0)
    IfCharacterInsideRegion(9, PLAYER, region=5112801)
    IfFlagOff(9, 15115852)
    IfConditionTrue(-1, input_condition=9)
    IfAttackedWithDamageType(-1, attacked_entity=5110801, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(51010005, skippable=True, fade_out=True, player_id=PLAYER, move_to_region=5112802, move_to_map=(51, 1))
    SkipLines(7)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    PlayCutscene(
        51010005,
        skippable=False,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=5112802,
        move_to_map=(51, 1),
    )
    SkipLines(4)
    SkipLinesIfCharacterInsideRegion(2, character=PLAYER, region=5112815)
    PlayCutscene(51010005, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(
        51010005,
        skippable=False,
        fade_out=True,
        player_id=PLAYER,
        move_to_region=5112816,
        move_to_map=(51, 1),
    )
    WaitFrames(1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 15115805)
    IfCharacterInsideRegion(1, PLAYER, region=5112800)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    BanishInvaders(unknown=0)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(5111810)
    EnableCharacter(5110801)
    EnableAnimations(5110801)
    EnableAI(5110801)
    SetNetworkUpdateRate(5110801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5110801, 3035)
    ReferDamageToEntity(5110801, 5110800)
    DisableHealthBar(5110801)
    EnableBossHealthBar(5110800, name=906200)
    SetNetworkConnectedFlagState(flag=15110801, state=FlagState.On)


@RestartOnRest
def Event15115811():
    """ 15115811: Event 15115811 """
    EndIfFlagOn(15110800)
    IfHealthLessThan(-1, 5110800, 0.6499999761581421)
    IfHealthEqual(-1, 5110801, 0.0)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    GotoIfTryingToCreateSession(Label.L1)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        51010010,
        CutsceneType.SkippableFadeOut,
        ceremony_id=10,
        unknown=1,
        move_to_region=5112805,
        move_to_map=(51, 1),
        player_id=PLAYER,
    )
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    IfHealthValueLessThanOrEqual(2, PLAYER, 0)
    GotoIfConditionTrue(Label.L2, input_condition=2)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        51010010,
        CutsceneType.UnskippableFadeOut,
        ceremony_id=10,
        unknown=1,
        move_to_region=5112805,
        move_to_map=(51, 1),
        player_id=PLAYER,
    )
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    PlayCutsceneAndSetMapCeremony(
        51010010,
        cutscene_type=CutsceneType.UnskippableFadeOut,
        ceremony_id=10,
        unknown=1,
        player_id=PLAYER,
    )
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfCharacterInsideRegion(Label.L4, character=PLAYER, region=5112810)
    IfHealthValueLessThanOrEqual(4, PLAYER, 0)
    GotoIfConditionTrue(Label.L4, input_condition=4)
    PlayCutsceneAndMovePlayerAndSetMapCeremony(
        51010010,
        CutsceneType.Unskippable,
        ceremony_id=10,
        unknown=1,
        move_to_region=5112806,
        move_to_map=(51, 1),
        player_id=PLAYER,
    )
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    PlayCutsceneAndSetMapCeremony(
        51010010,
        cutscene_type=CutsceneType.Unskippable,
        ceremony_id=10,
        unknown=1,
        player_id=PLAYER,
    )

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(1)
    DisableCharacter(5110801)
    DisableAnimations(5110801)
    Move(5110800, destination=5112807, destination_type=CoordEntityType.Region, copy_draw_parent=5110800)
    EnableCharacter(5110800)
    EnableAnimations(5110800)
    EnableAI(5110800)
    SetNetworkUpdateRate(5110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5110800, 3037)
    EnableFlag(15115802)
    DisableObject(5116820)
    EnableObject(5116821)
    CreateVFX(5113830)
    CreateVFX(5113831)
    CreateVFX(5113832)
    CreateVFX(5113833)


@RestartOnRest
def Event15115812():
    """ 15115812: Event 15115812 """
    EndIfFlagOn(15110800)
    IfFlagOn(1, 15115802)
    IfCharacterHasSpecialEffect(1, 5110800, 16207)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(15115803)
    DeleteVFX(5113830, erase_root_only=True)
    DeleteVFX(5113831, erase_root_only=True)
    DeleteVFX(5113832, erase_root_only=True)
    DeleteVFX(5113833, erase_root_only=True)
    CreateVFX(5113820)
    CreateVFX(5113821)
    CreateVFX(5113822)
    CreateVFX(5113823)


@RestartOnRest
def Event15115847():
    """ 15115847: Event 15115847 """
    DisableNetworkSync()
    EndIfFlagOn(15110800)
    AddSpecialEffect(PLAYER, 16189)
    Wait(0.30000001192092896)
    IfCharacterOutsideRegion(1, PLAYER, region=5112830)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 16189)
    Wait(0.30000001192092896)
    IfCharacterInsideRegion(2, PLAYER, region=5112830)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest
def Event15115848(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 15115848: Event 15115848 """
    DisableNetworkSync()
    DisableObject(arg_4_7)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    IfFlagOn(-1, arg_12_15)
    IfValueComparison(-1, ComparisonType.Equal, left=arg_12_15, right=0)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerNotInOwnWorld(1)
    IfFlagOn(-2, arg_12_15)
    IfValueComparison(-2, ComparisonType.Equal, left=arg_12_15, right=0)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOff(2, arg_0_3)
    IfTryingToCreateSession(-3)
    IfTryingToJoinSession(-3)
    IfConditionTrue(3, input_condition=-3)
    IfFlagOn(3, arg_0_3)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(0, input_condition=-4)
    EnableObject(arg_4_7)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    CreateObjectVFX(arg_8_11, obj=arg_4_7, model_point=101)
    IfFlagOn(-11, arg_12_15)
    IfValueComparison(-11, ComparisonType.Equal, left=arg_12_15, right=0)
    IfConditionTrue(11, input_condition=-11)
    IfPlayerNotInOwnWorld(11)
    IfFlagOn(-12, arg_12_15)
    IfValueComparison(-12, ComparisonType.Equal, left=arg_12_15, right=0)
    IfConditionTrue(12, input_condition=-12)
    IfFlagOff(12, arg_0_3)
    IfTryingToCreateSession(-13)
    IfTryingToJoinSession(-13)
    IfConditionTrue(13, input_condition=-13)
    IfFlagOn(13, arg_0_3)
    IfConditionFalse(14, input_condition=11)
    IfConditionFalse(14, input_condition=12)
    IfConditionFalse(14, input_condition=13)
    IfConditionTrue(0, input_condition=14)
    Restart()


@RestartOnRest
def Event15115849():
    """ 15115849: Event 15115849 """
    RunCommonEvent(20005800, args=(15110800, 5111800, 5112800, 15115805, 5111800, 5115800, 15110801, 0))
    RunEvent(15115895, slot=0, args=(15110800, 5111800, 5112800, 15115805, 5111800, 15115806, 15110801, 0, 5112810))
    SkipLinesIfFlagOn(2, 15110801)
    RunCommonEvent(
        20001838,
        args=(15110800, 15115805, 15115806, 15115810, 5114801, 5114802, 5114803, 15115802, 15115803),
    )
    SkipLines(1)
    RunCommonEvent(
        20005833,
        args=(15110800, 15115805, 15115806, 5112800, 5114801, 5114802, 5114803, 15115802, 15115803),
    )
    RunEvent(15115848, slot=0, args=(15110800, 5111800, 4, 15110801))
    RunCommonEvent(20005810, args=(15110800, 5111800, 5112800, 10000))


@RestartOnRest
def Event15115850():
    """ 15115850: Event 15115850 """
    EndIfFlagOn(15110850)
    IfCharacterDead(1, 5110850)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(15110850)
    EnableFlag(65100604)
    EndIfPlayerNotInOwnWorld()
    DisableFlag(15115852)


@RestartOnRest
def Event15115860():
    """ 15115860: Event 15115860 """
    GotoIfFlagOff(Label.L0, 15110850)
    DisableCharacter(5110850)
    DisableAnimations(5110850)
    DropMandatoryTreasure(5110850)
    DisableBackread(5110850)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    DisableFlag(15115851)
    DisableFlag(15115852)
    DisableAI(5110850)
    DisableCharacter(5110850)
    DisableBackread(5110850)
    DisableAnimations(5110850)
    SetCharacterTalkRange(5110850, distance=100.0)
    DisableFlag(75110150)
    IfCharacterType(-15, PLAYER, CharacterType.BlackPhantom)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=7)
    IfCharacterInvadeType(-15, character=PLAYER, invade_type=21)
    EndIfConditionTrue(-15)
    GotoIfFlagOn(Label.L1, 15115851)
    IfFlagOn(3, 15110800)
    IfFlagOn(3, 15110801)
    IfFlagOff(4, 15110801)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(9, input_condition=-3)
    IfEntityWithinDistance(9, PLAYER, 5110850, radius=60.0)
    IfCharacterInsideRegion(9, PLAYER, region=5112851)
    IfPlayerInOwnWorld(9)
    IfConditionTrue(-1, input_condition=9)
    IfAttackedWithDamageType(-1, attacked_entity=5102850, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 15115855)
    IfConditionTrue(0, input_condition=1)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(15115851)
    EnableFlag(15115852)
    EnableCharacter(5110850)
    EnableBackread(5110850)
    EnableAnimations(5110850)
    SetNetworkUpdateRate(5110850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ActivateMultiplayerBuffs(5110850)
    EnableAI(5110850)
    ForceAnimation(5110850, 63010)
    EnableFlag(15115855)


@RestartOnRest
def Event15115861():
    """ 15115861: Event 15115861 """
    EndIfFlagOn(15110850)
    EndIfFlagOn(15110801)
    IfFlagOn(1, 15115852)
    IfFlagOn(1, 15110801)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(5110850, 91030)
    Wait(2.0)
    DisableCharacter(5110850)
    DisableAnimations(5110850)
    EndIfPlayerNotInOwnWorld()
    IfFlagOn(2, 15110800)
    IfCharacterInsideRegion(2, PLAYER, region=5112850)
    IfConditionTrue(0, input_condition=2)
    EnableCharacter(5110850)
    EnableAnimations(5110850)
    Move(5110850, destination=5112852, destination_type=CoordEntityType.Region, copy_draw_parent=5110850)
    ResetAnimation(5110850, disable_interpolation=False)
    ForceAnimation(5110850, 63010)


@RestartOnRest
def Event15115888(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 15115888: Event 15115888 """
    DisableNetworkSync()
    DisableObject(arg_4_7)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    End()
    IfFlagOff(-1, arg_12_15)
    IfFlagOn(-1, arg_24_27)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerNotInOwnWorld(1)
    IfFlagOn(-2, arg_16_19)
    IfValueComparison(-2, ComparisonType.Equal, left=arg_16_19, right=0)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOff(2, arg_12_15)
    IfFlagOn(-3, arg_24_27)
    IfValueComparison(-3, ComparisonType.Equal, left=arg_24_27, right=0)
    IfConditionTrue(3, input_condition=-3)
    IfFlagOff(3, arg_20_23)
    IfTryingToCreateSession(-4)
    IfTryingToJoinSession(-4)
    IfConditionTrue(4, input_condition=-4)
    IfFlagOn(4, arg_0_3)
    IfConditionTrue(-5, input_condition=1)
    IfConditionTrue(-5, input_condition=2)
    IfConditionTrue(0, input_condition=-5)
    EnableObject(arg_4_7)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    CreateObjectVFX(arg_8_11, obj=arg_4_7, model_point=101)
    IfFlagOff(-11, arg_12_15)
    IfFlagOn(-11, arg_24_27)
    IfConditionTrue(11, input_condition=-11)
    IfPlayerNotInOwnWorld(11)
    IfFlagOn(-12, arg_16_19)
    IfValueComparison(-12, ComparisonType.Equal, left=arg_16_19, right=0)
    IfConditionTrue(12, input_condition=-12)
    IfFlagOff(12, arg_12_15)
    IfFlagOn(-13, arg_24_27)
    IfValueComparison(-13, ComparisonType.Equal, left=arg_24_27, right=0)
    IfConditionTrue(13, input_condition=-13)
    IfFlagOff(13, arg_20_23)
    IfTryingToCreateSession(-14)
    IfTryingToJoinSession(-14)
    IfConditionTrue(14, input_condition=-14)
    IfFlagOn(14, arg_0_3)
    IfConditionFalse(15, input_condition=11)
    IfConditionFalse(15, input_condition=12)
    IfConditionTrue(0, input_condition=15)
    Restart()


@RestartOnRest
def Event15115889():
    """ 15115889: Event 15115889 """
    RunEvent(15115888, slot=0, args=(15110890, 5111850, 2, 15110850, 15115851, 15110800, 15110801))
    RunCommonEvent(20005810, args=(15110890, 5111850, 5112850, 10000))


@RestartOnRest
def Event15115890():
    """ 15115890: Event 15115890 """
    EndIfFlagOn(15110890)
    IfFlagOn(1, 15110800)
    IfFlagOn(1, 15110850)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(15110890)


def Event15115891():
    """ 15115891: Event 15115891 """
    EndIfPlayerNotInOwnWorld()
    CancelSpecialEffect(PLAYER, 4700)
    IfInsideMap(0, game_map=(51, 1))
    AddSpecialEffect(PLAYER, 4700)


@RestartOnRest
def Event15115895(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 15115895: Event 15115895 """
    DisableNetworkSync()
    EndIfFlagOn(arg_0_3)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    DisableFlag(arg_12_15)
    GotoIfValueComparison(Label.L0, ComparisonType.Equal, left=arg_24_27, right=0)
    GotoIfFlagOn(Label.L0, arg_24_27)
    SkipLinesIfEqual(1, left=arg_28_31, right=0)
    IfCharacterInsideRegion(-9, PLAYER, region=arg_28_31)
    IfFlagOn(-9, arg_24_27)
    IfConditionTrue(9, input_condition=-9)
    IfPlayerNotInOwnWorld(9)
    IfCharacterType(9, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=9)
    IfCharacterInsideRegion(15, PLAYER, region=arg_32_35)
    GotoIfConditionTrue(Label.L0, input_condition=15)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(1, arg_0_3)
    IfFlagOn(1, arg_12_15)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=arg_16_19, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_8_11, animation=60060, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfTimeElapsed(-1, 3.0)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    RestartIfFinishedConditionTrue(-1)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_20_23)
    Restart()


@RestartOnRest
def Event15115896(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 15115896: Event 15115896 """
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    IfPlayerNotInOwnWorld(1)
    IfFlagOn(1, arg_0_3)
    IfTryingToCreateSession(-1)
    IfTryingToJoinSession(-1)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=arg_12_15, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_8_11, animation=60060, wait_for_completion=True)
    Restart()


def Event15115700():
    """ 15115700: Event 15115700 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyOn(2, (1835, 1839))
    SetNetworkConnectedFlagRangeState((1835, 1839), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1835, state=FlagState.On)
    IfFlagOn(1, 1836)
    IfFlagOn(1, 70001074)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1835, 1839), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1835, state=FlagState.On)
    SkipLinesIfFlagRangeAnyOn(2, (1820, 1834))
    SetNetworkConnectedFlagRangeState((1820, 1834), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1820, state=FlagState.On)
    GotoIfFlagOff(Label.L9, 1835)
    SkipLinesIfFlagRangeAllOff(4, (1820, 1822))
    SetNetworkConnectedFlagRangeState((1820, 1834), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1823, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1835, 1839), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1837, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70001074)
    SkipLinesIfFlagOn(1, 1838)
    DisableFlag(75110150)

    # --- 10 --- #
    DefineLabel(10)

try:
    import time
    import random
    import pygame
except:
    pass

#해당 코드는 ChatGPT의 조언과 실제 역사 기반의 위키, 문서, 전쟁기념관 문서 등의 도움을 받았습니다.
#이 코드를 읽는 사람중 만약 파이썬 입문자가 있다면, 신속히 Ctrl + S 입력후 Alt + F4 를 입력하세요.

Time_list = ["WW2_E","WW2_M", "WW2_L", "K_W", "VN_W", "C_W", "IRQ_W", "M_W", "F_W"]

#시대별 전차 리스트
#심사숙고하여 선별 및 선정한 조합이니 주의

#|미국(+ 남베트남, 남한)
#example_example_List =       [''                    , ''                   , ''                   , ''                  ] #예시
WW2_Early_USAm_Tank_List =    ['M3A1_Stuart'         , 'M4A1_Sherman'       , 'M3_Lee'             , 'M10_GMC'           ] #WW2 초기
WW2_Middle_USAm_Tank_List =   ['M18_GMC'             , 'M26_Pershing'       , 'M4A3E2_(76)_W_Jumbo', 'M36B2'             ] #WW2 중기
WW2_Late_USAm_Tank_List =     ['M41A1_WalkerBulldog' , 'M46_Patton'         , 'T34'                , 'M56_Scorpion'      ] #WW2 후기
Korean_War_USAm_Tank_List =   ['M41A1_WalkerBulldog' , 'M46_Patton'         , 'M4A3E8_(76)_W_HVSS' , 'M36B2'             ] #6.25 전쟁
Vietnam_War_USAm_Tank_List =  ['M551_Sheridan'       , 'M48_Patton'         , 'M60_SuperPatton'    , 'M50_Ontos'         ] #베트남 전쟁
Cold_War_USAm_Tank_List =     ['M551_Sheridan'       , 'MBT-70'             , 'M103'               , 'M50_Ontos'         ] #냉전
Iraq_War_USAm_Tank_List =     ['M2_Bradley'          , 'M1A1'               , 'M1A1HA'             , 'M103'              ] #이라크 전쟁
Modern_War_USAm_Tank_List =   ['M3_Bradley'          , 'M1A2_SEP_v2'        , 'M1A2_SEP_v3'        , 'M1128_MGS'         ] #현대

#|소련(+ 러시아, 북베트남, 북한)
#USSR_Tank_List =  []

#|독일
#GARM_Tank_List =  []

#일부 CGPT 사용됨
class USA_Tanks:
    def __init__(self, Name, Hp, Speed, MG_I_List, SG_I_List):
        self.Name = Name
        self.Hp = Hp
        self.Speed = Speed
        self.MG_I_List = MG_I_List
        self.SG_I_List = SG_I_List

    def TestPrint(self):
        print(self.Name)
        print(self.Hp)
        print(self.Speed)
        print(self.MG_I_List)
        print(self.SG_I_List)

#전차 객체 생성

#|미국전차

#||포 정보              = [재장전시간, 관통력, 피해량]
#|||WW2_Early_USAm_Tank_List
weC37mmM6               = [ 3.7,  84,  35]                   #M3A1_Stuart
weC75mmM3               = [ 6.5, 102,  75]                   #M4A1_Sherman
weC37mmM5, weC75mmM2    = [ 3.7,  84,  25], [ 6.2,  95,  75] #M3_Lee
weC76mmM7               = [ 6.5, 149, 110]                   #M10_GMC
#|||WW2_Middle_USAm_Tank_List
wmC76mmM1               = [ 7.9, 146, 120]                   #M18_GMC
wmC90mmM3_o             = [ 9.7, 183, 190]                   #M26_Pershing
wmC76mmM1               = [ 7.6, 146, 180]                   #M4A3E2_76_W_Jumbo
wmC90mmM3_s             = [ 9.7, 305, 220]                   #M36B2
#|||WW2_Late_USAm_Tank_List
wlC76mmM32              = [ 7.6, 296, 180]                   #M41A1_WalkerBulldog
wlC90mmM3A1_o           = [ 9.7, 305, 260]                   #M46_Patton
wlC120mmT53             = [19.4, 279, 300]                   #T34
wlC90mmM54              = [ 9.7, 320, 290]                   #M56_Scorpion
#|||Korean_War_USAm_Tank_List
kwC76mmM32              = [ 7.6, 296, 180]                   #M41A1_WalkerBulldog_s
kwC90mmM3A1_s           = [ 9.7, 305, 260]                   #M46_Patton_s
kwC76mmM1A2             = [19.4, 279, 300]                   #M4A3E8_76_W_HVSS
kwC90mmM3_t             = [ 9.7, 320, 290]                   #M36B2_s


#||전차              = Exa_Tanks("전차 이름"             , 체력,속도, 주포 정보    , 부포 정보)
#|||WW2_Early_USAm_Tank_List
M3A1_Stuart          = USA_Tanks("M3A1 스튜어트 경전차"  ,  100,  58,     weC37mmM6,      None)
M4A1_Sherman         = USA_Tanks("M4A1 셔먼"             ,  210,  39,     weC75mmM3,      None)
M3_Lee               = USA_Tanks("M3 리"                 ,  215,  39,     weC37mmM5, weC75mmM2)
M10_GMC              = USA_Tanks("M10 GMC"               ,  190,  39,     weC76mmM7,      None)
#|||WW2_Middle_USAm_Tank_List
M18_GMC              = USA_Tanks("M18 GMC"               ,  210,  80,     wmC76mmM1,      None)
M26_Pershing         = USA_Tanks("M26 퍼싱"              ,  300,  48,   wmC90mmM3_o,      None)
M4A3E2_76_W_Jumbo    = USA_Tanks("M4A3E2 점보셔먼"       ,  375,  42,     wmC76mmM1,      None)
M36B2                = USA_Tanks("M36B2"                 ,  220,  40,   wmC90mmM3_s,      None)
#|||WW2_Late_USAm_Tank_List
M41A1_WalkerBulldog  = USA_Tanks("M41A1 워커불독"        ,  300,  72,    wlC76mmM32,      None)
M46_Patton           = USA_Tanks("M46 패튼"              ,  400,  48, wlC90mmM3A1_o,      None)
T34                  = USA_Tanks("T34"                   ,  550,  35,   wlC120mmT53,      None)
M56_Scorpion         = USA_Tanks("M56 스콜피온"          ,  280,  45,    wlC90mmM54,      None)
#|||Korean_War_USAm_Tank_List
M41A1_WalkerBulldog_s= USA_Tanks("M41A1 워커불독"        ,  300,  72,    kwC76mmM32,      None)
M46_Patton_s         = USA_Tanks("M46 패튼"              ,  400,  48, kwC90mmM3A1_s,      None)
M4A3E8_76_W_HVSS     = USA_Tanks("M4A3E8 이지에잇"       ,  400,  48,   kwC76mmM1A2,      None)
M36B2_s              = USA_Tanks("M36B2"                 ,  220,  40,   kwC90mmM3_t,      None)

#||리스트로 묶기


W2E_UT_L = [M3A1_Stuart          , M4A1_Sherman         , M3_Lee               , M10_GMC              ]
W2M_UT_L = [M18_GMC              , M26_Pershing         , M4A3E2_76_W_Jumbo    , M36B2                ]
W2L_UT_L = [M41A1_WalkerBulldog  , M46_Patton           , T34                  , M56_Scorpion         ]
KoW_UT_L = [M41A1_WalkerBulldog_s, M46_Patton_s         , M4A3E8_76_W_HVSS     , M36B2_s              ]

# --- 함수 정의 ---

def main_menu():
    print("==" * 10)
    print("TankCombat alpha-test ver.0 (CGPT helped TUI)")
    print("1. M3A1 스튜어트 경전차 보기")
    print("q. 종료하기")
    print("==" * 10)
    select = input("번호를 입력하세요: ")
    return select

def show_M3A1():
    print("==" * 10)
    print(f"이름: {M3A1_Stuart.Name}")
    print(f"체력(HP): {M3A1_Stuart.Hp}")
    print(f"속도: {M3A1_Stuart.Speed} km/h")
    print("주포 정보:")
    print(f" - 재장전 시간: {M3A1_Stuart.MG_I_List[0]}초")
    print(f" - 관통력: {M3A1_Stuart.MG_I_List[1]}mm")
    print(f" - 피해량: {M3A1_Stuart.MG_I_List[2]}")
    print("==" * 10)
    choice = input("메인 메뉴로 돌아가려면 '1'을 입력하세요: ")
    return choice

# --- 실행 루프 ---

while True:
    user_input = main_menu()
    if user_input == '1':
        back = show_M3A1()
        if back == '1':
            continue
    elif user_input.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")





    

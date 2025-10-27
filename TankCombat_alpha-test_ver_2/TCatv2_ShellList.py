#TankCombat_alpha-test_ver_2의 포탄 리스트. Made By PYS3301man.
#제작기간 = 시작: 2025-10-25 | 종료: 2025-1

# ['포탄 이름', '포탄 종류', '관통력', '피해량(고폭탄은 작약량)', '작약량(날대탄은 관-피-작 으로 기입)']
#|||WW2_Early_USAm_Tank_List
weSM51B1_37M6                                  = [ 'M51B1',  'APCBC', 84,  35]                             #M3A1_Stuart
weSM61_75M3, weSM48_75M3_o                     = [   'M61',  'APCBC',102,  75], [   'M48',  'HE', 10, 666] #M4A1_Sherman
weSM51B1_37M5                                  = [ 'M51B1',  'APCBC', 84,  25]                             #M3_Lee_MG
weSM61_75M2, weSM48_75M2_s                     = [   'M61',  'APCBC', 95,  75], [   'M48',  'HE', 10, 666] #M3_Lee_SG
weSM62_76M7, weSM42A1_76M7                     = [   'M62',  'APCBC',146, 110], [ 'M42A1',  'HE', 16, 390] #M10_GMC
#|||WW2_Middle_USAm_Tank_List
wmSM62_76M1_o, wmSM42A1_76M1_o, wmSM93_76M1_o  = [   'M62',  'APCBC',146, 120], [ 'M42A1',  'HE', 16, 390], [   'M93',   'APCR',191, 60] #M18_GMC
wmSM82_90M3_o, wmSM71_90M3_o, wmSM304_90M3_o   = [   'M82',  'APCBC',183, 190], [   'M71',  'HE', 20,1200], [  'M304',   'APCR',281, 80] #M26_Pershing
wmSM62_76M1_s, wmSM42A1_76M1_s, wmSM93_76M1_s  = [   'M62',  'APCBC',146, 180], [ 'M42A1',  'HE', 16, 390], [   'M93',   'APCR',191, 60] #M4A3E2_76_W_Jumbo
wmSM82_90M3_s, wmSM71_90M3_s, wmSM304_90M3_s, wmSM348_90M3_o = [   'M82',  'APCBC',183, 200], [   'M71',  'HE', 20,1200], [  'M304',   'APCR',281, 80], [  'M348', 'HEATFS',305, 220, 930] #M36B2
#|||WW2_Late_USAm_Tank_List
wlC76mmM32                                     = [296, 180]                   #M41A1_WalkerBulldog
wlC90mmM3A1_o                                  = [305, 260]                   #M46_Patton
wlC120mmT53                                    = [279, 300]                   #T34
wlC90mmM54                                     = [320, 290]                   #M56_Scorpion
#|||Korean_War_USAm_Tank_List
kwC76mmM32                                     = [296, 180]                   #M41A1_WalkerBulldog_s
kwC90mmM3A1_s                                  = [305, 260]                   #M46_Patton_s
kwC76mmM1A2                                    = [279, 300]                   #M4A3E8_76_W_HVSS
kwC90mmM3_t                                    = [320, 290]                   #M36B2_s



#|||WW2_Early_USAm_Tank_List
weC37mmM6               = [ 3.7,  weSM51B1_37M6]                                     #M3A1_Stuart
weC75mmM3               = [ 6.5,    weSM61_75M3,    weSM48_75M3_o]                   #M4A1_Sherman
weC37mmM5, weC75mmM2    = [ 3.7,  weSM51B1_37M5], [ 6.2, weSM61_75M2, weSM48_75M2_s] #M3_Lee
weC76mmM7               = [ 6.5,    weSM62_76M7,    weSM42A1_76M7]                   #M10_GMC
#|||WW2_Middle_USAm_Tank_List
wmC76mmM1               = [ 7.9,  wmSM62_76M1_o, wmSM42A1_76M1_o,  wmSM93_76M1_o]     #M18_GMC
wmC90mmM3_o             = [ 9.7,  wmSM82_90M3_o,   wmSM71_90M3_o, wmSM304_90M3_o]     #M26_Pershing
wmC76mmM1               = [ 7.6,  wmSM62_76M1_s, wmSM42A1_76M1_s,  wmSM93_76M1_s]     #M4A3E2_76_W_Jumbo
wmC90mmM3_s             = [ 9.7,  wmSM82_90M3_s,   wmSM71_90M3_s, wmSM304_90M3_s, wmSM348_90M3_o] #M36B2
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

#이 코드를 보고 있는 파이썬 입문자분들은 이런 노가다 짓 하지마세요

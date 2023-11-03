import pygame
import os
# 初始化pygame环境
pygame.init()
# 设置一个长为1200，宽为600的窗口
canvas = pygame.display.set_mode((1200, 600))

# 背景图片加载
bg = pygame.image.load('tools/img/bg.png').convert_alpha()
slot1 = pygame.image.load('tools/img/slot1.png').convert_alpha()
slot2 = pygame.image.load('tools/img/slot2.png').convert_alpha()
clock = pygame.time.Clock()
b1 = pygame.image.load(os.getcwd()+'/tools/img/bullet/b1.png').convert_alpha()
b2 = pygame.image.load(os.getcwd()+'/tools/img/bullet/b2.png').convert_alpha()
prompt = pygame.image.load(os.getcwd()+'/tools/img/prompt.png').convert_alpha()
bossPrompt = pygame.image.load(os.getcwd()+'/tools/img/bossPrompt.png').convert_alpha()
continueGame = pygame.image.load(os.getcwd()+'/tools/img/continue.png').convert_alpha()
xuanfu = pygame.image.load(os.getcwd()+'/tools/img/xuanfu.png').convert_alpha()
restartimg = pygame.image.load(os.getcwd()+'/tools/img/restart.png').convert_alpha()
suspend = pygame.image.load(os.getcwd()+'/tools/img/pause.png').convert_alpha()
# 将所有动画帧图片对象存储到列表中
# 貂移动图片列表
martenM = []
for i in range(6):
	martenM.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/marten/move/' + str(i) + '.png').convert_alpha())
# 貂攻击图片列表
martenA = []
for i in range(9):
	martenA.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/marten/attack/' + str(i) + '.png').convert_alpha())
# 貂被击倒图片列表
martenD = []
for i in range(9):
	martenD.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/marten/die/' + str(i) + '.png').convert_alpha())
# 红龙移动图片列表
redM = []
for i in range(12):
	redM.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/reddragon/move/' + str(i) + '.png').convert_alpha())
# 红龙攻击图片列表
redA = []
for i in range(19):
	redA.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/reddragon/attack/' + str(i) + '.png').convert_alpha())
# 红龙被击倒图片列表
redD = []
for i in range(4):
	redD.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/reddragon/die/' + str(i) + '.png').convert_alpha())
# 蓝龙移动图片列表
blueM = []
for i in range(12):
	blueM.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bluedragon/move/' + str(i) + '.png').convert_alpha())
# 蓝龙攻击图片列表
blueA = []
for i in range(12):
	blueA.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bluedragon/attack/' + str(i) + '.png').convert_alpha())
# 蓝龙被击倒图片列表
blueD = []
for i in range(6):
	blueD.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bluedragon/die/' + str(i) + '.png').convert_alpha())
# 猫移动图片列表
catM = []
for i in range(5):
	catM.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/cat/move/' + str(i) + '.png').convert_alpha())
# 猫攻击图片列表
catA = []
for i in range(13):
	catA.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/cat/attack/' + str(i) + '.png').convert_alpha())
# 猫被击倒图片列表
catD = []
for i in range(7):
	catD.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/cat/die/' + str(i) + '.png').convert_alpha())
# 鸟移动
birdM = []
for i in range(7):
	birdM.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bird/move/' + str(i) + '.png').convert_alpha())
# 鸟攻击
birdA = []
for i in range(13):
	birdA.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bird/attack/' + str(i) + '.png').convert_alpha())
# 鸟死亡
birdD = []
for i in range(6):
	birdD.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/bird/die/' + str(i) + '.png').convert_alpha())
# 能量
energies = []
for i in range(5):
	energies.append(pygame.image.load(os.getcwd()+'/tools/img/energy/' + str(i) + '.png').convert_alpha())
# 射手图片列表
shooters = []
for i in range(6):
	shooters.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/shooter/' + str(i) + '.png').convert_alpha())
# 炸弹
bombs = []
for i in range(8):
	bombs.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/bomb/' + str(i) + '.png').convert_alpha())
# 石头状态1
stones1 = []
for i in range(6):
	stones1.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/stone/state1/' + str(i) + '.png').convert_alpha())
# 石头状态2
stones2 = []
for i in range(6):
	stones2.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/stone/state2/' + str(i) + '.png').convert_alpha())
# 石头状态3
stones3 = []
for i in range(6):
	stones3.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/stone/state3/' + str(i) + '.png').convert_alpha())
# boss1移动
boss1M = []
for i in range(14):
	boss1M.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/boss1/move/' + str(i) + '.png').convert_alpha())
# boss1攻击
boss1A = []
for i in range(21):
	boss1A.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/boss1/attack1/' + str(i) + '.png').convert_alpha())
# boss1仰头：
boss1H = []
for i in range(8):
	boss1H.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/boss1/attack2/' + str(i) + '.png').convert_alpha())
# boss1出场攻击
boss1P = []
for i in range(14):
	boss1P.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/boss1/poom/' + str(i) + '.png').convert_alpha())
# boss1死亡
boss1D = []
for i in range(11):
	boss1D.append(pygame.image.load(os.getcwd()+'/tools/img/attacker/boss1/die/' + str(i) + '.png').convert_alpha())
# 符阵
buffs = []
for i in range(14):
	buffs.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/buff/' + str(i) + '.png').convert_alpha())
# 爆炸
fires = []
for i in range(8):
	fires.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/bomb/fires/'+str(i)+'.png').convert_alpha())
# 蒙层
layers = []
for i in range(3):
	layers.append(pygame.image.load(os.getcwd()+'/tools/img/end/'+str(i)+'.png').convert_alpha())
# 失败蒙层
layers_end = []
for i in range(3):
	layers_end.append(pygame.image.load(os.getcwd()+'/tools/img/end2/'+str(i)+'.png').convert_alpha())
# 胜利失败
win = pygame.image.load(os.getcwd()+'/tools/img/end/win.png').convert_alpha()
lose = pygame.image.load(os.getcwd()+'/tools/img/end/lose.png').convert_alpha()
# 血条
blood1 = pygame.image.load(os.getcwd()+'/tools/img/blood/1.png').convert_alpha()
blood2 = pygame.image.load(os.getcwd()+'/tools/img/blood/2.png').convert_alpha()
blood3 = pygame.image.load(os.getcwd()+'/tools/img/blood/3.png').convert_alpha()
blood4 = pygame.image.load(os.getcwd()+'/tools/img/blood/4.png').convert_alpha()
# 法师攻击状态
masterA = []
for i in range(9):
	masterA.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/master/attack/'+str(i)+'.png').convert_alpha())
# 法师站立状态
masterS = []
for i in range(6):
	masterS.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/master/stand/'+str(i)+'.png').convert_alpha())
# 攻击类型2
masterA2 = []
for i in range(3):
	masterA2.append(pygame.image.load(os.getcwd()+'/tools/img/bullet/weapon2/'+str(i)+'.png').convert_alpha())
# 第二关防御者站立
guardS = []
for i in range(15):
	guardS.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/guard/stand/'+str(i)+'.png').convert_alpha())
# 第二关防御者攻击
guardA = []
for i in range(4):
	guardA.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/guard/attack/'+str(i)+'.png').convert_alpha())
# 第二关防御者盾牌（发招）
sh = []
for i in range(6):
	sh.append(pygame.image.load(os.getcwd()+'/tools/img/defendor/guard/shield/'+str(i)+'.png').convert_alpha())
# 生命值减少动画
lifeR = []
for i in range(14):
	lifeR.append(pygame.image.load(os.getcwd()+'/tools/img/lifereduce/'+str(i)+'.png').convert_alpha())
# 防御值进度条
defenses = []
for i in range(5):
	defenses.append(pygame.image.load(os.getcwd()+'/tools/img/defense/'+str(i)+'.png').convert_alpha())
# 第二关防御值进度条
defenses2 = []
for i in range(5):
	defenses2.append(pygame.image.load(os.getcwd()+'/tools/img/defense2/'+str(i)+'.png').convert_alpha())
floats = []
# 浮动
for i in range(15):
	floats.append(pygame.image.load(os.getcwd() + '/tools/img/float/' + str(i+1) + '.png').convert_alpha())

pygame.mixer.init()
bgm = pygame.mixer.Sound(os.getcwd()+'/tools/sound/bgm.wav')
boom = pygame.mixer.Sound(os.getcwd()+'/tools/sound/boom.wav')
bulletmusic = pygame.mixer.Sound(os.getcwd()+'/tools/sound/bulletmusic.wav')
warning = pygame.mixer.Sound(os.getcwd()+'/tools/sound/warning.wav')
defenseReduceM = pygame.mixer.Sound(os.getcwd()+'/tools/sound/lifereduce.wav')
winMusic = pygame.mixer.Sound(os.getcwd()+'/tools/sound/win.wav')
loseMusic = pygame.mixer.Sound(os.getcwd()+'/tools/sound/lose.wav')
bgm.set_volume(0.05)
warning.set_volume(0.05)
boom.set_volume(0.05)
bulletmusic.set_volume(0.04)
defenseReduceM.set_volume(0.05)
winMusic.set_volume(0.05)
loseMusic.set_volume(0.05)

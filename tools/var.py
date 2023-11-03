from tools.load import *
import time
class Game():
    # 初始能量
    energy = 80
    # 攻击者出现的间隔
    animalInterval = 3
    # 防御值
    defense = 100
    # 子弹行数
    row = 1
    # 子弹间隔
    shootInterval = 1
    # 守护者对象
    defendor = None
    # 当前选中的守卫者的名字
    currentName = None
    # 当前选中守卫者的宽高,能量值,生命值
    currentWidth = 0
    currentHeight = 0
    currentEnergy = 0
    currentLife = 0
    # 放置守卫者的列表
    defendors = []
    # 放置卡片的列表
    cards = []
    # 判断是否应该产生守卫者对象的标识
    f1 = False
    # 判断卡片是否不消失的标识
    f2 = True
    # 判断能量够不够的标识
    isEnough = True
    # 判断是否能量够不够的表示
    isPrompt = False
    # 判断是否提示boss出现
    isPromptB = False
    lastTime = 0
    # 攻击者对象列表
    attackers = []
    # 攻击者子弹列表
    bullets = []
    # 能量列表
    energy_list = []
    # 攻击者die对象列表
    dies = []
    # 计算攻击者出现的起始时间/游戏进行时间
    startTime = time.time()
    # 计时器（提示能量不足）
    num = -1
    # 计时器（提示boss出现）
    Bnum = -1
    # 提示初始坐标
    promptY = 600
    # boss提示初始坐标
    promptBY = 600
    # 轮播计数变量
    n = 0
    # 最后12只计数
    animalNum = 10
    index_list = []
    isAttack = True
    isBoss = False
    # 游戏状态
    state = 'RUNNING'
    # 防御值下标
    d_i = 0
    # 生命值减少轮播下标
    defense_i = 0
    # 暂停轮播间隔
    pauseLastTime = 0
    a_img = lifeR[0]
    isBgmMusic = True
    isPauseMusic = True
    isWinMusic = True
    isLoseMusic = True
    endLastTime = 0
    t = 0
    endNum2 = 10
    card_list = []
    isShoot = False
    isShield = False
    shootInterval2 = 0.5
    ori_defense = defense
    is_ori_first = True
    user_row = 0
    user_shootInterval = 0
    user_energy = 0
    user_interval = 0
    user_defense = 0
    pos_list = [[495, 555], [572, 632], [652, 715], [731, 795]]
    card_x1 = 0
    card_x2 = 0


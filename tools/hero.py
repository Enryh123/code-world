from tools.var import *
from tools.load import *
import random,math

canvas.fill([255, 255, 255])

# 卡片类
class Card():
	def __init__(self,name,x1,x2,y1,y2,defendor_width,defendor_height,energy,life):
		self.name = name
		self.img = pygame.image.load(os.getcwd()+'/tools/img/card/'+self.name+'.png')
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.mouse_pos = [0,0]
		self.defendor_width = defendor_width
		self.defendor_height = defendor_height
		self.energy = energy
		self.life = life
	def paint(self):
		canvas.blit(self.img,(self.x1,self.y1))
	def judge_pos(self):
		x = self.mouse_pos[0]
		y = self.mouse_pos[1]
		if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 and Game.energy>=self.energy:
			Game.isEnough = True
			Game.currentName = self.name
			Game.currentWidth = self.defendor_width
			Game.currentHeight = self.defendor_height
			Game.currentEnergy = self.energy
			Game.currentLife = self.life
			img_list = get_list(Game.currentName)
			Game.defendor = Defendor(self.name,x,y,self.energy,self.life,self.life,img_list,self.defendor_width,self.defendor_height)
			Game.cards.append(Game.defendor)
			Game.f1 = True
			Game.f2 = True
		elif x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 and Game.energy<self.energy:
			Game.defendor = None
			Game.isEnough = False
			Game.isPrompt = True
			Game.cards.clear()



class Defendor():
	def __init__(self,name,mouse_x,mouse_y,energy,life,clife,img_list=None,width=0,height=0):
		self.name = name
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y
		self.width = width
		self.height = height
		self.x = self.mouse_x - self.width/2
		self.y = self.mouse_y - self.height/2
		self.index = 0
		self.energy = energy
		self.img_list = img_list
		self.img = self.img_list[self.index%len(self.img_list)]
		self.lastTime = 0
		self.interval = 0.07
		self.shootLastTime = 0
		self.shootInterval = Game.shootInterval
		self.life = life
		self.state = None
		self.isjudge = True
		self.n = 0
		self.bloodImg = blood1
		self.isShowBlood = False
		self.correctLife = clife
		self.isProtect = True
	def paintPlace(self):
		if self.name == 'buff' and self.isjudge:
			self.y -= 7
			self.isjudge = False
		img_rect = self.img.get_rect()
		img_rect.center = (self.x,self.y)
		canvas.blit(self.img,img_rect)
	def paintMove(self):
		canvas.blit(self.img,(self.x,self.y))
	def paintBlood(self):
		img_rect = self.bloodImg.get_rect()
		if self.name == 'guard':
			b_x = self.x + 10
			b_y = self.y - self.height / 2
		elif self.name == 'shield':
			b_x = self.x-10
			b_y = self.y - self.height / 2+20
		else:
			b_x = self.x
			b_y = self.y-self.height/2-17
		img_rect.center = (b_x,b_y)
		canvas.blit(self.bloodImg,img_rect)
	def animation(self):
		if not isActionTime(self.lastTime,self.interval):
			return
		self.lastTime = time.time()
		if self.name == 'shooter':
			self.img = shooters[self.index % 6]
		elif self.name == 'buff':
			self.img = buffs[self.index % 14]
		elif self.name == 'stone':
			self.img = self.img_list[self.index % 6]
		elif self.name == 'bomb' and self.state==None:
			self.img = bombs[self.index % 7]
		elif self.name == 'bomb' and self.state == 'b' :
			if self.n == 0:
				self.index = 0
			self.img = fires[self.index % 9]
			self.n += 1
		else:
			self.img = self.img_list[self.index % len(self.img_list)]
			if len(Game.attackers) > 0:
				if self.name == 'master':
					self.img_list = masterA
				elif self.name == 'guard':
					self.img_list = guardA
		self.index += 1
	# 射击
	def shoot1(self):
		if not isActionTime(self.shootLastTime,self.shootInterval):
			return
		self.shootLastTime = time.time()
		if Game.row == 1:
			Game.bullets.append(Bullet1(self.x+self.width-20,self.y-10,27,34,b1))
		elif Game.row == 2:
			Game.bullets.append(Bullet1(self.x + self.width - 20, self.y - 10, 27, 34, b1))
			Game.bullets.append(Bullet1(self.x + self.width - 20, self.y + 10, 27, 34, b1))
		elif Game.row >= 3:
			for i in range(Game.row):
				# 偶数
				if i == 0:
					Game.bullets.append(Bullet1(self.x + self.width - 20, self.y, 27, 34, b1))
				elif i == 1:
					Game.bullets.append(Bullet1(self.x + self.width - 20, self.y - 12, 27, 34, b1))
				elif i == 2:
					Game.bullets.append(Bullet1(self.x + self.width - 20, self.y + 12, 27, 34, b1))
				elif i%2 == 1:
					Game.bullets.append(Bullet1(self.x + self.width - 20, self.y - i * 8, 27, 34, b1))
				else:
					Game.bullets.append(Bullet1(self.x + self.width - 20, self.y + (i - 1) * 8, 27, 34, b1))
	def shoot2(self):
		if not isActionTime(self.shootLastTime, self.shootInterval):
			return
		self.shootLastTime = time.time()
		s_x = random.randint(0, 900)
		Game.bullets.append(Bullet2(s_x, -100, 86, 116, masterA2, 3, 2))
	def showShield(self):
		if self.isProtect:
			Game.defendors.append(Defendor('shield',self.x+190,self.y+170,0,self.life,self.life, sh,234, 325))
			self.isProtect = False
	# 定义hit方法判断两个对象之间是否发生碰撞
	def hit(self, component):
		c = component
		result = c.x>self.x-self.width/2-c.width/2+50 and \
				 c.x<self.x+self.width/2+c.width/2 and \
				 c.y>self.y-self.height/2-c.height/2 and \
				 c.y<self.y+self.height/2+c.height/2
		return result

# 定义攻击者类
class Attacker():
	def __init__(self,x,y,width,height,img_list,type,life,move_num,attack_num,energy,speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.state = 'move'
		self.type = type
		self.index = 0
		self.img_list = img_list
		self.frame = self.img_list[self.index]
		self.life = life
		self.lastTime = 0
		self.interval = 0.09
		self.eatLastTime = 0
		self.eatInterval = 0.1
		self.move_num = move_num
		self.attack_num = attack_num
		self.energy = energy
		self.speed = speed
		self.n = 0
		self.h = 0
		self.isbomb = False
	#创建画攻击者和攻击者移动方法
	def paint(self):
		img_rect = self.frame.get_rect()
		img_rect.center = (self.x, self.y)
		canvas.blit(self.frame, img_rect)
	def move(self):
		self.x -= self.speed
	#攻击者播放动画方法
	def animation(self):
		#判断是否到了图片切换的时间
		if not isActionTime(self.lastTime,self.interval):
			return
		self.lastTime = time.time()
		if self.state == 'move':
			self.frame = self.img_list[self.index % self.move_num]
			self.move()
		elif self.state == 'stand':
			self.frame = self.img_list[self.index % 6]
		elif self.state == 'attack':
			self.frame = self.img_list[self.index % self.attack_num]
		elif self.state == 'head':
			if self.h == 0:
				self.index = 0
			self.frame = boss1H[self.index % 8]
			self.h += 1
			if self.h >= 8:
				self.state = 'move'
		elif self.state == 'die':
			if self.n == 0:
				self.index = 0
			n = len(switch_die(self.type))
			self.frame = switch_die(self.type)[self.index % n]
			if self.index%n == n-1:
				if self.n > 5:
					e = Energy(self.x,self.y,energies,self.energy)
					Game.energy_list.append(e)
					Game.attackers.remove(self)
			self.n += 1
		self.index += 1
	# 定义hit方法判断两个对象之间是否发生碰撞
	def hit(self, component):
		c = component
		return  self.x>c.x-c.width/2-self.width/2+30 and self.x<c.x+c.width/2+self.width/2

class componentDie():
	def __init__(self,x,y,type=0,energy=None,ob = None):
		self.x = x
		self.y = y
		self.type = type
		self.index = 0
		self.n = 0
		self.len = len(switch_die(self.type))
		self.frame = switch_die(self.type)[self.index % self.len]
		self.energy = energy
		self.lastTime = 0
		self.interval = 0.07
		self.ob = ob
		self.m = 0
	def paint(self):
		img_rect = self.frame.get_rect()
		img_rect.center = (self.x,self.y)
		canvas.blit(self.frame,img_rect)
	def animation(self):
		if not isActionTime(self.lastTime,self.interval):
			return
		self.lastTime = time.time()
		if self.n == 0:
			self.index = 0
		self.frame = switch_die(self.type)[self.index % self.len]
		# 爆炸的情况
		if self.type == 7:
			if self.n > 7:
				Game.dies.remove(self)
				for a in Game.attackers:
					if a.x > self.x-150 and a.x <= self.x+200 and a.y > self.y-120 and a.y < self.y + 100 and a.type!=5:
						a.isbomb = True
						a.state = 'die'
		# boss1出场随机打击
		elif self.type == 6:
			if self.n > 12:
				Game.dies.remove(self)
				try :
					Game.defendors.remove(self.ob)
				except:
					pass
		elif self.type == 5:
			if self.m > 10:
				Game.dies.remove(self)
			self.m += 1
		else:
			if self.n > 15:
				e = Energy(self.x, self.y, energies, self.energy)
				Game.energy_list.append(e)
				Game.dies.remove(self)
		self.n += 1
		self.index += 1

class Bullet1():
	def __init__(self,x,y,width,height,img):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.img = img
		self.sign = 'normal'
		self.isBulletMusic = True
		self.id = 's1'
	def paint(self):
		img_rect = self.img.get_rect()
		img_rect.center = (self.x,self.y)
		canvas.blit(self.img,img_rect)
	def step(self):
		self.x += 4
class Energy():
	def __init__(self,x,y,img_list,energy):
		self.x = x
		self.y = y
		self.img_list = img_list
		self.index = 0
		self.frame = self.img_list[self.index]
		self.lastTime = 0
		self.interval = 0.07
		self.energy = energy
	def paint(self):
		img_rect = self.frame.get_rect()
		img_rect.center = (self.x,self.y)
		canvas.blit(self.frame,img_rect)
	def animation(self):
		#判断是否到了图片切换的时间
		if not isActionTime(self.lastTime,self.interval):
			return
		self.lastTime = time.time()
		self.frame = self.img_list[self.index % 5]
		self.index+=1
	def move(self):
		if self.index>10:
			if self.x>0 and self.y>0:
				self.x -= 20
				self.y += 20
			if self.x<=440:
				self.x = 440
			if self.y >= 520:
				self.y = 520
			if self.x <= 440 and self.y >= 520:
				Game.energy_list.remove(self)
				Game.energy += self.energy

class Bullet2():
	def __init__(self,x,y,width,height,img_list,imgNum,type,num=3):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.index = 0
		self.imgNum = imgNum
		self.img_list = img_list
		self.img = self.img_list[self.index%self.imgNum]
		self.sign = 'normal'
		self.num = num
		self.type = type
		self.lastTime = 0
		self.interval = 0.07
		self.isBulletMusic = True
		self.id = 's2'
	def paint(self):
		img_rect = self.img.get_rect()
		img_rect.center = (self.x,self.y)
		canvas.blit(self.img,img_rect)
	def animation(self):
		if self.type == 4:
			self.interval = 0.08
		if not isActionTime(self.lastTime,self.interval):
			return
		self.lastTime = time.time()
		self.img = self.img_list[self.index%self.imgNum]
		self.index += 1
	def step(self):
		if self.type == 0 or self.type == 1:
			if self.num == 1:
				self.x += 6
				self.y -= 2
			elif self.num ==2:
				self.x += 6
				self.y -= 1
			elif self.num ==3:
				self.x += 6
			elif self.num == 4:
				self.x += 6
				self.y += 1
			elif self.num == 5:
				self.x += 6
				self.y += 2
		elif self.type == 2:
			self.x += 5
			self.y += 6
# 显示文字的方法
def fill_text(text,pos,size,isEnd):
	f = pygame.font.SysFont(None, size)
	t = f.render(str(text), True, (255, 255, 255))
	if isEnd:
		canvas.blit(t,pos)
	else:
		t_rect = t.get_rect()
		t_rect.center = pos
		canvas.blit(t,t_rect)

def checkHit():
	for attacker in Game.attackers:
		# 攻击者和守护者的碰撞
		for defendor in Game.defendors:
			if defendor.name != 'shield':
				if isInOne1(attacker,defendor):
					if attacker.hit(defendor):
						afterHit(1,attacker,defendor)
			else:
				if attacker.x>defendor.x-defendor.width/2-attacker.width/4 and attacker.x<defendor.x+defendor.width/2 and attacker.y>defendor.y-110 and attacker.y<defendor.y+100:
					afterHit(1, attacker, defendor)
		# 攻击者和子弹的碰撞
		for bullet in Game.bullets:
			if bullet.id == 's1':
				if isInOne2(attacker,bullet):
					if attacker.hit(bullet):
						afterHit(2,attacker,bullet=bullet)
			else:
				if attacker.x > bullet.x - bullet.width / 2 - attacker.width / 2 + 30 and attacker.x < bullet.x + bullet.width / 2 + attacker.width / 2 and bullet.y > attacker.y - attacker.height / 2 - bullet.height / 2 + 50:
					afterHit(2, attacker, bullet=bullet)
	# # 子弹和符阵的碰撞
	for bullet in Game.bullets:
		for defendor in Game.defendors:
			if defendor.name == 'buff' :
				if defendor.hit(bullet):
					bullet.img = b2
					bullet.sign = 'buffmode'

def afterHit(bangsign,Attacker,defendor=None,bullet=None):
	# 攻击者和守护者碰撞后的事情
	if bangsign == 1:
		if (Attacker.type!=5 or defendor.name!='bomb') and Attacker.state != 'die':
			img_list = switch_attack(Attacker.type)
			Attacker.state = 'attack'
			Attacker.img_list = img_list
			defendor.isShowBlood = True
		if defendor.life > defendor.correctLife*0.9:
			defendor.bloodImg = blood1
			if defendor.name == 'stone':
				defendor.img = stones1[defendor.index%6]
		elif defendor.life > defendor.correctLife*0.7:
			defendor.bloodImg = blood2
			if defendor.name == 'stone':
				defendor.img = stones1[defendor.index%6]
		elif defendor.life > defendor.correctLife*0.35:
			defendor.bloodImg = blood3
			if defendor.name == 'stone':
				defendor.img = stones2[defendor.index%6]
				defendor.img_list = stones2
		elif defendor.life > 0:
			defendor.bloodImg = blood4
			if defendor.name == 'stone':
				defendor.img = stones3[defendor.index%6]
				defendor.img_list = stones3
		# 攻击者碰撞炸弹后做的事
		if defendor.name == 'bomb':
			warning.stop()
			boom.play()
			Game.dies.append(componentDie(defendor.x,defendor.y,7))
			Game.defendors.remove(defendor)
		if defendor.life==1:
			Attacker.state = 'move'
			img_list = switch_move(Attacker.type)
			Attacker.img_list = img_list
		elif defendor.life == 0:
			# 攻击者吃掉守护者，继续往前走
			Attacker.state = 'move'
			img_list = switch_move(Attacker.type)
			Attacker.img_list = img_list
			Game.defendors.remove(defendor)
			return
		if not isActionTime(Attacker.eatLastTime,Attacker.eatInterval):
			return
		Attacker.eatLastTime = time.time()
		defendor.life -= 1
	# 子弹和攻击者碰撞后做的事
	elif bangsign == 2:
		if bullet.isBulletMusic:
			bulletmusic.play()
			bullet.isBulletMusic = False
		Game.bullets.remove(bullet)
		if Attacker.life >= 1:
			if Attacker.type==5 and Attacker.x > 1150:
				return
			if bullet.sign == 'normal':
				Attacker.life -= 1
			elif bullet.sign == 'buffmode':
				Attacker.life -= 2
			if Attacker.life == 0 or Attacker.life == -1:
				try:
					Game.attackers.remove(Attacker)
					# 播放动画
					Game.dies.append(componentDie(Attacker.x, Attacker.y,Attacker.type, Attacker.energy))
					return
				except ValueError:
					pass

# 切换攻击者攻击的方法
def switch_attack(type):
	if type == 1:
		img_list = martenA
	elif type == 2:
		img_list = blueA
	elif type == 3:
		img_list = catA
	elif type == 4:
		img_list = redA
	elif type == 5:
		img_list = boss1A
	elif type == 10:
		img_list = birdA
	return img_list
# 切换攻击者移动的方法
def switch_move(type):
	if type == 1:
		img_list = martenM
	elif type == 2:
		img_list = blueM
	elif type == 3:
		img_list = catM
	elif type == 4:
		img_list = redM
	elif type == 5:
		img_list = boss1M
	elif type == 10:
		img_list = birdM
	return img_list
# 切换攻击者被击倒的方法
def switch_die(type):
	if type == 1:
		img_list = martenD
	elif type == 2:
		img_list = blueD
	elif type == 3:
		img_list = catD
	elif type == 4:
		img_list = redD
	elif type == 5:
		img_list = boss1D
	elif type == 6:
		img_list = boss1P
	elif type == 7:
		img_list = fires
	elif type == 10:
		img_list = birdD
	return img_list

def place_defendor(x,y):
	area_x = 190
	area_y = -47
	for i in range(60):
		if Game.f1:
			if i % 12 == 0:
				area_x = 190
				area_y += 90
			if x >= area_x and x <= area_x + 85 and y >= area_y and y <= area_y + 90 and Game.isEnough:
				image_list = get_list(Game.currentName)
				d = Defendor(Game.currentName, x, y, Game.currentEnergy, Game.currentLife, Game.currentLife, image_list, Game.currentWidth,
							 Game.currentHeight)
				d.x = area_x + 85 / 2
				d.y = area_y + 90 / 2
				Game.defendors.append(d)
				Game.energy -= d.energy
				Game.f2 = False
				Game.f1 = False
				Game.cards.clear()
				break
			area_x += 85

def isChooseCard(x,y):
	if len(Game.card_list) == 0:
		return False
	elif len(Game.card_list) == 1:
		if 495 <= x <= 550 and 515 <= y <= 595:
			return True
		return False
	elif len(Game.card_list) == 2:
		if 495 <= x <= 550 and 515 <= y <= 595 or 570 <= x <= 625 and 515 <= y <= 595:
			return True
		return False
	elif len(Game.card_list) == 3:
		if 495 <= x <= 550 and 515 <= y <= 595 or 570 <= x <= 625 and 515 <= y <= 595 or \
				650 <= x <= 705 and 515 <= y <= 595:
			return True
		return False
	elif len(Game.card_list) == 4:
		if 495 <= x <= 550 and 515 <= y <= 595 or 570 <= x <= 625 and 515 <= y <= 595 or \
				650 <= x <= 705 and 515 <= y <= 595 or 730 <= x <= 785 and 515 <= y <= 595:
			return True
		return False

def switchRunning():
	Game.state = 'RUNNING'
	Game.isPauseMusic = True
	Game.defense_i = 0
	Game.startTime = Game.startTime + int((time.time() - Game.startTime) - Game.t)

def restart():
	Game.state = 'RUNNING'
	Game.row = Game.user_row
	Game.shootInterval = Game.user_shootInterval
	Game.energy = Game.user_energy
	Game.animalInterval = Game.user_interval
	Game.defense = Game.user_defense
	Game.defendor = None
	Game.currentName = None
	Game.currentWidth = 0
	Game.currentHeight = 0
	Game.currentEnergy = 0
	Game.currentLife = 0
	Game.defendors.clear()
	Game.cards.clear()
	Game.f1 = False
	Game.f2 = True
	Game.isEnough = True
	Game.isPrompt = False
	Game.isPromptB = False
	Game.lastTime = 0
	Game.attackers.clear()
	Game.bullets.clear()
	Game.energy_list.clear()
	Game.dies.clear()
	Game.startTime = time.time()
	Game.num = -1
	Game.Bnum = -1
	Game.promptY = 600
	Game.promptBY = 600
	Game.n = 0
	Game.animalNum = Game.endNum2
	Game.index_list = []
	Game.isAttack = True
	Game.isBoss = False
	Game.d_i = 0
	Game.defense_i = 0
	Game.pauseLastTime = 0
	Game.a_img = lifeR[0]
	Game.isBgmMusic = True
	Game.isPauseMusic = True
	Game.isWinMusic = True
	Game.isLoseMusic = True
	Game.endLastTime = 0
	Game.t = 0
	Game.ori_defense = Game.defense
	Game.is_ori_first = True

def clickCard(pos):
	Game.f1 = True
	for c in Game.card_list:
		c.mouse_pos = pos
		c.judge_pos()


# 获取守护者名对应的列表
def get_list(currentName):
	if currentName == 'buff':
		img_list = buffs
	elif currentName == 'shooter':
		img_list = shooters
	elif currentName == 'bomb':
		img_list = bombs
	elif currentName == 'stone':
		img_list = stones1
	elif currentName == 'master':
		img_list = masterS
	elif currentName == 'guard':
		img_list = guardS
	return img_list

#添加时间间隔的方法
def isActionTime(lastTime, interval):
	if lastTime == 0:
		return True
	currentTime = time.time()
	return currentTime - lastTime >= interval



# 攻击者和守护者是否在同一行的判定
def isInOne1(Attacker,defendor):
	if Attacker.type != 5:
		if Attacker.y==80 and defendor.y>=45 and defendor.y<135:
			return True
		elif Attacker.y==170 and defendor.y>=135 and defendor.y<225:
			return True
		elif Attacker.y==270 and defendor.y>=225 and defendor.y<315:
			return True
		elif Attacker.y==360 and defendor.y>=315 and defendor.y<405:
			return True
		elif Attacker.y==450 and defendor.y>=405 and defendor.y<595:
			return True
	else:
		if defendor.y>=225 and defendor.y<315 or \
				defendor.y>=315 and defendor.y<405:
			return True

# 攻击者和子弹是否在同一行的判定
def isInOne2(Attacker,bullet):
	if Attacker.type != 5:
		if Attacker.y==80 and bullet.y>=45 and bullet.y<=135:
			return True
		elif Attacker.y==170 and bullet.y>=135 and bullet.y<=225:
			return True
		elif Attacker.y==270 and bullet.y>=225 and bullet.y<=315:
			return True
		elif Attacker.y==360 and bullet.y>=315 and bullet.y<=405:
			return True
		elif Attacker.y==450 and bullet.y>=405 and bullet.y<=595:
			return True
	else:
		if (bullet.y>=135 and bullet.y<=225 or \
				bullet.y>=225 and bullet.y<=315 or \
				bullet.y>=315 and bullet.y<=405) and bullet.id=='s1':
			return True

# 蒙层切换
def swtich_layer(isEnd=False):
	global layerImg
	if not isActionTime(Game.endLastTime,0.07):
			return layerImg
	Game.endLastTime = time.time()
	Game.n += 1
	if Game.n > 2:
		Game.n = 2
	if isEnd:
		layerImg = layers_end[Game.n]
	else:
		layerImg = layers[Game.n]
	return layerImg
# 显示胜利或者失败
def end(state,image):
	canvas.blit(image, (0, 0))
	if state == 'win':
		canvas.blit(win, (400, 200))
	elif state == 'lose':
		canvas.blit(lose, (400, 150))


# 警报声
def firstWaring():
	warning.play(loops=0)

# 计算游戏进行时间
def timeJudge():
	endTime = time.time()
	Game.t = int(endTime - Game.startTime)
# boss出场打击
def bossAttack(a):
	a.state = 'head'
	s = 1
	i = 0
	while i < math.ceil(len(Game.defendors)*0.7):
		i += 1
		randN = random.randint(0,len(Game.defendors)-1)
		if Game.defendors[randN].name == 'guard':
			i -= 1
			continue
		if randN not in Game.index_list:
			Game.index_list.append(randN)
			d = Game.defendors[randN]
			Game.dies.append(componentDie(d.x,d.y,6,ob=d))
			s += 1

# 防御值显示
def showDefense():
		canvas.blit(defenses[Game.d_i],(493,500))
# 卡槽重绘
def rePaint():
	canvas.blit(slot1,(384,494))
	# 卡片的绘制
	for c in Game.card_list:
		c.paint()

def createAttObject(n,y):
	# 红龙
	if n > 8:
		z = Attacker(1255,y,110,95,redM,4,12,len(redM),len(redA),10,7)
		Game.attackers.insert(0,z)
	# 鸟
	elif n > 6:
		z = Attacker(1255,y,82,90,birdM,10,12,len(birdM),len(birdA),8,4)
		Game.attackers.insert(0, z)
	# 蓝龙
	elif n > 4:
		z = Attacker(1255, y, 110, 95, blueM, 2, 10, len(blueM), len(blueA), 8, 10)
		Game.attackers.insert(0,z)
	# 猫
	elif n > 2:
		z = Attacker(1255,y,110,84,catM,3,25,len(catM),len(catA),5,3)
		Game.attackers.insert(0,z)
	# 貂
	elif n >= 0:
		z = Attacker(1241,y,82,99,martenM,1,20,len(martenM),len(martenA),5,6)
		Game.attackers.insert(0,z)

# 产生攻击者方法
def componentEnter():
	# 控制第一个攻击者，隔几秒再出现
	currTime = time.time()
	t = int(currTime - Game.startTime)
	if t < 3:
		return
	elif t == 3:
		firstWaring()
	#判断是否到了产生攻击者的时间
	if not isActionTime(Game.lastTime,Game.animalInterval):
		return
	Game.lastTime = time.time()
	n = random.randint(0,10)
	y_list = [80,170,270,360,450]
	i = random.randint(0,4)
	y = y_list[i]
	if t <= 25:
		createAttObject(n,y)
		if t>=22:
			Game.isPromptB = True
	else:
		if Game.animalNum != 0:
			Game.animalInterval = 1
			if Game.isBoss:
				z = Attacker(1295,270,193,244,boss1M,5,300,len(boss1M),len(boss1A),100,2)
				Game.attackers.append(z)
				Game.isBoss = False
			createAttObject(n,y)
			Game.animalNum -= 1
		elif Game.animalNum == 0:
			if len(Game.attackers) == 0:
				Game.state = 'WIN'


# 叉
def fork():
	global img_rect
	img_rect = Game.a_img.get_rect()
	img_rect.center = (610, 270)
	canvas.blit(Game.a_img, img_rect)
	if not isActionTime(Game.pauseLastTime,0.03):
		return
	Game.pauseLastTime = time.time()
	Game.a_img = lifeR[Game.defense_i%14]
	Game.defense_i += 1

def layer_paint(isEnd=False):
	image = swtich_layer(isEnd)
	canvas.blit(image, (0, 0))

# 防御值提示
def defensePrompt():
	fill_text(str(Game.defense),(705,195),80,True)
	canvas.blit(continueGame,(500,350))
def componentPaint():
	for d in Game.defendors:
		d.paintPlace()
	# 保证血条绘制在植物的上方
	for d in Game.defendors:
		if d.isShowBlood:
			d.paintBlood()
	for attacker in Game.attackers:
		attacker.paint()
	for d in Game.dies:
		d.paint()
	for b in Game.bullets:
		b.paint()
	fill_text(str(Game.t),(1162,22),40,False)
	# 卡槽
	canvas.blit(slot1,(384,494))
	if type(Game.energy) != int:
		Game.energy = round(Game.energy,2)
	fill_text(Game.energy, (442, 583), 25,False)
	# 卡片的绘制
	for c in Game.card_list:
		c.paint()
	showDefense()
	for e in Game.energy_list:
		e.paint()
	if Game.f1 and Game.state == 'RUNNING':
		try:
			Game.cards[-1].paintMove()
		except:
			pass
	canvas.blit(xuanfu,(135,460))
	canvas.blit(xuanfu,(905,460))
	#  判断能量够不够
	if Game.isPrompt:
		canvas.blit(prompt,(50,Game.promptY))
	# 判断是否提示boss出现
	if Game.isPromptB and Game.state == 'RUNNING' or Game.state == 'SUSPEND':
		canvas.blit(bossPrompt,(870,Game.promptBY))

def componentStep():
	for d in Game.defendors:
		d.animation()
	for attacker in Game.attackers:
		attacker.animation()
		if attacker.type == 5 and attacker.x < 1150 and Game.isAttack:
			bossAttack(attacker)
			Game.isAttack = False
		if attacker.x < 177:
			if Game.defense <= 20:
				Game.state = 'LOSE'
			else:
				Game.state = 'PAUSE'
				Game.attackers.remove(attacker)
	for d in Game.dies:
		d.animation()
	for b in Game.bullets:
		b.step()
		if b.id == 's2':
			b.animation()
		if b.x>1200 or b.y>440 and b.id == 's2':
			Game.bullets.remove(b)
	for e in Game.energy_list:
		e.animation()
		e.move()
	#  判断能量够不够
	if Game.isPrompt:
		if Game.num>200:
			Game.isPrompt =False
			Game.num = 0
			Game.promptY = 600
		Game.num += 1
		Game.promptY -= 5
		if Game.promptY < 400:
			Game.promptY = 400
	# 判断是否提示boss出现
	if Game.isPromptB and Game.state == 'RUNNING':
		if Game.Bnum>200:
			Game.promptBY += 4
			if Game.promptBY > 600:
				Game.promptBY = 600
				Game.isBoss = True
				Game.isPromptB  = False
				Game.Bnum = 0
		else:
			Game.Bnum += 1
			Game.promptBY -= 3
			if Game.promptBY < 360:
				Game.promptBY = 360
def state_check():
	for a in Game.attackers:
		for d in Game.defendors:
			# 如果守卫和攻击没有碰撞 并且 守卫不是炸弹
			if d.hit(a) != True and d.name!='bomb' and a.isbomb!=True and a.state!='head':
				a.state = 'move'
				img_list = switch_move(a.type)
				a.img_list = img_list

# 控制游戏状态
def controlState():
	if Game.state == 'RUNNING':
		if Game.isBgmMusic:
			bgm.play(-1)
			Game.isBgmMusic =False
		showDefense()
		timeJudge()
		componentEnter()
		componentPaint()
		componentStep()
		for d in Game.defendors:
			if d.name=='shooter':
				d.shoot1()
			elif d.img_list == masterA:
				d.shoot2()
			elif d.img_list == guardA:
				d.showShield()
		state_check()
		checkHit()
	elif Game.state == 'PAUSE':
		if Game.isPauseMusic:
			if Game.is_ori_first:
				Game.ori_defense = Game.defense
				Game.is_ori_first = False
			defenseReduceM.play()
			Game.defense -= 20
			if Game.defense >= Game.ori_defense*0.8:
				Game.d_i = 1
			elif Game.defense >= Game.ori_defense*0.6:
				Game.d_i = 2
			elif Game.defense >= Game.ori_defense*0.4:
				Game.d_i = 3
			elif Game.defense >= Game.ori_defense*0.2:
				Game.d_i = 4
			Game.isPauseMusic = False
		componentPaint()
		if Game.defense_i <= 13:
			fork()
		else:
			layer_paint(True)
			defensePrompt()
	elif Game.state == 'LOSE':
		rePaint()
		if Game.isLoseMusic:
			bgm.stop()
			loseMusic.play()
			Game.isLoseMusic = False
		image = swtich_layer()
		end('lose',image)
		canvas.blit(restartimg, (560, 330))
	elif Game.state == 'WIN':
		rePaint()
		showDefense()
		if Game.isWinMusic:
			bgm.stop()
			winMusic.play()
			Game.isWinMusic = False
		image = swtich_layer()
		end('win',image)
	elif Game.state == 'SUSPEND':
		componentPaint()
		canvas.blit(suspend,(30,10))

def save_data():
	Game.user_row = Game.row
	Game.user_shootInterval = Game.shootInterval
	Game.user_energy = Game.energy
	Game.user_interval = Game.animalInterval
	Game.user_defense = Game.defense
	Game.endNum2 = Game.animalNum

def spaceEvent():
	if Game.state == 'RUNNING':
		Game.state = 'SUSPEND'
		pygame.mixer.pause()
	elif Game.state == 'SUSPEND':
		Game.state = 'RUNNING'
		Game.startTime = Game.startTime + int((time.time() - Game.startTime) - Game.t)
		pygame.mixer.unpause()

# 射手 shooter
def shooter(life=8):
	card1 = Card('shooter', Game.card_x1, Game.card_x2, 517, 597, 73, 85, 10, life)
	Game.card_list.append(card1)
	add_card()
# 石头人 stone
def stone(life=8):
	card2 = Card('stone', Game.card_x1, Game.card_x2, 517, 597, 95, 87, 5, life)
	Game.card_list.append(card2)
	add_card()
# 炸弹 bomb
def bomb(life=8):
	card4 = Card('bomb', Game.card_x1, Game.card_x2, 517, 597, 74, 58, 15, life)
	Game.card_list.append(card4)
	add_card()
# 增益魔法 magic
def magic(life=8):
	card3 = Card('buff', Game.card_x1, Game.card_x2, 517, 597, 70, 79, 8, life)
	Game.card_list.append(card3)
	add_card()
# 战士 fighter
def fighter(life=8):
	card5 = Card('master', Game.card_x1, Game.card_x2, 517, 597, 57, 123, 20, life)
	Game.card_list.append(card5)
	add_card()
# 神鸟 bird
def bird(life=8):
	card6 = Card('guard',Game.card_x1, Game.card_x2, 517, 597, 100, 140, 10, life)
	Game.card_list.append(card6)
	add_card()

def add_card():
	if len(Game.card_list) <= 4:
		for i in range(len(Game.card_list)):
			Game.card_list[i].x1 = Game.pos_list[i][0]
			Game.card_list[i].x2 = Game.pos_list[i][1]
	else:
		Game.card_list.pop(-2)
		for i in range(len(Game.card_list)):
			Game.card_list[i].x1 = Game.pos_list[i][0]
			Game.card_list[i].x2 = Game.pos_list[i][1]








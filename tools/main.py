import sys,os
sys.path.insert(0, os.getcwd())
from tools.var import *
import tools.hero as hero

def start(bullet,attackInterval,energy,defense,animalInterval,animalNum):
    pygame.display.set_caption("保卫学院")
    def handleEvent():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if hero.isChooseCard(x, y) and Game.state == 'RUNNING':
                    hero.clickCard(pos)
                elif x >= 190 and x <= 1200 and y >= 43 and y <= 490 and Game.state == 'RUNNING':
                    hero.place_defendor(x, y)
                elif x > 500 and x < 680 and y > 350 and y < 420 and Game.state == 'PAUSE':
                    hero.switchRunning()
                elif x > 565 and x < 684 and y > 340 and y < 425 and Game.state == 'LOSE':
                    hero.restart()
            if event.type == pygame.MOUSEMOTION:
                if Game.defendor != None and Game.state == 'RUNNING' and Game.f1 and Game.f2:
                    pos = pygame.mouse.get_pos()
                    Game.defendor.x = pos[0] - Game.defendor.width / 2
                    Game.defendor.y = pos[1] - Game.defendor.height / 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hero.spaceEvent()

    Game.row = bullet
    Game.shootInterval = attackInterval
    Game.energy = energy
    Game.defense = defense
    Game.animalInterval = animalInterval
    Game.animalNum = animalNum
    hero.save_data()
    while True:
        canvas.blit(bg, (0, 0))
        hero.controlState()
        handleEvent()
        clock.tick(60)
        pygame.display.update()
        pygame.time.delay(15)
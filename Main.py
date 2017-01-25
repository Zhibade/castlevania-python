import pygame, sys
from pygame.locals import *

from Character.Belmont import Belmont
from Props.Candle import Candle
from Collision.Platform import PlatformBox
from Stage.Stage import Stage
from UI.UI import UI_Image
from UI.UI import UI_Text

pygame.init();
fpsLimit = pygame.time.Clock()
runTime = pygame.time.get_ticks()/1000

winWidth = 578
winHeight = 448

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Castlevania Gameplay')

bg = pygame.Color(0,0,0)

player = Belmont()
player.setPos(-10,244)

candle01 = Candle(84, 240)
candle02 = Candle(157, 261)
candle03 = Candle(243, 244)
candle04 = Candle(372, 196)
candle05 = Candle(502, 239)

candleGroup = [candle01, candle02, candle03, candle04, candle05]
itemGroup = []

currentStage = Stage(0, 80, 4)

platform01 = PlatformBox(68, 340, 511, 60)
platform02 = PlatformBox(0, 244, 68, 60)
platform03 = PlatformBox(522, 213, 56, 60)
platform04 = PlatformBox(137, 276, 56, 60)
platform05 = PlatformBox(392, 276, 56, 60)

platformGroup = [platform01, platform02, platform03, platform04, platform05]

score = 0

UI_fontSize = 16

UI_Top = UI_Image(0,0,'UI.png')
UI_Score = UI_Text(95, 12, "emulogic.ttf", "000000", UI_fontSize)
UI_Time = UI_Text(286, 12, "emulogic.ttf", "0000", UI_fontSize)
UI_HeartCount = UI_Text(367, 29, "emulogic.ttf", "ASD", UI_fontSize)
UI_LifeCount = UI_Text(367, 45, "emulogic.ttf", "05", UI_fontSize)

UI_TextGroup = [UI_Score, UI_Time, UI_HeartCount, UI_LifeCount]

while True:
    win.fill(bg)

    currentStage.update()
    runTime = pygame.time.get_ticks()/1000

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RIGHT:
                player.setKeyDown("right", True)
                if player.getJumpState() == False and player.getAttackState() == False:
                    player.setMove(True)
                    player.setSpeed(2,"x")
            elif event.key == K_LEFT:
                player.setKeyDown("left", True)
                if player.getJumpState() == False and player.getAttackState() == False:
                    player.setMove(True)
                    player.setSpeed(-2,"x")
            if event.key == K_z:
                player.initAttack()
            if event.key == K_DOWN:
                player.initCrouch()
            if event.key == K_SPACE:
                player.initJump()

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                player.setKeyDown("right", False)
                if player.getKeyState("left") == False:
                    player.setMove(False)

            elif event.key == K_LEFT:
                player.setKeyDown("left", False)
                if player.getKeyState("right") == False:
                    player.setMove(False)

            if event.key == K_DOWN:
                player.stopCrouch()

    fpsLimit.tick(30)

    player.update()

    for x in candleGroup:
        pos = x.getPos()
        rect = x.getRect()
        player.attackBox.getHit(pos[0], pos[1], rect[0], rect[1], x)
        x.update()

        if x.getState() == False:
            item = x.getSpawnedItem()
            iPos = item.getPos()
            iRect = item.getRect()
            player.passiveBox.getHit(iPos[0], iPos[1], iRect[0], iRect[1], item)

            if item.getState() == False and item.getPickedUpState() == False:
                item.pickUp()
                player.addHeartToCount(item.getHeartValue())

            for y in platformGroup:
                jPos = y.getPos()
                jRect = y.getRect()
                if iPos[0] > jPos[0] and iPos[0] < (jPos[0] + jRect[0]):
                    item.setFloor(jPos[1] + jRect[1] - iRect[1])

    for x in platformGroup:
        pos = player.passiveBox.getPos()
        bottom = x.getHit(pos[0], pos[1], 40, 59)
        x.update()

        if x.getCollision():
            pPos = player.getPos()
            if pPos[1] <= bottom:
                player.setFloor(bottom)
                player.addCollision(x)



    UI_Top.update()

    if player.getHeartCount() < 10:
        UI_HeartCount.setText("0" + str(player.getHeartCount()))
    else:
        UI_HeartCount.setText(str(player.getHeartCount()))

    UI_Time.setText("0" + str(999 - runTime))

    score = player.getHeartCount() * 75
    if score < 10:
        UI_Score.setText("00000" + str(score))
    elif score > 10 and score < 100:
        UI_Score.setText("0000" + str(score))
    elif score > 100 and score < 1000:
        UI_Score.setText("000" + str(score))
    elif score > 1000:
        UI_Score.setText("00" + str(score))

    for x in UI_TextGroup:
        x.update()

    pygame.display.update()

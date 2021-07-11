import pygame
import random

# Init
pygame.init()

# create screen
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (2100, 1400))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))

# Player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerXChange = 0


# Enemies
enemyImage = []
enemyXChangeConst = 0.1
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
numEnemies = 6


def enemies(numE, enemyImage, enemyX, enemyY, enemyXChange, enemyYChange):
    for i in range(numE):
        enemyImage.append(pygame.image.load("alien.png"))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyXChange.append(enemyXChangeConst)
        enemyYChange.append(40)


enemies(numEnemies, enemyImage, enemyX, enemyY, enemyXChange, enemyYChange)

# Bullet
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletYChange = 0.5
bulletFire = False

# Score
scoreValue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over
overFont = pygame.font.Font("freesansbold.ttf", 64)
resetFont = pygame.font.Font("freesansbold.ttf", 32)
scoreTitleFont = pygame.font.Font("freesansbold.ttf", 48)
scoreFont = pygame.font.Font("freesansbold.ttf", 25)
highScoreChecked = False
scoreList = []

# Sound
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
bulletSound = pygame.mixer.Sound("laser.wav")
enemySound = pygame.mixer.Sound("explosion.wav")
enemySound.set_volume(0.5)


def score(x, y):
    pyScore = font.render(f"Score: {scoreValue}", True, (255, 255, 255))
    screen.blit(pyScore, (x, y))


def gameOverText():
    global scoreList
    overText = overFont.render("GAME OVER", True, (255, 0, 0))
    resetText = resetFont.render("Press [R] to restart", True, (255, 255, 255))
    scoreTitle = scoreTitleFont.render("High Scores", True, (255, 255, 255))
    score1 = scoreFont.render(f"1: {scoreList[0]}", True, (255, 255, 255))
    score2 = scoreFont.render(f"2: {scoreList[1]}", True, (255, 255, 255))
    score3 = scoreFont.render(f"3: {scoreList[2]}", True, (255, 255, 255))
    score4 = scoreFont.render(f"4: {scoreList[3]}", True, (255, 255, 255))
    score5 = scoreFont.render(f"5: {scoreList[4]}", True, (255, 255, 255))
    score6 = scoreFont.render(f"6: {scoreList[5]}", True, (255, 255, 255))
    score7 = scoreFont.render(f"7: {scoreList[6]}", True, (255, 255, 255))
    score8 = scoreFont.render(f"8: {scoreList[7]}", True, (255, 255, 255))
    score9 = scoreFont.render(f"9: {scoreList[8]}", True, (255, 255, 255))
    score10 = scoreFont.render(f"10: {scoreList[9]}", True, (255, 255, 255))
    screen.blit(overText, (200, 50))
    screen.blit(resetText, (250, 150))
    screen.blit(scoreTitle, (255, 200))
    screen.blit(score1, (260, 270))
    screen.blit(score2, (260, 310))
    screen.blit(score3, (260, 350))
    screen.blit(score4, (260, 390))
    screen.blit(score5, (260, 430))
    screen.blit(score6, (460, 270))
    screen.blit(score7, (460, 310))
    screen.blit(score8, (460, 350))
    screen.blit(score9, (460, 390))
    screen.blit(score10, (460, 430))


def highScore(score):
    global highScoreChecked
    global scoreList
    if not highScoreChecked:
        with open("highScores.txt", "r+") as f:
            scoreStr = f.read()
            scoreList = list(scoreStr.split(","))
            scoreList = [int(e) for e in scoreList]
            scoreList.append(score)
            scoreList.sort(reverse=True)
            scoreList.pop()
            scoreStr = ",".join(str(e) for e in scoreList)
            f.seek(0)
            f.write(scoreStr)
            f.truncate()
            highScoreChecked = True


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))


def enemySpawn(i):
    global enemyX
    global enemyY
    enemyX[i] = random.randint(0, 735)
    enemyY[i] = random.randint(50, 150)


def bullet(x, y):
    global bulletFire
    bulletFire = True
    screen.blit(bulletImage, (x + 16, y + 10))


def bulletReset():
    global bulletFire
    global bulletY
    bulletY = 480
    bulletFire = False


def isCollision(x1, x2, y1, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return (True if distance < 27 else False)
    # return ((False, True)[distance])


# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Keystrokes
    playerFormula = 0.3 + scoreValue/100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -(playerFormula)
            if event.key == pygame.K_RIGHT:
                playerXChange = playerFormula
            if event.key == pygame.K_SPACE:
                if not bulletFire:
                    bulletSound.play()
                    bulletX = playerX
                    bullet(bulletX, bulletY)
            if event.key == pygame.K_r:
                enemyImage = []
                enemyXChangeConst = 0.1
                enemyX = []
                enemyY = []
                enemyXChange = []
                enemyYChange = []
                numEnemies = 6
                enemies(numEnemies, enemyImage, enemyX, enemyY, enemyXChange,
                        enemyYChange)
                scoreValue = 0
                highScoreChecked = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0

    # Player movement
    playerX += playerXChange
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyFormula = enemyXChangeConst + scoreValue/100
    for i in range(numEnemies):
        if enemyY[i] > 440:
            for j in range(numEnemies):
                enemyY[j] = 2000
            highScore(scoreValue)
            gameOverText()
            break
        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = enemyFormula
            enemyY[i] += enemyYChange[i]
        if enemyX[i] >= 736:
            enemyXChange[i] = -(enemyFormula)
            enemyY[i] += enemyYChange[i]

        # Collision
        collision = isCollision(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision:
            enemySound.play()
            bulletReset()
            enemySpawn(i)
            scoreValue += 1
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletReset()
    if bulletFire:
        bullet(bulletX, bulletY)
        bulletY -= bulletYChange

    # Re-draw entities
    player(playerX, playerY)
    score(textX, textY)
    pygame.display.update()

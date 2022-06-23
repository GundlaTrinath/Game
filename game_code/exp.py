import pygame, sys
from pygame import mixer

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.mixer.init()
height = 800
width = 1500
pygame.display.set_caption('findaway')
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
font = pygame.font.Font('freesansbold.ttf', 32)

w = 945
x = 545
vel = 1
cn='0'
start = True
left = False
right = False
up = False
down = False

mixer.music.load("Monkeys-Spinning-Monkeys.wav")
mixer.music.play(-1)

background=pygame.image.load('bgd1.png')
background=pygame.transform.scale(background,(width,height))
img_d = pygame.image.load('car1.png')
img_u = pygame.image.load('car2.png')
img_r = pygame.image.load('car3.png')
img_l = pygame.image.load('car4.png')
img_h = pygame.image.load('home.png')
hint=pygame.image.load('idea.png')
coin1=pygame.image.load('coin.png')
coin=pygame.transform.scale(coin1,(20,20))
# winner=pygame.image.load('winner.png')

coinsound=pygame.mixer.Sound('mixkit-game-success-alert-2039.wav')

textx = 700
texty = 50
text=open("data.txt","r")
with open("data.txt","r") as f:
    text_r=f.read()
level_s=int(text_r)
list1=[[635,130],[835,380],[835,200]]

def level_switch(n):
    global level_s
    if n==1:
        level1()
    elif n==2:
        level2()
    elif n==3:
        level3()
    elif n==4:
        level4()
    elif n==5:
        level5()

def result(x, y):
    score = font.render("WINNER", True, (255, 0, 0))
    screen.blit(score, (x, y))

def fail(x, y):
    score = font.render("FAIL", True, (0,5,250))
    screen.blit(score, (x, y))

def result1(x, y):
    score = font.render("WINNER", True, (0,5,250))
    screen.blit(score, (x, y))

def fail1(x, y):
    score = font.render("FAIL", True, (255, 0, 0))
    screen.blit(score, (x, y))

def title(x, y):
    title = font.render("FINDAWAY", True, (255, 255, 0))
    screen.blit(title, (x, y))


def levels(x, y):
    sqr = pygame.draw.circle(screen, (255, 0, 225), (x, y), 30)

def level_l(x,y):
    sqr=pygame.draw.circle(screen,(255,225,225),(x,y),33)

def level_n(x, y, no):
    num = font.render(no, True, (255, 255, 255))
    screen.blit(num, (x, y))

def rec(x,y):
    pygame.draw.rect(screen,(255,255,255),(x,y,206,56))
def mus(x,y):
    pygame.draw.rect(screen, (0, 200, 0), (x,y,100,50))

def data(n):
    text = open("data.txt", "w")
    text.write(n)
    text.close()

click = False

def main_menu():
    a,b=647,397
    c,d=650,610
    global cn
    while True:
        global click
        screen.blit(background,(0,0))
        # screen.fill((0, 0, 0))
        title(670, 100)
        level_n(690,200,"LEVELS")
        global level_s
        if level_s==1:
            level_l(550,300)
        if level_s==2:
            level_l(650,300)
        if level_s==3:
            level_l(750,300)
        if level_s==4:
            level_l(850,300)
        if level_s==5:
            level_l(950,300)
        levels(850, 300)
        levels(750, 300)
        levels(650, 300)
        levels(550, 300)
        levels(950, 300)

        level_n(540, 285, "1")
        level_n(640, 285, "2")
        level_n(740, 285, "3")
        level_n(840, 285, "4")
        level_n(940, 285, "5")
        global mx, my
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(650, 400, 200, 50)
        button_2 = pygame.Rect(650, 470, 200, 50)
        button_3 = pygame.Rect(650, 540, 200, 50)
        music1=pygame.Rect(650,610,100,50)
        music2=pygame.Rect(750,610,100,50)

        screen.blit(coin,(50,50))
        screen.blit(coin,(50,60))
        screen.blit(coin,(60,55))
        coinscore=font.render(cn,True,(255,255,255))
        screen.blit(coinscore,(100,50))

        rec(a,b)
        pygame.draw.rect(screen, (0, 255, 0), button_1)
        pygame.draw.rect(screen, (0, 255, 0), button_2)
        pygame.draw.rect(screen, (0, 255, 0), button_3)
        pygame.draw.rect(screen, (0, 255, 0), music1)
        pygame.draw.rect(screen, (0, 255, 0), music2)
        if a==647 and b==607:
            mus(c,d)
        if level_s==1:
            level_n(700, 410, "START")
        if level_s>1:
            level_n(680, 410, "RESUME")
        level_n(675, 480, "RESTART")
        level_n(710, 550, "EXIT")
        level_n(670,620,"ON")
        level_n(770,620,"OFF")
        level_n(520,620,"MUSIC")

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            userInput = pygame.key.get_pressed()
            if userInput[pygame.K_UP]:
                if b>397:
                    b-=70
            if userInput[pygame.K_DOWN]:
                if b<607:
                    b+=70
            if userInput[pygame.K_LEFT]:
                if c==750 and b==607: #off
                    c-=100
            if userInput[pygame.K_RIGHT]:
                if c==650 and b==607: #on
                    c+=100
            if userInput[pygame.K_RETURN]:
                if b==397:
                    level_switch(level_s)
                if b==467:
                    data("1")
                    level_s=1
                    cn='0'
                if b==537:
                    sys.exit()
                if c == 750 and b == 607:
                    mixer.music.pause()
                if c == 650 and b == 607:
                    mixer.music.unpause()


            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def level1():
    w = 945
    x = 545
    vel = 1
    start = True
    left = False
    right = False
    up = False
    down = False
    gameOn = True
    while gameOn:
        click = False
        screen.fill('gray')
        rec(1200,50)
        pygame.draw.rect(screen,'green',(1203, 53, 200, 50))
        level_n(1225, 63, "HOME (h)")
        pygame.draw.rect(screen, 'black', (510, 110, 490, 490), 6, 5)
        pygame.draw.line(screen, 'black', [935, 110], [935, 535], 5)
        pygame.draw.line(screen, 'black', [875, 110], [875, 535], 5)
        pygame.draw.line(screen, 'black', [815, 110], [815, 535], 5)
        pygame.draw.line(screen, 'black', [755, 110], [755, 535], 5)
        pygame.draw.line(screen, 'black', [695, 110], [695, 535], 5)
        pygame.draw.line(screen, 'black', [635, 110], [635, 535], 5)
        pygame.draw.line(screen, 'black', [575, 110], [575, 535], 5)

        pygame.draw.line(screen, 'black', [510, 535], [877, 535], 5)
        pygame.draw.line(screen, 'black', [510, 475], [877, 475], 5)
        pygame.draw.line(screen, 'black', [510, 415], [935, 415], 5)
        pygame.draw.line(screen, 'black', [510, 355], [935, 355], 5)
        pygame.draw.line(screen, 'black', [510, 295], [877, 295], 5)
        pygame.draw.line(screen, 'black', [510, 235], [993, 235], 5)
        pygame.draw.line(screen, 'black', [510, 175], [935, 175], 5)

        pygame.draw.line(screen, 'gray', [578, 535], [632, 535], 5)
        pygame.draw.line(screen, 'gray', [578, 475], [632, 475], 5)
        pygame.draw.line(screen, 'gray', [875, 418], [875, 472], 5)
        pygame.draw.line(screen, 'gray', [815, 418], [815, 472], 5)
        pygame.draw.line(screen, 'gray', [575, 418], [575, 472], 5)
        pygame.draw.line(screen, 'gray', [516, 415], [572, 415], 5)
        pygame.draw.line(screen, 'gray', [516, 355], [572, 355], 5)
        pygame.draw.line(screen, 'gray', [935, 298], [935, 352], 5)
        pygame.draw.line(screen, 'gray', [875, 238], [875, 292], 5)
        pygame.draw.line(screen, 'gray', [815, 238], [815, 292], 5)
        pygame.draw.line(screen, 'gray', [755, 238], [755, 292], 5)
        pygame.draw.line(screen, 'gray', [695, 238], [695, 292], 5)
        pygame.draw.line(screen, 'gray', [635, 238], [635, 292], 5)
        pygame.draw.line(screen, 'gray', [575, 178], [575, 232], 5)
        pygame.draw.line(screen, 'gray', [578, 235], [632, 235], 5)
        pygame.draw.line(screen, 'gray', [516, 175], [572, 175], 5)


        pygame.time.delay(2)
        if start:
            screen.blit(img_u, (w, x))
        if up:
            screen.blit(img_u, (w, x))
        if down:
            screen.blit(img_d, (w, x))
        if left:
            screen.blit(img_l, (w, x))
        if right:
            screen.blit(img_r, (w, x))

        screen.blit(img_h, (525, 125))
        level = font.render("Level - 1", True, (0, 5, 250))
        screen.blit(level, (100, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP]:
            if x >= 125 and (x != 247 or w == 585) and (x != 187 or w == 524) and (
                    x != 543 or w == 885 or w == 585 or w == 946 or w == 945) and (
                    x != 425 or w == 524 or w == 765 or w == 946 or w == 945) and (x != 304 or w == 945 or w == 885):
                x -= vel
                left = False
                right = False
                up = True
                down = False
                start = False

        if userInput[pygame.K_DOWN]:
            if x <= 545 and (x != 425 or w == 585 or w == 885 or w == 946 or w == 945) and (
                    x != 305 or w == 945 or w == 946 or w == 524) and (x != 247 or w == 885 or w == 946) and (
                    x != 187 or w == 585) and (x != 124):
                x += vel
                left = False
                right = False
                up = False
                down = True
                start = False

        if userInput[pygame.K_LEFT]:
            if w >= 525 and (w != 945 or x == 545 or x == 546 or x == 305) and (
                    w != 885 or x == 546 or x == 545 or x == 247 or x == 425) and (
                    w != 585 or x == 545 or x == 546 or x == 187 or x == 425) and (
                    w != 766 or x == 545 or x == 247 or x == 546):
                w -= vel
                left = True
                right = False
                up = False
                down = False
                start = False

        if userInput[pygame.K_RIGHT]:
            if w <= 945 and (w != 885 or x == 545 or x == 546 or x == 305) and (
                    w != 585 or x == 546 or x == 545 or x == 247) and (
                    w != 524 or x == 425 or x == 546 or x == 545 or x == 187):
                w += vel
                left = False
                right = True
                up = False
                down = False
                start = False

        if (w == 524 and x == 124):
            global level_s
            level_s=2
            result(textx, texty)
            result1(textx+3,texty+3)
            # screen.blit(winner,(120,0))
            data("2")
            rec(1200, 700)
            pygame.draw.rect(screen, 'green', (1203, 703, 200, 50))
            level_n(1230, 715, "NEXT(n) >")
            if userInput[pygame.K_n]:
                level2()

        if userInput[pygame.K_h]:
            main_menu()

        if userInput[pygame.MOUSEBUTTONDOWN]:
            if event.button == 1:
                click = True
        pygame.display.update()
    pygame.quit()

def level2():
    w = 946
    x = 545
    vel = 1
    start = True
    left = False
    right = False
    up = False
    down = False
    gameOn = True
    while gameOn:
        click = False
        screen.fill('gray')
        rec(1200, 50)
        pygame.draw.rect(screen, 'green', (1203, 53, 200, 50))
        level_n(1225, 63, "HOME (h)")
        pygame.draw.rect(screen, 'black', (510, 110, 490, 490), 6, 5)
        pygame.draw.line(screen, 'black', [935, 110], [935, 595], 5)
        pygame.draw.line(screen, 'black', [875, 110], [875, 595], 5)
        pygame.draw.line(screen, 'black', [815, 110], [815, 595], 5)
        pygame.draw.line(screen, 'black', [755, 110], [755, 595], 5)
        pygame.draw.line(screen, 'black', [695, 110], [695, 595], 5)
        pygame.draw.line(screen, 'black', [635, 110], [635, 595], 5)
        pygame.draw.line(screen, 'black', [575, 110], [575, 595], 5)

        pygame.draw.line(screen, 'black', [510, 535], [993, 535], 5)
        pygame.draw.line(screen, 'black', [510, 475], [993, 475], 5)
        pygame.draw.line(screen, 'black', [510, 415], [993, 415], 5)
        pygame.draw.line(screen, 'black', [510, 355], [993, 355], 5)
        pygame.draw.line(screen, 'black', [510, 295], [993, 295], 5)
        pygame.draw.line(screen, 'black', [510, 235], [993, 235], 5)
        pygame.draw.line(screen, 'black', [510, 175], [993, 175], 5)

        pygame.draw.line(screen, 'gray', [578, 475], [632, 475], 5)
        pygame.draw.line(screen, 'gray', [578, 415], [632, 415], 5)
        pygame.draw.line(screen, 'gray', [578, 355], [632, 355], 5)
        pygame.draw.line(screen, 'gray', [578, 295], [632, 295], 5)
        pygame.draw.line(screen, 'gray', [578, 235], [632, 235], 5)
        pygame.draw.line(screen, 'gray', [698, 235], [752, 235], 5)
        pygame.draw.line(screen, 'gray', [698, 295], [752, 295], 5)
        pygame.draw.line(screen, 'gray', [818, 295], [872, 295], 5)
        pygame.draw.line(screen, 'gray', [818, 235], [872, 235], 5)
        pygame.draw.line(screen, 'gray', [818, 415], [872, 415], 5)
        pygame.draw.line(screen, 'gray', [818, 475], [872, 475], 5)
        pygame.draw.line(screen, 'gray', [938, 535], [993, 535], 5)
        pygame.draw.line(screen, 'gray', [938, 295], [993, 295], 5)
        pygame.draw.line(screen, 'gray', [938, 235], [993, 235], 5)
        pygame.draw.line(screen, 'gray', [938, 175], [993, 175], 5)
        pygame.draw.line(screen, 'gray', [635, 532], [635, 478], 5)
        pygame.draw.line(screen, 'gray', [695, 532], [695, 478], 5)
        pygame.draw.line(screen, 'gray', [635, 232], [635, 178], 5)
        pygame.draw.line(screen, 'gray', [695, 232], [695, 178], 5)
        pygame.draw.line(screen, 'gray', [755, 532], [755, 478], 5)
        pygame.draw.line(screen, 'gray', [815, 532], [815, 478], 5)
        pygame.draw.line(screen, 'gray', [875, 532], [875, 478], 5)
        pygame.draw.line(screen, 'gray', [935, 532], [935, 478], 5)
        pygame.draw.line(screen, 'gray', [635, 116], [635, 172], 5)
        pygame.draw.line(screen, 'gray', [695, 116], [695, 172], 5)
        pygame.draw.line(screen, 'gray', [755, 116], [755, 172], 5)
        pygame.draw.line(screen, 'gray', [815, 116], [815, 172], 5)
        pygame.draw.line(screen, 'gray', [875, 116], [875, 172], 5)
        pygame.draw.line(screen, 'gray', [935, 116], [935, 172], 5)
        pygame.draw.line(screen, 'gray', [755, 352], [755, 298], 5)
        pygame.draw.line(screen, 'gray', [815, 352], [815, 298], 5)
        pygame.draw.line(screen, 'gray', [875, 352], [875, 298], 5)
        pygame.draw.line(screen, 'gray', [935, 352], [935, 298], 5)
        pygame.draw.line(screen, 'gray', [575, 172], [575, 116], 5)

        pygame.time.delay(2)
        if start:
            screen.blit(img_u, (w, x))
        if up:
            screen.blit(img_u, (w, x))
        if down:
            screen.blit(img_d, (w, x))
        if left:
            screen.blit(img_l, (w, x))
        if right:
            screen.blit(img_r, (w, x))

        screen.blit(img_h, (525, 125))
        level = font.render("Level - 2", True, (0, 5, 250))
        screen.blit(level, (100, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP]:
            if x >= 125 and (x != 487 or w == 585 or w == 830) and (x != 195 or w == 946) and (
                    x != 367 or w == 585) and (x != 311 or w == 585 or w == 713 or w == 830 or w == 946):
                x -= vel
                left = False
                right = False
                up = True
                down = False
                start = False

        if userInput[pygame.K_DOWN]:
            if x <= 545 and (x != 487 or w == 946) and (x != 311 or w == 585) and (x != 124 or w == 946) and (
                    x != 195 or w == 585 or w == 713 or w == 830 or w == 946) and (
                    x != 250 or w == 713 or w == 946 or w == 585 or w == 830):
                x += vel
                left = False
                right = False
                up = False
                down = True
                start = False

        if userInput[pygame.K_LEFT]:
            if w >= 525 and (w != 946 or x == 487 or x == 124 or x == 311) and (w != 585 or x == 124) and (
                    w != 713 or x == 487 or x == 195 or x == 124) and (w != 830 or x == 487 or x == 124 or x == 311):
                w -= vel
                left = True
                right = False
                up = False
                down = False
                start = False

        if userInput[pygame.K_RIGHT]:
            if w <= 945 and (w != 585 or x == 195 or x == 487 or x == 124) and (
                    w != 830 or x == 487 or x == 311 or x == 124) and (
                    w != 713 or x == 487 or x == 311 or x == 124) and (w != 524):
                w += vel
                left = False
                right = True
                up = False
                down = False
                start = False

        if (w == 524 and x == 124):
            global level_s
            level_s = 3
            result(textx, texty)
            result1(textx + 3, texty + 3)
            data("3")
            rec(1200, 700)
            pygame.draw.rect(screen, 'green', (1203, 703, 200, 50))
            level_n(1230, 715, "NEXT(n) >")
            if userInput[pygame.K_n]:
                level3()

        if userInput[pygame.K_h]:
            main_menu()

        if userInput[pygame.MOUSEBUTTONDOWN]:
            if event.button == 1:
                click = True
        pygame.display.update()
    pygame.quit()
def level3():
    global cn
    w = 946
    x = 545
    vel = 1
    i=0
    j=0
    k=1
    r=5
    start = True
    left = False
    right = False
    up = False
    down = False
    gameOn = True
    while gameOn:
        click = False
        screen.fill('gray')
        rec(1200, 50)
        pygame.draw.rect(screen, 'green', (1203, 53, 200, 50))
        level_n(1225, 63, "HOME (h)")
        pygame.draw.rect(screen, 'black', (510, 110, 490, 490), 6, 5)
        pygame.draw.line(screen, 'black', [935, 110], [935, 595], 5)
        pygame.draw.line(screen, 'black', [875, 110], [875, 595], 5)
        pygame.draw.line(screen, 'black', [815, 110], [815, 595], 5)
        pygame.draw.line(screen, 'black', [755, 110], [755, 595], 5)
        pygame.draw.line(screen, 'black', [695, 110], [695, 595], 5)
        pygame.draw.line(screen, 'black', [635, 110], [635, 595], 5)
        pygame.draw.line(screen, 'black', [575, 110], [575, 595], 5)

        pygame.draw.line(screen, 'black', [510, 535], [993, 535], 5)
        pygame.draw.line(screen, 'black', [510, 475], [993, 475], 5)
        pygame.draw.line(screen, 'black', [510, 415], [993, 415], 5)
        pygame.draw.line(screen, 'black', [510, 355], [993, 355], 5)
        pygame.draw.line(screen, 'black', [510, 295], [993, 295], 5)
        pygame.draw.line(screen, 'black', [510, 235], [993, 235], 5)
        pygame.draw.line(screen, 'black', [510, 175], [993, 175], 5)

        pygame.draw.line(screen, 'gray', [578, 475], [632, 475], 5)
        pygame.draw.line(screen, 'gray', [578, 415], [632, 415], 5)
        pygame.draw.line(screen, 'gray', [578, 355], [632, 355], 5)
        pygame.draw.line(screen, 'gray', [578, 295], [632, 295], 5)
        pygame.draw.line(screen, 'gray', [578, 235], [632, 235], 5)
        pygame.draw.line(screen, 'gray', [698, 235], [752, 235], 5)
        pygame.draw.line(screen, 'gray', [698, 295], [752, 295], 5)
        pygame.draw.line(screen, 'gray', [818, 295], [872, 295], 5)
        pygame.draw.line(screen, 'gray', [818, 235], [872, 235], 5)
        pygame.draw.line(screen, 'gray', [818, 415], [872, 415], 5)
        pygame.draw.line(screen, 'gray', [818, 475], [872, 475], 5)
        pygame.draw.line(screen, 'gray', [938, 535], [993, 535], 5)
        pygame.draw.line(screen, 'gray', [938, 295], [993, 295], 5)
        pygame.draw.line(screen, 'gray', [938, 235], [993, 235], 5)
        pygame.draw.line(screen, 'gray', [938, 175], [993, 175], 5)
        pygame.draw.line(screen, 'gray', [635, 532], [635, 478], 5)
        pygame.draw.line(screen, 'gray', [695, 532], [695, 478], 5)
        pygame.draw.line(screen, 'gray', [635, 232], [635, 178], 5)
        pygame.draw.line(screen, 'gray', [695, 232], [695, 178], 5)
        pygame.draw.line(screen, 'gray', [755, 532], [755, 478], 5)
        pygame.draw.line(screen, 'gray', [815, 532], [815, 478], 5)
        pygame.draw.line(screen, 'gray', [875, 532], [875, 478], 5)
        pygame.draw.line(screen, 'gray', [935, 532], [935, 478], 5)
        pygame.draw.line(screen, 'gray', [635, 116], [635, 172], 5)
        pygame.draw.line(screen, 'gray', [695, 116], [695, 172], 5)
        pygame.draw.line(screen, 'gray', [755, 116], [755, 172], 5)
        pygame.draw.line(screen, 'gray', [815, 116], [815, 172], 5)
        pygame.draw.line(screen, 'gray', [875, 116], [875, 172], 5)
        pygame.draw.line(screen, 'gray', [935, 116], [935, 172], 5)
        pygame.draw.line(screen, 'gray', [755, 352], [755, 298], 5)
        pygame.draw.line(screen, 'gray', [815, 352], [815, 298], 5)
        pygame.draw.line(screen, 'gray', [875, 352], [875, 298], 5)
        pygame.draw.line(screen, 'gray', [935, 352], [935, 298], 5)
        pygame.draw.line(screen, 'gray', [575, 172], [575, 116], 5)

        if (x==124 and w==635 and int(cn)==0):
            coinsound.play()
            i=1
            cn='1'
        if (x==367 and w==830 and int(cn)==1):
            coinsound.play()
            i=2
            cn='2'
        if (x==195 and w==830 and int(cn)==2):
            coinsound.play()
            r=0
            cn='3'

        if int(cn)!=3:
            screen.blit(coin,(list1[i][j],list1[i][k]))

        pygame.time.delay(2)
        if start:
            screen.blit(img_u, (w, x))
        if up:
            screen.blit(img_u, (w, x))
        if down:
            screen.blit(img_d, (w, x))
        if left:
            screen.blit(img_l, (w, x))
        if right:
            screen.blit(img_r, (w, x))

        screen.blit(img_h, (525, 125))
        level = font.render("Level - 3", True, (0, 5, 250))
        screen.blit(level, (100, 50))

        pygame.draw.rect(screen,'gold',(105,105,110,60))
        pygame.draw.rect(screen, 'white', (110, 110, 100, 50))

        screen.blit(coin,(120,120))
        screen.blit(coin,(120,130))
        screen.blit(coin,(130,125))
        coinscore=font.render(cn,True,(0,5,255))
        screen.blit(coinscore,(170,120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP]:
            if x >= 125 and (x != 487 or w == 585 or w==830) and(x!=195 or w==946) and (x!=367 or w==585) and (x!=311 or w==585 or w==713 or w==830 or w==946):
                x -= vel
                left = False
                right = False
                up = True
                down = False
                start = False

        if userInput[pygame.K_DOWN]:
            if x <= 545 and (x != 487 or w==946) and (x!=311 or w==585) and (x!=124 or w==946)and(x!=195 or w==585 or w==713 or w==830 or w==946) and (x!=250 or w==713 or w==946 or w==585 or w==830):
                x += vel
                left = False
                right = False
                up = False
                down = True
                start = False

        if userInput[pygame.K_LEFT]:
            if w >= 525 and (w != 946 or x==487 or x==124 or x==311) and (w!=585 or x==124) and (w!=713 or x==487 or x==195 or x==124) and (w!=830 or x==487 or x==124 or x==311):
                w -= vel
                left = True
                right = False
                up = False
                down = False
                start = False

        if userInput[pygame.K_RIGHT]:
            if w <= 945 and (w != 585 or x==195 or x==487 or x==124) and (w!=830 or x==487 or x==311 or x==124) and (w!=713 or x==487 or x==311 or x==124) and (w!=524):
                w += vel
                left = False
                right = True
                up = False
                down = False
                start = False

        if (w == 524 and x == 124 and int(cn) != 3):
            global level_s
            level_s = 3
            fail(textx, texty)
            fail1(textx + 3, texty + 3)
            data("3")
            cn='0'
            level_n(600,715,"Collect all coins.")
            rec(1200, 700)
            pygame.draw.rect(screen, 'green', (1203, 703, 200, 50))
            level_n(1215, 715, "RESTART(r)")
            if userInput[pygame.K_r]:
                level3()

        if (w == 524 and x == 124 and int(cn) == 3):

            level_s = 4
            result(textx, texty)
            result1(textx + 3, texty + 3)
            data("4")
            rec(1200, 700)
            pygame.draw.rect(screen, 'green', (1203, 703, 200, 50))
            level_n(1230, 715, "NEXT(n) >")
            if userInput[pygame.K_n]:
                level4()

        if userInput[pygame.K_h]:
            main_menu()

        if userInput[pygame.MOUSEBUTTONDOWN]:
            if event.button == 1:
                click = True
        pygame.display.update()
    pygame.quit()
def level4():
    pass
def level5():
    pass

main_menu()

import pygame
pygame.init()
pygame.mixer.init()
height=800
width=1500
pygame.display.set_caption('Game')
screen=pygame.display.set_mode((width,height),pygame.RESIZABLE)


w=945
x=545
vel=1
start=True
left=False
right=False
up=False
down=False
font=pygame.font.Font('freesansbold.ttf',32)

img_d=pygame.image.load('car1.png')
img_u=pygame.image.load('car2.png')
img_r=pygame.image.load('car3.png')
img_l=pygame.image.load('car4.png')
img_h=pygame.image.load('home.png')
textx=700
texty=50

def result(x,y):
    score=font.render("WINNER",True,(255,0,0))
    screen.blit(score,(x,y))



gameOn=True
while gameOn:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOn=False

    userInput=pygame.key.get_pressed()
    if userInput[pygame.K_UP]:
        if x>=125 and (x!=247 or w==585) and (x!=187 or w==524) and (x!=543 or w==885 or w==585 or w==946 or w==945) and (x!=425 or w==524 or w==765 or w==946 or w==945) and (x!=304 or w==945 or w==885):
            x-=vel
            left=False
            right=False
            up=True
            down=False
            start=False


    if userInput[pygame.K_DOWN]:
        if x<=545 and (x!=425 or w==585 or w==885 or w==946 or w==945) and(x!=305 or w==945 or w==946 or w==524) and (x!=247 or w==885) and (x!=187 or w==585):
            x+=vel
            left=False
            right=False
            up=False
            down=True
            start=False

    if userInput[pygame.K_LEFT]:
        if w>=525 and (w!=945 or x==545 or x==546 or x==305) and (w!=885 or x==546 or x==545 or x==247 or x==425) and (w!=585 or x==545 or x==546 or x==187 or x==425) and (w!=766 or x==545 or x==247 or x==546):
            w-=vel
            left=True
            right=False
            up=False
            down=False
            start = False

    if userInput[pygame.K_RIGHT]:
        if w<=945 and (w!=885 or x==545 or x==546 or x==305) and (w!=585 or x==546 or x==545 or x==247) and (w!=524 or x==425 or x==546 or x==545 or x==187):
            w+=vel
            left=False
            right=True
            up=False
            down=False
            start = False


    screen.fill('gray')
    pygame.draw.rect(screen,'black',(510,110,490,490),6,5)
    pygame.draw.line(screen,'black',[935,110],[935,535],5)
    pygame.draw.line(screen,'black',[875,110],[875,535],5)
    pygame.draw.line(screen,'black',[815,110],[815,535],5)
    pygame.draw.line(screen,'black',[755,110],[755,535],5)
    pygame.draw.line(screen,'black',[695,110],[695,535],5)
    pygame.draw.line(screen,'black',[635,110],[635,535],5)
    pygame.draw.line(screen,'black',[575,110],[575,535],5)


    pygame.draw.line(screen,'black',[510,535],[877,535],5)
    pygame.draw.line(screen,'black',[510,475],[877,475],5)
    pygame.draw.line(screen,'black',[510,415],[935,415],5)
    pygame.draw.line(screen,'black',[510,355],[935,355],5)
    pygame.draw.line(screen,'black',[510,295],[877,295],5)
    pygame.draw.line(screen,'black',[510,235],[993,235],5)
    pygame.draw.line(screen,'black',[510,175],[935,175],5)


    pygame.draw.line(screen,'gray',[578,535],[632,535],5)
    pygame.draw.line(screen,'gray',[578,475],[632,475],5)
    pygame.draw.line(screen,'gray',[875,418],[875,472],5)
    pygame.draw.line(screen,'gray',[815,418],[815,472],5)
    pygame.draw.line(screen,'gray',[575,418],[575,472],5)
    pygame.draw.line(screen,'gray',[516,415],[572,415],5)
    pygame.draw.line(screen,'gray',[516,355],[572,355],5)
    pygame.draw.line(screen,'gray',[935,298],[935,352],5)
    pygame.draw.line(screen,'gray',[875,238],[875,292],5)
    pygame.draw.line(screen,'gray',[815,238],[815,292],5)
    pygame.draw.line(screen,'gray',[755,238],[755,292],5)
    pygame.draw.line(screen,'gray',[695,238],[695,292],5)
    pygame.draw.line(screen,'gray',[635,238],[635,292],5)
    pygame.draw.line(screen,'gray',[575,178],[575,232],5)
    pygame.draw.line(screen,'gray',[578,235],[632,235],5)
    pygame.draw.line(screen,'gray',[516,175],[572,175],5)

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
    screen.blit(img_h,(525,125))
    level=font.render("Level - 1",True,(0,5,250))
    screen.blit(level,(100,50))
    if(w==524 and x==124):
        result(textx,texty)
    pygame.display.update()

pygame.quit()

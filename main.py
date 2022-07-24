import sys
print(sys.path)
import pygame
import spritesheet
from Agent import Agent
from random import choice

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Music
#https://www.beepbox.co/player/#song=9n31s0k0l00e0ct2ma7g0fj07r1i0o432T1v0u61f0qwx10v311d08A5F2B6Q0530Pf636E2b677T1v3u30f0qwx10r511d08A9F4B0Q19e4Pb631E3b7626637T1v3ue1f0q0y10n73d4aA0F0B7Q0000Pe600E2bb619T2v3u02f10w4qw02d03w0E0b4h8QkCgy00014h8Ncx00000h4h4g0000004QcM01800p23yFE-47l0QRidltJdlBls3wliq_4GbYGXaIJUGEL8WieyiFFF8VeShFQyeWYzHHEFH8WaqUaDk8WV6i8V6EzEL8XyeYzVqyQzPsDeKOs-AFE-A7p0QRidltZdlBlt6UnMpvipt170Rgle81NZ1BO9714s42CLW6LgqZ1u0DjFEOiewzEE8W97gunQOAxq1rhq3tGaq2D8cKhVgI0kQyQCbkbikQyQyR2VN60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite test')
font = pygame.font.Font('monogram.ttf', 40)
sprite_sheet = spritesheet.SpriteSheet(pygame.image.load('./assets/meenymini_moods_big.png').convert_alpha())
bg = pygame.image.load("./assets/bg-day.png")
present = pygame.image.load("./assets/present.png")
present.convert()
BLACK = (0, 0, 0)
Ernie = Agent("Ernie")
Bert = Agent("Bert")
PRETRAINED = False

if(PRETRAINED):
    cur_action = Ernie.update()
    for i in range(100):
        op_cur_action = Bert.update(cur_action)
        cur_action = Ernie.update(op_cur_action)

Ernie.state = 2
Bert.state = 2

# Sounds
sfx = {
    "happy" : pygame.mixer.Sound("./assets/joy.wav"),
    "mad" : pygame.mixer.Sound("./assets/mad.wav"),
    "sad" : pygame.mixer.Sound("./assets/sad.wav"),
    "attack" : pygame.mixer.Sound("./assets/pow.wav")
}

moods = {
    2:0,
    3:1,
    1:2,
    0:3,
    4:4,
    5:5
}
states = ["mad", "sad", "neutral", "happy"]
gifts=["brocolli","conditioner","doll","USB drive","flowers","sharpie","bag","food","tissue box","lamp shade","cat","greeting card","sticky note","shoe lace","thermostat","photo album","sun glasses","purse","grid paper","box","bottle","glasses","white out","beef","playing card","deodorant","speakers","sketch pad","rubber band","chair","glow stick","candle","shirt","seat belt","keys","milk","bananas","rubber duck","rusty nail","outlet","tooth picks","button","wagon","shovel","sandal","shampoo","camera","window","toe ring","teddies","door","shoes","blouse","money","chapter book","mp3 player","magnet","ring","perfume","charger","rug","video games","house","bracelet","bed","credit card","nail file","car","sidewalk"]
insults = ["You are a doorknob.", "Your head looks like a naked mushroom","Your resolution is lower than my self-confidence","Your left foot is 1 pixel smaller than mine"]
compliments = ["You are a splendid ray of sunshine!","I am complimenting you right now!","Uh... wow?","You are so talented at existing!","You are awesome"]
run = True
next_action = "stare"
turn = 1
key_release = True
text = "Press space to see the interaction play out"
subtext = ""
ernie_speech = ""
bert_speech = ""
show_gift = False
while run:
    if turn:
        current_agent = Ernie
        other_agent = Bert
    else:
        current_agent = Bert
        other_agent = Ernie
    screen.blit(bg, (0, 0))
    screen.blit(sprite_sheet.get_image(moods[Bert.state],254,254,1, BLACK), (50, 254))
    #font.render_to(screen, (100, 500), "Bert", BLACK)
    screen.blit(font.render("Bert", False, BLACK), (100, 500))
    screen.blit(sprite_sheet.get_image(moods[Ernie.state],254,254,1, BLACK,mirrorx=True),(450, 254))
    #font.render_to(screen, (450, 500), "Ernie", BLACK)
    screen.blit(font.render("Ernie", False, BLACK), (450, 500))
    #font.render_to(screen, (80, 40), text, BLACK)
    screen.blit(font.render(text, False, BLACK), (80, 40))
    screen.blit(font.render(current_agent.id+" is now "+states[current_agent.state], False, BLACK), (80, 60))
    #font.render_to(screen, (80, 60), subtext, BLACK)
    screen.blit(font.render(subtext, False, BLACK), (80, 80))
    #font.render_to(screen, (20, 200), bert_speech, BLACK)
    screen.blit(font.render(bert_speech, False, BLACK), (20, 200))
    #font.render_to(screen, (80, 200), ernie_speech, BLACK)
    screen.blit(font.render(ernie_speech, False, BLACK), (80, 200))
    if(show_gift):
        screen.blit(present, (250, 80))
    pygame.display.update()
    screen.blit(bg, (0, 0))
    event = pygame.event.wait()
    if event.type == pygame.K_ESCAPE or event.type == pygame.QUIT:
        pygame.quit()
        run = False
        #sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and key_release:
            turn = (turn+1)%2
            key_release = False
            cur_action = current_agent.update(next_action)
            next_action = other_agent.update(cur_action)
            ernie_speech = ""
            bert_speech = ""
            subtext = ""
            show_gift = False
            if cur_action == "attack":
                text = current_agent.id + " attacks " + other_agent.id + "!"
                pygame.mixer.Sound.play(sfx["attack"])
                screen.blit(bg, (0, 0))
                if(other_agent.id == "Ernie"):
                    screen.blit(sprite_sheet.get_image(moods[4],254,254,1, BLACK,mirrorx=True), (450,254))
                    screen.blit(sprite_sheet.get_image(moods[5],254,254,1, BLACK), (50, 254))
                else:
                    screen.blit(sprite_sheet.get_image(moods[5],254,254,1, BLACK,mirrorx=True), (450,254))
                    screen.blit(sprite_sheet.get_image(moods[4],254,254,1, BLACK), (50, 254))
                pygame.display.update()
                pygame.time.wait(1000)
            elif cur_action == "gift":
                text = current_agent.id + " gifts " + "["+choice(gifts)+"] to " + other_agent.id
                if(other_agent.state == 0 or other_agent.state == 1):
                    subtext = other_agent.id + " didn't seem to like it..."
                elif(other_agent.state == 3):
                    subtext = other_agent.id + " loves it!"
                show_gift = True
            elif cur_action == "insult":
                text = current_agent.id + " insults " + other_agent.id + "!"
                if current_agent.id == "Ernie":
                    ernie_speech = choice(insults)
                else:
                    bert_speech = choice(insults)
                if other_agent.state == "neutral":
                    subtext = other_agent.id + " was not fazed!"
            elif cur_action == "compliment":
                text = current_agent.id + " compliments " + other_agent.id + "!"
                if current_agent.id == "Ernie":
                    ernie_speech = choice(compliments)
                else:
                    bert_speech = choice(compliments)
                if other_agent.state == "sad" or other_agent.state == "mad":
                    subtext = other_agent.id + " mistook it for an upsetting remark!"
            elif cur_action == "stare":
                text = current_agent.id + " awkwardly stares at " + other_agent.id + "!"
            if other_agent.state != 2:
                #print(other_agent.state)
                pygame.mixer.Sound.play(sfx[states[other_agent.state]])
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            key_release = True
    #event handler
    
    
    
pygame.quit()
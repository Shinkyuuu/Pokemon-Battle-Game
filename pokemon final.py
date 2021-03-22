import pygame
import time
import os
import random

# NAME THE GAME
pygame.display.set_caption("Pokemon")

# DETERMINE SCREEN RESOLUTION

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
resy = 1080 #int(input("How tall do you want the game? "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
resx = resy * (16/9)

# GAME RESOLUTION
gamex = int(resy * 256 / 384)
gamey = int(resy)

# POSITION OF GAME WINDOW
wx = 0
wy = 0
'''
wx = 1920 / 2 - (gamex / 2)
wy = 0
'''
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wx,wy)

# FULLSCREEN OR WINDOWED?
pip = input("Does win32api work? (y/n) ")
if pip == 'y':
    # If win32api Works
    from win32api import GetSystemMetrics
    if resy > GetSystemMetrics(1):
        win = pygame.display.set_mode((gamex, gamey))
    else:
        windowType = input("Windowed (a) or Fullscreen (b)? ")
        
        if windowType == 'a':
            win = pygame.display.set_mode((gamex, gamey))
        elif windowType == 'b':
            win = pygame.display.set_mode((gamex, gamey), pygame.FULLSCREEN)
        else:
            print("That makes me error")
else:          
    # If win32api doesnt work
    windowType = input("Windowed (a) or Fullscreen (b)? ")
        
    if windowType == 'a':
        win = pygame.display.set_mode((gamex, gamey))
    elif windowType == 'b':
        win = pygame.display.set_mode((gamex, gamey), pygame.FULLSCREEN)
    else:
        print("That makes me error")

    print('\n' * 2)
    print("Coolio")

    
#GAME START            
pygame.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) # MAKES CURSOR DISSAPEAR

# MISC. VARIABLES
variableBS = 0
pokeCounter = 0
walkCount = 0
walkCount2 = 0
holderx = False
holdery = False
holderx2 = True
holdery2 = True

# PLAYER/ENEMY STATS
playerHealth = 314
enemyHealth = 314
left1 = True
right1 = False
up1 = True
down1 = False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BATTLE MODE VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PLAYER DIMENSIONS (BATTLE MODE)
playerDimensionx = int((240 * gamey) / 1080)
playerDimensiony = int((240 * gamey) / 1080)

# POKEBALL DIMENSIONS (BATTLE MODE)
pokeballDimensionx = int((30 * gamey) / 1080)
pokeballDimensiony = int((30 * gamey) / 1080)

# POKEBALL POSITION (BATTLE MODE)
pokex = int((160 * gamex) / resx)
pokey = int((255 * gamey) / 1080)

# POKEMON DIMENSIONS (BATTLE MODE)
pokemonDimensionx = int((220 * gamey) / 1080)
pokemonDimensiony = int((220 * gamey) / 1080)

pokemonDimension2x = int((240 * gamey) / 1080)
pokemonDimension2y = int((240 * gamey) / 1080)

# POKEMON POSITION (BATTLE MODE)
pokemonx = int((90 * gamey) / 1080)
pokemony = int((200 * gamey) / 1080)

pokemon2xi = int(((-255 * gamey) - (pokemonDimension2x / 2)) / 1080)
pokemon2yi = int(((82 * gamey) - (pokemonDimension2y / 2)) / 1080)

pokemon2x = int((403 * gamey) / 1080)
pokemon2y = int((92 * gamey) / 1080)

# PLAYER POSITION (BATTLE MODE)
initialx = int((739 * gamey) / 1080)
initialy = int((166 * gamey) / 1080)
               
x = int((140 * gamex) / resx)
y = int((165 * gamey) / 1080)

# PLAYER VELOCITY (BATTLE MODE)
vel = int((30 * gamey) / 1080)

# BACKGROUND DIMENSIONS (BATTLE MODE)
bgDimensionx = int(gamex)
bgDimensiony = int((gamey / 2) - (gamey/ 2 * .25))

bglandDimension1x = int((428 * gamey) / 1080)
bglandDimension1y = int((61 * gamey) / 1080)

bglandDimension2x = int((355 * gamey) / 1080)
bglandDimension2y = int((91 * gamey) / 1080)

bgtransitionDimensionx = int((1296 * gamey) / 1080)
bgtransitionDimensiony = int((gamey / 2) - (gamey/ 2 * .25)) 

lowerDimensionx = int(gamex)
lowerDimensiony = int(gamey / 2) 
               
battleTextDimensionx = int(gamex)
battleTextDimensiony = int((gamey / 2) * .25)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~REGULAR VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PLAYER DEMENSIONS
spriteDimensionx = int((90 * gamey) / 1080)
spriteDimensiony = int((90 * gamey) / 1080)

# PLAYER POSITION
spritex = int(gamex / 2 - (spriteDimensionx / 2))
spritey = int(gamey / 4 - (spriteDimensiony / 2))

run = True
left = False
right = False
front = False
back = False

# PROFESSOR POSITION
spritex2 = int((585 * gamey) / 1080)
spritey2 = int((195 * gamey) / 1080)

left2 = False
right2 = False
front2 = False
back2 = False




# BACKGROUND DIMENSIONS
grandLakeHouseDimensionx = int(gamex * 1.1)
grandLakeHouseDimensiony = int((gamex * 1.1) * 166 / 276)

theLabDimensionx = int(gamex * 1.5)
theLabDimensiony = int((gamex * 1.5) * 166 / 377)

# BACKGROUND POSITIONS/ HIT BOXES

theLabx = ((75 * gamey) / 1080)
theLaby = ((-160 * gamey) / 1080)

thelabTopBox = (int((-100 * gamey) / 1080))
thelabBottomBox =(int((225 * gamey) / 1080))
thelabLeftBox = (int((60 * gamey) / 1080))
thelabRightBox =(int((1077 * gamey) / 1080))

thelabWallTopBox = (int((24 * gamey) / 1080))
thelabWallBottomBox = (int((80 * gamey) / 1080))
thelabWallLeftBox = (int((690 * gamey) / 1080))
thelabWallRightBox = (int((740 * gamey) / 1080))

machineBottomBox = (int((-75 * gamey) / 1080))
machineLeftBox = (int((490 * gamey) / 1080))
machineRightBox = (int((610 * gamey) / 1080))

benchBottomBox = (int((-75 * gamey) / 1080))
benchRightBox = (int((410 * gamey) / 1080))

deskTopBox = (int((200 * gamey) / 1080))
deskLeftBox = (int((350 * gamey) / 1080))
deskRightBox = (int((700 * gamey) / 1080))

bookShelfTopBox = (int((-40 * gamey) / 1080))
bookShelfBottomBox = (int((190 * gamey) / 1080))
bookShelfRightBox = (int((170 * gamey) / 1080))

bgland1xi = int((690 * gamey) / 1080)
bgland1yi = int((345 * gamey) / 1080)

bgland1x = int((0 * gamey) / 1080)
bgland1y = int((345 * gamey) / 1080)

bgland2xi = int((-327 * gamey) / 1080)
bgland2yi = int((202 * gamey) / 1080)

bgland2x = int((363 * gamey) / 1080)
bgland2y = int((202 * gamey) / 1080)

bgTransitionxi = 0
bgTransitionyi = 0



# BUTTON DIMENSIONS / POSITION
attackDimensionx = int((346 * gamey)/ 1080)
attackDimensiony = int((150 * gamey) / 1080)

attackx = int((8 * gamey) / 1080)
attacky = int((600 * gamey) / 1080)

bigButtonDimensionx = int((618 * gamey) / 1080)
bigButtonDimensiony = int((260 * gamey) / 1080)

bigx = int((50 * gamey) / 1080)
bigy = int((625 * gamey) / 1080)

mediumButtonDimensionx = int((340 * gamey) / 1080)
mediumButtonDimensiony = int((154 * gamey) / 1080)

mediumx = int((10 * gamey) / 1080)
mediumy = int((600 * gamey) / 1080)

hpDimensionx = int((350 * gamey) / 1080)
hpDimensiony = int((115 * gamey) / 1080)

hpx = 0
hpy = int((40 * gamey) / 1080)

hp2x = int((375 * gamey) / 1080)
hp2y = int((270 * gamey) / 1080)

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Frames/Images for each sprite/background
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

battleStart = [pygame.transform.scale(pygame.image.load('Assets/start0.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start1.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start2.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start3.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start4.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start5.png').convert_alpha(),
                (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start6.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start7.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start8.png').convert_alpha(), (playerDimensionx, playerDimensiony)), pygame.transform.scale(pygame.image.load('Assets/start9.png').convert_alpha(), (playerDimensionx, playerDimensiony))]

playerMoveLeft = [pygame.transform.scale(pygame.image.load('l0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/l1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/l2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/l3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
playerMoveRight = [pygame.transform.scale(pygame.image.load('Assets/r0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/r1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/r2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/r3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
playerMoveFront = [pygame.transform.scale(pygame.image.load('Assets/f0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/f1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/f2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('f3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
playerMoveBack = [pygame.transform.scale(pygame.image.load('Assets/b0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/b1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/b2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/b3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]


profMoveLeft = [pygame.transform.scale(pygame.image.load('Assets/cl0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cl1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cl2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/cl3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
profMoveRight = [pygame.transform.scale(pygame.image.load('Assets/cr0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cr1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cr2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/cr3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
profMoveFront = [pygame.transform.scale(pygame.image.load('Assets/cf0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cf1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cf2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/cf3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
profMoveBack = [pygame.transform.scale(pygame.image.load('Assets/cb0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cb1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('Assets/cb2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('Assets/cb3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]

bgrass = pygame.transform.scale(pygame.image.load('Assets/bgrass2.png').convert_alpha(), (bgDimensionx, bgDimensiony))
bgrassLand = pygame.transform.scale(pygame.image.load('Assets/bgrass2land.png').convert_alpha(), (bgDimensionx, bgDimensiony))
bgrassLand1 = pygame.transform.scale(pygame.image.load('Assets/bgrass2land1.png').convert_alpha(), (bglandDimension1x, bglandDimension1y))
bgrassLand2 = pygame.transform.scale(pygame.image.load('Assets/bgrass2land2.png').convert_alpha(), (bglandDimension2x, bglandDimension2y))
bgrassTransition = pygame.transform.scale(pygame.image.load('Assets/grasstransitions.png').convert_alpha(), (bgtransitionDimensionx, bgtransitionDimensiony))
lower = pygame.transform.scale(pygame.image.load('Assets/lower.png').convert_alpha(), (lowerDimensionx, lowerDimensiony))
pokeballSelection = pygame.transform.scale(pygame.image.load('pokemonSelection.png').convert_alpha(), (lowerDimensionx, lowerDimensiony))

battleText = pygame.transform.scale(pygame.image.load('Assets/battleText.png').convert_alpha(), (battleTextDimensionx, battleTextDimensiony))
battleMode = pygame.transform.scale(pygame.image.load('Assets/lowerbattlechoose.png').convert_alpha(), (lowerDimensionx, lowerDimensiony))
attackMode = pygame.transform.scale(pygame.image.load('Assets/lowerattackchoose.png').convert_alpha(), (lowerDimensionx, lowerDimensiony))
grassAttack = pygame.transform.scale(pygame.image.load('Assets/grassattack.png').convert_alpha(), (attackDimensionx, attackDimensiony))
waterAttack = pygame.transform.scale(pygame.image.load('Assets/waterattack.png').convert_alpha(), (attackDimensionx, attackDimensiony))
fireAttack = pygame.transform.scale(pygame.image.load('Assets/fireattack.png').convert_alpha(), (attackDimensionx, attackDimensiony))
bigSelect = pygame.transform.scale(pygame.image.load('Assets/bigselect.png').convert_alpha(), (bigButtonDimensionx, bigButtonDimensiony))
mediumSelect = pygame.transform.scale(pygame.image.load('mediumselect.png').convert_alpha(), (mediumButtonDimensionx, mediumButtonDimensiony))

playerHP = pygame.transform.scale(pygame.image.load('Assets/playerhp.png').convert_alpha(), (hpDimensionx, hpDimensiony))
enemyHP = pygame.transform.scale(pygame.image.load('Assets/enemyhp.png').convert_alpha(), (hpDimensionx, hpDimensiony))





grandLakeHouse = pygame.transform.scale(pygame.image.load('Assets/grandLakeHouse.png').convert_alpha(), (grandLakeHouseDimensionx, grandLakeHouseDimensiony))
theLab = pygame.transform.scale(pygame.image.load('Assets/theRealLab.png').convert_alpha(), (theLabDimensionx, theLabDimensiony))
theLabLights = pygame.transform.scale(pygame.image.load('Assets/theRealLabLighting.png').convert_alpha(), (theLabDimensionx, theLabDimensiony))
bookshelf1 = pygame.transform.scale(pygame.image.load('Assets/bookshelf1.png').convert_alpha(), (theLabDimensionx, theLabDimensiony))
bookshelf2 = pygame.transform.scale(pygame.image.load('Assets/bookshelf2.png').convert_alpha(), (theLabDimensionx, theLabDimensiony))
bookshelf3 = pygame.transform.scale(pygame.image.load('Assets/bookshelf3.png').convert_alpha(), (theLabDimensionx, theLabDimensiony))

piplupB = pygame.transform.scale(pygame.image.load('Assets/piplupB.png').convert_alpha(), (pokemonDimensionx, pokemonDimensiony))
chimcharB = pygame.transform.scale(pygame.image.load('Assets/chimcharB.png').convert_alpha(), (pokemonDimensionx, pokemonDimensiony))
turtwigB = pygame.transform.scale(pygame.image.load('Assets/turtwigB.png').convert_alpha(), (pokemonDimensionx, pokemonDimensiony))

piplupF = pygame.transform.scale(pygame.image.load('Assets/piplupF.png').convert_alpha(), (pokemonDimension2x, pokemonDimension2y))
chimcharF = pygame.transform.scale(pygame.image.load('Assets/chimcharF.png').convert_alpha(), (pokemonDimension2x, pokemonDimension2y))
turtwigF = pygame.transform.scale(pygame.image.load('Assets/turtwigF.png').convert_alpha(), (pokemonDimension2x, pokemonDimension2y))

pokemon = turtwigB

enemyPokemon = turtwigF



    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                    TIME DELAYS (SECONDS)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# PUT IN HOWEVER MUCH TIME YOU WANT TO DELAY THE SCREEN IN SECONDS (IT AUTO CONVERTS THE NUMBERS)

def delay (default = .1): # DELAYS FOR A SPECIFIC AMOUNT OF TIME AND UPDATES THE SCREEN (USE FOR ANIMATIONS)
    nextTime = (pygame.time.get_ticks() * gamey / 1080) + ((default * gamey / 1080) * 1000)
    while nextTime > (pygame.time.get_ticks() * gamey / 1080):
        pygame.event.get()
        pygame.display.update()
        pygame.time.get_ticks()
        

def superDelay (default2 = .025): # DELAYS FOR A SPECIFIC AMOUNT OF TIME (USE FOR SETTIGN THE FRAME RATE OR WHEN THERE IS NO MOVEMENT GOING ON)
    nextTime = (pygame.time.get_ticks() * gamey / 1080) + ((default2 * gamey / 1080) * 1000)
    while nextTime > (pygame.time.get_ticks() * gamey / 1080):
        pygame.event.get()
        
        pygame.time.get_ticks()
      
        
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                           MAKING TEXT APPEAR ONSCREEN
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def newText(string): # GENERIC TEXT THAT MAKES CHARACTERS APPEAR, REQUIRES THE PRESS OF THE SPACE BAR TO DISSAPEAR  (ONE AT A TIME)
    font = pygame.font.Font("PokemonDPPt.ttf", (int((51 * gamey) / 1080)))
    if (len(string)) > 62: # Max Character Length
        print("THAT WILL NOT WORK")
    delay(.5)
    textx = (int((50 * gamey) / 1080))
    texty = (int((425 * gamey) / 1080))
    maxWidth = (int((1581 * gamey) / 1080))
    holder1 = True
    text = ''
    text2 = ''
    text3 = ''
    
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25))) # Text Box
    length = int(len(string))
    if length > (maxWidth // (int((51 * gamey) / 1080))):# If the string will be more than 1 line long
        newLength = (maxWidth // (int((51 * gamey) / 1080)))
        newNewLength = length - (maxWidth // (int((51 * gamey) / 1080)))

    if length > (maxWidth // (int((51 * gamey) / 1080))): # If string is more than 1 line long
        for letterCount in range (0, newLength):# Line 1
            text += string[letterCount]
            textFace = font.render(text, True, (50, 50, 50))
            width, height = textFace.get_size()
           
            
            win.blit(textFace, (textx, texty)) # print letter
            pygame.display.update()
            delay(.02)
        
        for letterCount2 in range (newLength, len(string)):# Line 2
            text2 += string[letterCount2]
            textFace2 = font.render(text2, True, (50, 50, 50))
            width, heignt = textFace2.get_size()
    
            
            win.blit(textFace2, (textx, texty + (int((50 * gamey) / 1080)))) # print letter
            pygame.display.update()
            delay(.02)
    elif length <= (maxWidth // (int((51 * gamey) / 1080))): # If string is only 1 line
        for letterCount3 in range (len(string)):# Line 1
            text3 += string[letterCount3]
            textFace3 = font.render(text3, True, (50, 50, 50))
            width, height = textFace3.get_size()
    
            
            win.blit(textFace3, (textx, texty)) # print letter
            pygame.display.update()
            delay(.02)
    while holder1:
        pygame.event.get()
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            holder1 = False
    
 
            
def newAttackText(string): # THE SAME AS NEW TEXT, BUT DOESN'T REQUIRE THE SPACE BAR TO GO AWAY. (DISSAPEARS ON ITS OWN)  (ONE AT A TIME)
    font = pygame.font.Font("PokemonDPPt.ttf", (int((51 * gamey) / 1080)))
    if (len(string)) > 62: # Max Character Length
        print("THAT WILL NOT WORK")
    
    delay(.5)
    textx = (int((50 * gamey) / 1080))
    texty = (int((425 * gamey) / 1080))
    maxWidth = (int((1581 * gamey) / 1080))
    text = ''
    text2 = ''
    text3 = ''
    
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25))) # Text Box
    length = int(len(string))
    if length > (maxWidth // (int((51 * gamey) / 1080))):# If the string will be more than 1 line long
        newLength = (maxWidth // (int((51 * gamey) / 1080)))
        newNewLength = length - (maxWidth // (int((51 * gamey) / 1080)))

    if length > (maxWidth // 51): # If string is more than 1 line long
        for letterCount in range (0, newLength):# Line 1
            text += string[letterCount]
            textFace = font.render(text, True, (50, 50, 50))
            width, height = textFace.get_size()
           
            
            win.blit(textFace, (textx, texty)) # print letter
            pygame.display.update()
            delay(.02)
        
        for letterCount2 in range (newLength, len(string)):# Line 2
            text2 += string[letterCount2]
            textFace2 = font.render(text2, True, (50, 50, 50))
            width, heignt = textFace2.get_size()
    
            
            win.blit(textFace2, (textx, texty + (int((50 * gamey) / 1080)))) # print letter
            pygame.display.update()
            delay(.02)
    elif length <= (maxWidth // (int((51 * gamey) / 1080))): # If string is only 1 line
        for letterCount3 in range (len(string)):# Line 1
            text3 += string[letterCount3]
            textFace3 = font.render(text3, True, (50, 50, 50))
            width, height = textFace3.get_size()
    
            
            win.blit(textFace3, (textx, texty)) # print letter
            pygame.display.update()
            delay(.02)
            
def playerNameText(string): # TEXT FOR THE PLAYER'S POKEMON'S NAME (INSTANT)
    font = pygame.font.Font("PokemonDPPt.ttf", (int((46 * gamey) / 1080)))
    
 
    textx = int((445 * gamey) / 1080)
    texty = int((287 * gamey) / 1080)
    text = ''
    text += string[0: len(string)]
    textFace = font.render(text, True, (255, 255, 255))
    width, height = textFace.get_size()
   
       
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

def enemyNameText(string): # TEXT FOR THE ENEMY'S POKEMON'S NAME (INSTANT)
    font = pygame.font.Font("PokemonDPPt.ttf", (int((46 * gamey) / 1080)))
   
 
    textx = int((10 * gamey) / 1080)
    texty = int((70 * gamey) / 1080)
    text = ''
    text += string[0: len(string)]
    textFace = font.render(text, True, (255, 255, 255))
    width, height = textFace.get_size()
  
       
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

def attack1Text(string): # ATTACK TEXT FOR TOP LEFT BUTTON (INSTANT)
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
   
 
    textx = int((60 * gamey) / 1080)
    texty = int((638 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
     
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()
    
def attack2Text(string): # ATTACK TOP RIGHT (INSTANT)
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
 
    textx = int((420 * gamey) / 1080)
    texty = int((638 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
   
       
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()
    
def attack3Text(string): # ATTACK TEXT FOR BOTTOM LEFT BUTTON (INSTANT)
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))

    textx = int((60 * gamey) / 1080)
    texty = int((806 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
          
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()
    
def attack4Text(string): # ATTACK TEXT FOR BOTTOM RIGHT BUTTON (INSTANT)
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))

    textx = int((420 * gamey) / 1080)
    texty = int((806 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
    
       
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

def pp1Text(string): # ATTACK 1 POWER POINTS
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
    textx = int((225 * gamey) / 1080)
    texty = int((668 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
    
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

def pp2Text(string): # ATTACK 2 POWER POINTS
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
    textx = int((585 * gamey) / 1080)
    texty = int((668 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
    
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

def pp3Text(string): # ATTACK 3 POWER POINTS
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
    textx = int((225 * gamey) / 1080)
    texty = int((836 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
    
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()
    
def pp4Text(string): # ATTACK 4 POWER POINTS
    font = pygame.font.Font(("PokemonDPPt.ttf"), (int((46 * gamey) / 1080)))
    textx = int((585 * gamey) / 1080)
    texty = int((836 * gamey) / 1080)
    text = ''
    text += string
    textFace = font.render(text, True, (110, 100, 100))
    width, height = textFace.get_size()
    
    win.blit(textFace, (textx, texty)) # print string
    pygame.display.update()

    
            

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            ENEMY POKEMON MOVES AND STATS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def enemyPokemonStuff():

    global enemyHealth
    global attackDamage
    global enemyAttacks
    global enemyPokemonName
    global enemyPokemon
    randomEnemyPokemonList = [turtwigF, chimcharF, piplupF]
    enemyPokemon = random.choice(randomEnemyPokemonList)
    if enemyPokemon == turtwigF:
        enemyPokemonName = "TURTWIG"
        enemyHealth = 314
        enemyAttacks = [["Razor Leaf", 55], ["Tackle", 40], ["LeafStorm", 100], ["Bite", 60]]
    elif enemyPokemon == chimcharF:
        enemyPokemonName = "CHIMCHAR"
        enemyHealth = 314
        enemyAttacks = [["Scratch", 40], ["Flame Wheel", 60], ["Flamethrower", 90], ["Fury Swipes", 18]]
    elif enemyPokemon == piplupF:
        enemyPokemonName = "PIPLUP"
        enemyHealth = 314
        enemyAttacks = [["Bubble", 40], ["Fury Attack", 15], ["Whirlpool", 35], ["Hydro Pump", 110]]
    

  




def enemyAttackSequence():
    global enemyHealth
    global attackDamage
    global enemyAttacks
    global enemyPokemonName
    global playerHealth
    global pokemonx
    global pokemony
    global bgTransitionxi
    global bgTransitionyi
    global pokemon2xi
    global pokemon2yi
    global battleTextDimensionx
    global battleTextDimensiony
    enemyPokemonAttack = random.choice(enemyAttacks)
    enemyPokemonUsed = enemyPokemonAttack[0]
    enemyAttackDamage = enemyPokemonAttack[1]
    delay(1.5)
    newAttackText(enemyPokemonName+ " used "+ enemyPokemonUsed + "!")
    delay(.6)
    
    delay(.3)
    
    win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
    win.blit(bgrassLand, (0,0))
    win.blit(pokemon, (pokemonx, pokemony))
    win.blit(enemyPokemon, (pokemon2xi - 5, pokemon2yi - 10))
    pygame.draw.rect(win, (0, 0, 0), (0, int((540 * gamey / 1080) - (gamey / 2 * .25)), battleTextDimensionx, battleTextDimensiony))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    playerHealhBar()
    enemyHealhBar()
    pygame.display.update()
    delay(.2)
    win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
    win.blit(bgrassLand, (0,0))                
    win.blit(pokemon, (pokemonx, pokemony))
    win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
    pygame.draw.rect(win, (0, 0, 0), (0, int((540 * gamey / 1080) - (gamey / 2 * .25)), battleTextDimensionx, battleTextDimensiony))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    playerHealhBar()
    enemyHealhBar()
    pygame.display.update()
    
    for enemyDamageDone in range (0, enemyAttackDamage):
                    playerHealth -= 1
                    playerHealhBar()
                    delay(.01)


    
            
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            PLAYER POKEMON MOVES AND STATS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

playerHealth = 314
pp1 = 35
pp2 = 40
pp3 = 20
pp4 = 2

def turtwig():    
    global pokemonUsed1
    global pokemonUsed2
    global pokemonUsed3
    global pokemonUsed4
    global playerHealth
    global attackDamage1
    global attackDamage2
    global attackDamage3
    global attackDamage4
    global pokemonName
    pokemonName = "TURTWIG"
    
    pokemonUsed1 = "Razor Leaf"
    win.blit(grassAttack, (attackx, attacky))# TOP LEFT
    attackDamage1 = 55

    pokemonUsed2 = "Tackle"
    win.blit(grassAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    attackDamage2 = 40

    pokemonUsed3 = "Leaf Storm"
    win.blit(grassAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    attackDamage3 = 100

    pokemonUsed4 = "Bite"
    win.blit(grassAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attackDamage4 = 60

def piplup():    
    global pokemonUsed1
    global pokemonUsed2
    global pokemonUsed3
    global pokemonUsed4
    global playerHealth
    global attackDamage1
    global attackDamage2
    global attackDamage3
    global attackDamage4
    global pokemonName
    pokemonName = "PIPLUP"
    
    pokemonUsed1 = "Bubble"
    win.blit(waterAttack, (attackx, attacky))# TOP LEFT
    attackDamage1 = 40

    pokemonUsed2 = "Fury Attack"
    win.blit(waterAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    attackDamage2 = 15

    pokemonUsed3 = "Whirlpool"
    win.blit(waterAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    attackDamage3 = 35

    pokemonUsed4 = "Hydro Pump"
    win.blit(waterAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attackDamage4 = 110

def chimchar():    
    global pokemonUsed1
    global pokemonUsed2
    global pokemonUsed3
    global pokemonUsed4
    global playerHealth
    global attackDamage1
    global attackDamage2
    global attackDamage3
    global attackDamage4
    global pokemonName
    pokemonName = "CHIMCHAR"
    
    pokemonUsed1 = "Scratch"
    win.blit(fireAttack, (attackx, attacky))# TOP LEFT
    attackDamage1 = 40

    pokemonUsed2 = "Flame Wheel"
    win.blit(fireAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    attackDamage2 = 60

    pokemonUsed3 = "Flamethrower"
    win.blit(fireAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    attackDamage3 = 90

    pokemonUsed4 = "Fury Swipes"
    win.blit(fireAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attackDamage4 = 18


    
def pokemonStuff():
    if pokemon == turtwigB: # INITIAL FRAME
        turtwig()
    elif pokemon == piplupB:
        piplup()
    elif pokemon == chimcharB:
        chimchar()

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            PLAYER POKEMON ATTACK BUTTONS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def turtwigButtons():
    win.blit(grassAttack, (attackx, attacky))# TOP LEFT
    win.blit(grassAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(grassAttack, (attackx, int((765 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(grassAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
 
def piplupButtons(): 
    win.blit(waterAttack, (attackx, attacky))# TOP LEFT
    win.blit(waterAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(waterAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(waterAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    
def chimcharButtons(): 
    win.blit(fireAttack, (attackx, attacky))# TOP LEFT
    win.blit(fireAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(fireAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(fireAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
  
def pokemonButtonStuff():
    if pokemon == turtwigB: # WHICH POKEMON
        turtwigButtons()
    elif pokemon == piplupB:
        piplupButtons()
    elif pokemon == chimcharB:
        chimcharButtons()

            
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                   ANIMATION FOR PLAYER'S POKEMON ATTACKING
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def playerPokemonAttack():
    global pokemonx
    global pokemony
    global bgTransitionxi
    global bgTransitionyi
    global pokemon2xi
    global pokemon2yi
    global battleTextDimensionx
    global battleTextDimensiony
    delay(.3)
    
    win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
    win.blit(bgrassLand, (0,0))
    win.blit(pokemon, (pokemonx + 5, pokemony - 10))
    win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
    pygame.draw.rect(win, (0, 0, 0), (0, int((540 * gamey / 1080) - (gamey / 2 * .25)), battleTextDimensionx, battleTextDimensiony))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    playerHealhBar()
    enemyHealhBar()
    pygame.display.update()
    delay(.2)
    win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
    win.blit(bgrassLand, (0,0))                
    win.blit(pokemon, (pokemonx, pokemony))
    win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
    pygame.draw.rect(win, (0, 0, 0), (0, int((540 * gamey / 1080) - (gamey / 2 * .25)), battleTextDimensionx, battleTextDimensiony))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    playerHealhBar()
    enemyHealhBar()
    pygame.display.update()
     




'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                    HEALTH BARS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def enemyHealhBar():
    global enemyHealth
    global hpx
    global hpy
    
    win.blit(enemyHP, (hpx, hpy))
    enemyNameText(enemyPokemonName)
    if enemyHealth <= 0:
        pygame.display.update()
    else:
        pygame.draw.rect(win, ((255-(int(enemyHealth * (255 /314)))), int(enemyHealth * (255 /314)), 0), (int(137 * gamey / 1080), int(120 * gamey / 1080), int(enemyHealth * ((int((132 * gamey) / 1080)) /314)) , (int((5 * gamey) / 1080))))
    pygame.display.update()
    
def playerHealhBar():
    global playerHealth
    global hp2x
    global hp2y
    
    win.blit(playerHP, (hp2x, hp2y))
    playerNameText(pokemonName)
    if playerHealth <= 0:
        pygame.display.update()
    else:
        pygame.draw.rect(win, ((255-(int(playerHealth * (255 /314)))), int(playerHealth * (255 /314)), 0), (int(572 * gamey / 1080), int(336 * gamey / 1080), int(playerHealth * ((int((132 * gamey) / 1080)) /314)) , (int((6 * gamey) / 1080))))
    pygame.display.update()
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                    POKEMON ATTACKS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    
def choose():
    global playerHealth
    global enemyHealth
    global mediumx
    global mediumy
    global left1
    global right1
    global up1
    global down1
    global pp1
    global pp2
    global pp3
    global pp4
    
    win.blit(attackMode, (0, int((540 * gamey) / 1080)))
    pokemonStuff()# INITIAL FRAME
    
    playerHealhBar()
    enemyHealhBar()
    
    
    
    attack1Text(pokemonUsed1)
    attack2Text(pokemonUsed2)
    attack3Text(pokemonUsed3)
    attack4Text(pokemonUsed4)
    pp1Text(str(pp1))
    pp2Text(str(pp2))
    pp3Text(str(pp3))
    pp4Text(str(pp4))
    
    newAttackText("What will " + pokemonName+ " do?")
    
    while playerHealth > 0 and enemyHealth > 0: # WHILE BOTH POKEMON ARE STILL ALIVE
        
        pygame.event.get()
        superDelay()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# LEFT
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, mediumy))
                left1 = True
                up1 = True
                down1 = False
                right1 = False
                print("TOP LEFT")
                pygame.display.update()
            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, int((765 * gamey) / 1080)))
                left1 = True
                up1 = False
                down1 = True
                right1 = False
                print("BOTTOM LEFT")
                pygame.display.update()
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, int((765 * gamey) / 1080)))
                left1 = True
                up1 = False
                down1 = True
                right1 = False
                print("BOTTOM RIGHT")
                pygame.display.update()
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, mediumy))
                left1 = True
                up1 = True
                down1 = False
                right1 = False
                print("TOP RIGHT1")
                pygame.display.update()
            else:
               pygame.display.update()
            attack1Text(pokemonUsed1)
            attack2Text(pokemonUsed2)
            attack3Text(pokemonUsed3)
            attack4Text(pokemonUsed4)
            pp1Text(str(pp1))
            pp2Text(str(pp2))
            pp3Text(str(pp3))
            pp4Text(str(pp4))

        elif keys[pygame.K_RIGHT]:# RIGHT
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), mediumy))
                left1 = False
                up1 = True
                down1 = False
                right1 = True
                print("TOP LEFT")
                pygame.display.update()
            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), int((765 * gamey) / 1080)))
                left1 = False
                up1 = False
                down1 = True
                right1 = True
                print("BOTTOM LEFT")
                pygame.display.update()
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), int((765 * gamey) / 1080)))
                left1 = False
                up1 = False
                down1 = True
                right1 = True
                print("BOTTOM RIGHT")
                pygame.display.update()
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), mediumy))
                left1 = False
                up1 = True
                down1 = False
                right1 = True
                print("TOP RIGHT2")
                pygame.display.update()
            else:
               pygame.display.update()
            attack1Text(pokemonUsed1)
            attack2Text(pokemonUsed2)
            attack3Text(pokemonUsed3)
            attack4Text(pokemonUsed4)
            pp1Text(str(pp1))
            pp2Text(str(pp2))
            pp3Text(str(pp3))
            pp4Text(str(pp4))
   
        
        elif keys[pygame.K_UP]:# UP
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, mediumy))
                left1 = True
                up1 = True
                down1 = False
                right1 = False
                print("TOP LEFT")
                pygame.display.update()
            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, mediumy))
                left1 = True
                up1 = True
                down1 = False
                right1 = False
                print("BOTTOM LEFT")
                pygame.display.update()
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), mediumy))
                left1 = False
                up1 = True
                down1 = False
                right1 = True
                print("BOTTOM RIGHT")
                pygame.display.update()
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), mediumy))
                left1 = False
                up1 = True
                down1 = False
                right1 = True
                print("TOP RIGHT3")
                pygame.display.update()
            else:
               pygame.display.update()
            attack1Text(pokemonUsed1)
            attack2Text(pokemonUsed2)
            attack3Text(pokemonUsed3)
            attack4Text(pokemonUsed4)
            pp1Text(str(pp1))
            pp2Text(str(pp2))
            pp3Text(str(pp3))
            pp4Text(str(pp4))
  

            
        elif keys[pygame.K_DOWN]:# DOWN
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, int((765 * gamey) / 1080)))
                left1 = True
                up1 = False
                down1 = True
                right1 = False
                print("TOP LEFT")
                pygame.display.update()
            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (mediumx, int((765 * gamey) / 1080)))
                left1 = True
                up1 = False
                down1 = True
                right1 = False
                print("BOTTOM LEFT")
                pygame.display.update()
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), int((765 * gamey) / 1080)))
                left1 = False
                up1 = False
                down1 = True
                right1 = True
                print("BOTTOM RIGHT")
                pygame.display.update()
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                win.blit(attackMode, (0, int((540 * gamey) / 1080)))
                pokemonButtonStuff() # WHICH POKEMON
                win.blit(mediumSelect, (int((370 * gamey) / 1080), int((765 * gamey) / 1080)))
                left1 = False
                up1 = False
                down1 = True
                right1 = True
                print("TOP RIGHT4")
                pygame.display.update()
            else:
               pygame.display.update()
            attack1Text(pokemonUsed1)
            attack2Text(pokemonUsed2)
            attack3Text(pokemonUsed3)
            attack4Text(pokemonUsed4)
            pp1Text(str(pp1))
            pp2Text(str(pp2))
            pp3Text(str(pp3))
            pp4Text(str(pp4))
   
        if keys[pygame.K_SPACE]: # PLAYER CHOOSED THE MOVE AND IT DEALS DAMAGE
                  
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                if pp1 > 0: 
                    newAttackText(pokemonName+ " used "+ pokemonUsed1 + "!")
                    pp1 -= 1
                    pp1Text(str(pp1))
                    playerPokemonAttack()
                    pygame.display.update()
                    for damageDone1 in range (0, attackDamage1):
                        enemyHealth -= 1
                        
                        enemyHealhBar()
                        delay(.01)
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The Foe Fainted!") 
                    else:
                        enemyHealhBar()
                        enemyAttackSequence()
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                        else:
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                    
                
                else:
                    newAttackText(pokemonName+ " is all out!")
                    
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                if pp2 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed2 + "!")
                    playerPokemonAttack()
                    pp2 -= 1
                    pp2Text(str(pp2))
                    pygame.display.update()
                    for damageDone2 in range (0, attackDamage2):
                        enemyHealth -= 1
                        
                        enemyHealhBar()
                        delay(.01)
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The Foe Fainted!") 
                    else:
                        enemyHealhBar()
                        enemyAttackSequence()
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                        else:
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                    
                   
                else:
                    newAttackText(pokemonName+ " is all out!")
                    

            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                if pp3 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed3 + "!")
                    playerPokemonAttack()
                    pp3 -= 1
                    pp3Text(str(pp3))
                    pygame.display.update()
                    for damageDone3 in range (0, attackDamage3):
                        enemyHealth -= 1
                        
                        enemyHealhBar()
                        delay(.01)
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The Foe Fainted!") 
                    else:
                        enemyHealhBar()
                        enemyAttackSequence()
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                        else:
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                    
                    
                else:
                    newAttackText(pokemonName+ " is all out!")
                    
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                if pp4 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed4 + "!")
                    playerPokemonAttack()
                    pp4 -= 1
                    pp4Text(str(pp4))
                    pygame.display.update()
                    for damageDone4 in range (0, attackDamage4):
                        enemyHealth -= 1
                        
                        enemyHealhBar()
                        delay(.01)
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        
                        newAttackText("The Foe Fainted!") 
                    else:
                        enemyHealhBar()
                        enemyAttackSequence()
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                        else:
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                
                    
                    
                else:
                    newAttackText(pokemonName+ " is all out!")
               
                
     

                
        else:
            attack1Text(pokemonUsed1)
            attack2Text(pokemonUsed2)
            attack3Text(pokemonUsed3)
            attack4Text(pokemonUsed4)
            pp1Text(str(pp1))
            pp2Text(str(pp2))
            pp3Text(str(pp3))
            pp4Text(str(pp4))
            pygame.display.update()
            
       
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Animation for the Player throwing the pokeball (BATTLE MODE)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# INITIAL MOVEMENT (PLAYER THROWS POKEBALL)
def animate():
    
    global pokeCounter
    global initialx
    global initialy
    global x
    global y
    global pokex
    global pokey
    global vel
    global bgland1xi
    global bgland2xi
    global bgland1yi
    global bgland2yi
    global bgTransitionxi
    global bgTransitionyi
    global variableBS
    global pokemon2x
    global pokemon2y
    global pokemon2xi
    global pokemon2yi
    # Initial battle start animation
    '''
        redundent code :REDACTED:
    '''
    enemyHealth = 314
    while variableBS < 13:
        pygame.display.update()
        win.blit(pygame.transform.scale(pygame.image.load('battle0.png'), (int(gamex), int(gamey / 2))), (0, 0))
        variableBS += 1
        delay(.08)
    variableBS = 0
    while variableBS < 20:
        pygame.display.update()
        win.blit(pygame.transform.scale(pygame.image.load('battle' + str(variableBS) + '.png'), (int(gamex), int(gamey / 2))), (0, 0))
        variableBS += 1
        delay(.08)
    variableBS = 0
    # Player slides in from the right into position
    while (initialx >= x):
        pygame.display.update()
        initialx -= 10
        pokemon2xi += 10
        bgland1xi -= 10
        bgland2xi += 10
        bgTransitionxi -= 5
        win.fill((0,0,0))
        win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
        win.blit(lower, (0, int((540 * gamey) / 1080)))
        win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
        win.blit(bgrassLand1, (bgland1xi, bgland1yi))
        win.blit(bgrassLand2, (bgland2xi, bgland2yi))
        win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
        win.blit(pygame.transform.scale(pygame.image.load('start3.png'), (playerDimensionx, playerDimensiony)), (initialx, initialy))
        delay(.02)
        
    # Player now in position and ready to throw 
    '''
        redundent code :REDACTED:
    '''
    delay(2)
   
    #Repeats for every frame of the animation
    for variable0 in range (1,10):
        #Set the Background
        win.fill((0,0,0))
        win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
        win.blit(bgrassLand, (0,0))
        win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
        win.blit(lower, (0, int((540 * gamey) / 1080)))
        win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
        #Animate the pokeball
        if variable0 > 5:
            #Pokeball rotation animation
            pokeframe = pygame.transform.scale(pygame.image.load('pokeball' + str(pokeCounter) + '.png'), (pokeballDimensionx, pokeballDimensiony))
            win.blit(pokeframe, (pokex, pokey))
            if pokey < int((190 * gamey) / 1080):
                pokey -= int((18 * gamey) / 1080)
                pokex += int((12 * gamey) / 1080)
                    
            elif pokey < int((180 * gamey) / 1080):
                pokey -= int((10 * gamey) / 1080)
                pokex += int((12 * gamey) / 1080)
                    
            else:
                pokey -= int((40 * gamey) / 1080)
                pokex += int((12 * gamey) / 1080)
            pokeCounter = pokeCounter + 1
            
               
        #Animate the player 
        frame = pygame.transform.scale(pygame.image.load('start'+ str(variable0) +'.png'), (playerDimensionx, playerDimensiony))
        win.blit(frame, (x, y))
        #Update the display 
        pygame.display.update()        
        x -= vel
        delay()
    #move the player off screen after throwing pokeball  
    for variable1 in range (0,15):
        win.fill((0,0,0))
        win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
        win.blit(bgrassLand, (0,0))
        win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
        win.blit(lower, (0, int((540 * gamey) / 1080)))
        win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
        for variable11 in range (0,1):
            #After the player throws the pokeball into the air, this is the animation for it falling and hitting the ground
            pokeframe2 = pygame.transform.scale(pygame.image.load('pokeball' + str(pokeCounter) + '.png'), (pokeballDimensionx, pokeballDimensiony))
            win.blit(pokeframe2, (pokex, pokey))
            if pokey > int((360 * gamey) / 1080):
                pokey += 0
                pokex += 0
                
            elif pokey < int((210 * gamey) / 1080):
                pokey += int((35 * gamey) / 1080)
                pokex += int((12 * gamey) / 1080)
                
            else:
                pokey += int((40 * gamey) / 1080)
                pokex += int((12 * gamey) / 1080)
                
            if pokeCounter > 10:
                pokeCounter = 0
                
            else:
                pokeCounter = pokeCounter + 1
                
        #Player moves to the left until no longer visible
        win.blit(pygame.transform.scale(pygame.image.load('start9.png'), (playerDimensionx, playerDimensiony)), (x,y))
        pygame.display.update()
        x -= vel
        delay()
        
    # The pokemon appears out of the pokeball
    win.fill((0,0,0))
    win.blit(bgrassTransition, (bgTransitionxi, bgTransitionyi))
    win.blit(bgrassLand, (0,0))
    win.blit(enemyPokemon, (pokemon2xi, pokemon2yi))
    win.blit(pokemon, (pokemonx, pokemony))
    pygame.draw.rect(win, (0, 0, 0), (0, int((540 * gamey / 1080) - (gamey / 2 * .25)), battleTextDimensionx, battleTextDimensiony))
    win.blit(lower, (0, int((540 * gamey) / 1080)))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    pygame.display.update()
    
    choose()# PLAYER PICKS WHICH ATTACK TO DO AND THE ENEMY ATTACKS BACK

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RESET THE VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~
    #Reset player position
    initialx = int((1970 * gamex) / resx)
    initialy = int((166 * gamey) / 1080)
    
    x = int((140 * gamex) / resx)
    y = int((165 * gamey) / 1080)
    
    #Reset BG Position
    bgland1xi =int((690 * gamey) / 1080)
    bgland1yi =int((345 * gamey) / 1080)

    bgland2xi =int((-327 * gamey) / 1080)
    bgland2yi =int((202 * gamey) / 1080)

    bgTransitionxi = 0
    bgTransitionyi = 0
    
    #Reset pokeball position
    pokex = int((160 * gamex) / resx)
    pokey = int((255 * gamey) / 1080)
    
    #Reset pokemon position
    pokemon2xi = int((-256 * gamey) / 1080)
    pokemon2yi = int((82 * gamey) / 1080)
    
    pokeCounter = 0
    delay(3)

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Animation for player controlling the sprite 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def moveSprite():
    global walkCount
    global holderx
    global holdery
    

    if walkCount  == 32:
        walkCount = 0
    # FOR walkCount 0 to 7, it will call playerMove(DIRECTION)[0] because // truncates the answer, each image of the walking animation will be held for 8 frames each. (Frame length is determined by superDelay())
    if left:
        win.blit(playerMoveLeft[walkCount // 8], (spritex, spritey))
        walkCount += 1
        holderx = True
        holdery = False
        
    elif right:
        win.blit(playerMoveRight[walkCount // 8], (spritex, spritey))
        walkCount += 1
        holderx = False
        holdery = True
        
    elif front:
        win.blit(playerMoveFront[walkCount // 8], (spritex, spritey))
        walkCount += 1
        holderx = True
        holdery = True
        
    elif back:
        win.blit(playerMoveBack[walkCount // 8], (spritex, spritey))
        walkCount += 1
        holderx = False
        holdery = False
        
    else:
        if holderx and not holdery:
            
            win.blit(playerMoveLeft[1], (spritex, spritey))
            
        elif not holderx and holdery:
            win.blit(playerMoveRight[1], (spritex, spritey))
            
        elif holderx and holdery:
            win.blit(playerMoveFront[1], (spritex, spritey))
            
        elif not holderx and not holdery:
            win.blit(playerMoveBack[1], (spritex, spritey))
            
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Animation for player controlling THE PROFESSOR
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def moveProf():
    global walkCount2
    global holderx2
    global holdery2
    

    if walkCount2  == 32:
        walkCount2 = 0
    
    if left2:
        win.blit(profMoveLeft[walkCount2 // 8], (spritex2, spritey2))
        walkCount2 += 1
        holderx2 = True
        holdery2 = False
        
    elif right2:
        win.blit(profMoveRight[walkCount2 // 8], (spritex2, spritey2))
        walkCount2 += 1
        holderx2 = False
        holdery2 = True
        
    elif front2:
        win.blit(profMoveFront[walkCount2 // 8], (spritex2, spritey2))
        walkCount2 += 1
        holderx2 = True
        holdery2 = True
        
    elif back2:
        win.blit(profMoveBack[walkCount2 // 8], (spritex2, spritey2))
        walkCount2 += 1
        holderx2 = False
        holdery2 = False
        
    else:
        if holderx2 and not holdery2:
            
            win.blit(profMoveLeft[1], (spritex2, spritey2))
            
        elif not holderx2 and holdery2:
            win.blit(profMoveRight[1], (spritex2, spritey2))
            
        elif holderx2 and holdery2:
            win.blit(profMoveFront[1], (spritex2, spritey2))
            
        elif not holderx2 and not holdery2:
            win.blit(profMoveBack[1], (spritex2, spritey2))

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    WHAT SHOULD THE SPRITE DO IF IT RUNS INTO A WALL?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
            
   
def borderLeft():
    global thelabLeftBox
    global thelabRightBox
    global thelabTopBox
    global thelabBottomBox
    global thelabWallLeftBox
    global thelabWallRightBox
    global thelabWallTopBox
    global thelabWallBottomBox
    global machineLeftBox
    global machineRightBox
    global machineBottomBox
    global theLaby
    global theLabx
    global spriteVel
    global spritex
    global spritey
    global spritex2
    global spritey2
    global benchRightBox
    global benchBottomBox
    global deskTopBox
    global deskRightBox
    global deskLeftBox
    global bookShelfBottomBox
    global bookShelfTopBox
    global bookShelfRightBox
    global dangerZoneTop
    global dangerZoneBottom
    global dangerZoneLeft
    global dangerZoneRight
    global dangerZoneTop2
    global dangerZoneBottom2
    global dangerZoneLeft2
    global dangerZoneRight2
    dangerZoneRight2 += spriteVel
    dangerZoneLeft2 += spriteVel
    dangerZoneRight += spriteVel
    dangerZoneLeft += spriteVel
    bookShelfRightBox += spriteVel
    deskRightBox += spriteVel
    deskLeftBox += spriteVel
    benchRightBox += spriteVel
    thelabLeftBox += spriteVel
    thelabRightBox += spriteVel
    thelabWallLeftBox += spriteVel
    thelabWallRightBox += spriteVel
    machineLeftBox += spriteVel
    machineRightBox += spriteVel
    spritex2 += spriteVel
    theLabx += spriteVel
    
def borderRight():
    global thelabLeftBox
    global thelabRightBox
    global thelabTopBox
    global thelabBottomBox
    global thelabWallLeftBox
    global thelabWallRightBox
    global thelabWallTopBox
    global thelabWallBottomBox
    global machineLeftBox
    global machineRightBox
    global machineBottomBox
    global theLaby
    global theLabx
    global spriteVel
    global spritex
    global spritey
    global spritex2
    global spritey2
    global benchRightBox
    global benchBottomBox
    global deskTopBox
    global deskRightBox
    global deskLeftBox
    global bookShelfBottomBox
    global bookShelfTopBox
    global bookShelfRightBox
    global dangerZoneTop
    global dangerZoneBottom
    global dangerZoneLeft
    global dangerZoneRight
    global dangerZoneTop2
    global dangerZoneBottom2
    global dangerZoneLeft2
    global dangerZoneRight2
    dangerZoneRight2 -= spriteVel
    dangerZoneLeft2 -= spriteVel
    dangerZoneRight -= spriteVel
    dangerZoneLeft -= spriteVel
    bookShelfRightBox -= spriteVel
    deskRightBox -= spriteVel
    deskLeftBox -= spriteVel
    benchRightBox -= spriteVel
    thelabLeftBox -= spriteVel
    thelabRightBox -= spriteVel
    thelabWallLeftBox -= spriteVel
    thelabWallRightBox -= spriteVel
    machineLeftBox -= spriteVel
    machineRightBox -= spriteVel
    spritex2 -= spriteVel
    theLabx -= spriteVel
    
def borderUp():
    global thelabLeftBox
    global thelabRightBox
    global thelabTopBox
    global thelabBottomBox
    global thelabWallLeftBox
    global thelabWallRightBox
    global thelabWallTopBox
    global thelabWallBottomBox
    global machineLeftBox
    global machineRightBox
    global machineBottomBox
    global theLaby
    global theLabx
    global spriteVel
    global spritex
    global spritey
    global spritex2
    global spritey2
    global benchRightBox
    global benchBottomBox
    global deskTopBox
    global deskRightBox
    global deskLeftBox
    global bookShelfBottomBox
    global bookShelfTopBox
    global bookShelfRightBox
    global dangerZoneTop
    global dangerZoneBottom
    global dangerZoneLeft
    global dangerZoneRight
    global dangerZoneTop2
    global dangerZoneBottom2
    global dangerZoneLeft2
    global dangerZoneRight2
    dangerZoneTop2 += spriteVel
    dangerZoneBottom2 += spriteVel
    dangerZoneTop += spriteVel
    dangerZoneBottom += spriteVel
    bookShelfTopBox += spriteVel
    bookShelfBottomBox += spriteVel
    deskTopBox += spriteVel
    benchBottomBox += spriteVel
    thelabWallTopBox += spriteVel
    thelabWallBottomBox += spriteVel
    machineBottomBox += spriteVel
    thelabTopBox += spriteVel
    thelabBottomBox += spriteVel
    spritey2 += spriteVel
    theLaby += spriteVel
    
def borderDown():
    global thelabLeftBox
    global thelabRightBox
    global thelabTopBox
    global thelabBottomBox
    global thelabWallLeftBox
    global thelabWallRightBox
    global thelabWallTopBox
    global thelabWallBottomBox
    global machineLeftBox
    global machineRightBox
    global machineBottomBox
    global theLaby
    global theLabx
    global spriteVel
    global spritex
    global spritey
    global spritex2
    global spritey2
    global benchRightBox
    global benchBottomBox
    global deskTopBox
    global deskRightBox
    global deskLeftBox
    global bookShelfBottomBox
    global bookShelfTopBox
    global bookShelfRightBox
    global dangerZoneTop
    global dangerZoneBottom
    global dangerZoneLeft
    global dangerZoneRight
    global dangerZoneTop2
    global dangerZoneBottom2
    global dangerZoneLeft2
    global dangerZoneRight2
    dangerZoneTop2 -= spriteVel
    dangerZoneBottom2 -= spriteVel
    dangerZoneTop -= spriteVel
    dangerZoneBottom -= spriteVel
    bookShelfTopBox -= spriteVel
    bookShelfBottomBox -= spriteVel
    deskTopBox -= spriteVel
    benchBottomBox -= spriteVel
    thelabWallTopBox -= spriteVel
    thelabWallBottomBox -= spriteVel
    machineBottomBox -= spriteVel
    thelabTopBox -= spriteVel
    thelabBottomBox -= spriteVel
    spritey2 -= spriteVel
    theLaby -= spriteVel

    


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    PLAYER PICKS HIS STARTER POKEMON!
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
       
def pickAPokemon():
    pokeHolder = True
    leftButton= False
    middleButton= False
    rightButton= False
    global pokemon
    while pokeHolder:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not leftButton and not middleButton and rightButton: # IF RIGHT
                leftButton = False
                middleButton = True
                rightButton = False
                newAttackText("PIPLUP?")
                
                delay(.025)
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                leftButton = True
                middleButton = False
                rightButton = False
                newAttackText("TURTWIG?")
                
            else: # IF LEFT
                leftButton = True
                middleButton = False
                rightButton = False
                newAttackText("TURTWIG?")
                
               
        elif keys[pygame.K_RIGHT]:
            if leftButton and not middleButton and not rightButton: # IF LEFT
                leftButton = False
                middleButton = True
                rightButton = False
                newAttackText("PIPLUP?")
               
                delay(.025)
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                leftButton = False
                middleButton = False
                rightButton = True
                newAttackText("CHIMCHAR?")
               
            else: # IF RIGHT
                leftButton = False
                middleButton = False
                rightButton = True
                newAttackText("CHIMCHAR?")
                    
        elif keys[pygame.K_SPACE]:
            if leftButton and not middleButton and not rightButton: # IF LEFT
                pokemon = turtwigB
                pokeHolder = False
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                pokemon = piplupB
                pokeHolder = False
            elif not leftButton and not middleButton and rightButton: # IF RIGHT
                pokemon = chimcharB
                pokeHolder = False
            
        else:
            pygame.display.update()


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                    Inside the Grass some lyes yet unseen?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                   
def dangerZone():
    global dangerZoneTop
    global dangerZoneBottom
    global dangerZoneLeft
    global dangerZoneRight
    global thelabTopBox
    global thelabWallRightBox
    # MAX VALUES
    '''
    dangerZone TOP = -100
    dangerZone BOTTOM = 225
    dangerZone RIGHT = 1077
    dangerZone Left = 740
    '''
    dangerZonePotentialTop = [0, 50, 100, 150, 200, 250, 300]
    dangerZonePotentialLeft = [0, 50, 100, 150, 200, 250, 300]

    dangerZoneTop = thelabTopBox + (random.choice(dangerZonePotentialTop))
    dangerZoneLeft = thelabWallRightBox + (random.choice(dangerZonePotentialLeft))
    dangerZoneRight = int(dangerZoneLeft) + int((50 * gamey) / 1080)
    dangerZoneBottom = int(dangerZoneTop) + int((50 * gamey) / 1080)
    
def dangerZone2():
    global dangerZoneTop2
    global dangerZoneBottom2
    global dangerZoneLeft2
    global dangerZoneRight2
    global thelabTopBox
    global thelabWallRightBox
    # MAX VALUES
    '''
    dangerZone TOP = -100
    dangerZone BOTTOM = 225
    dangerZone RIGHT = 1077
    dangerZone Left = 740
    '''
    dangerZonePotentialTop = [0, 50, 100, 150, 200, 250, 300]
    dangerZonePotentialLeft = [0, 50, 100, 150, 200, 250, 300]

    dangerZoneTop2 = thelabTopBox + (random.choice(dangerZonePotentialTop))
    dangerZoneLeft2 = thelabWallRightBox + (random.choice(dangerZonePotentialLeft))
    dangerZoneRight2 = int(dangerZoneLeft2) + int((50 * gamey) / 1080)
    dangerZoneBottom2 = int(dangerZoneTop2) + int((50 * gamey) / 1080)
    
        
   
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#                                                                                ~ANIMATION THAT STARTS THE GAME~
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
dangerZone()
dangerZone2()


def profLeftAnimation():
    global front2
    global back2
    global left2
    global right2
    front2 = False
    left2 = True
    right2 = False
    back2 = False
def profRightAnimation():
    global front2
    global back2
    global left2
    global right2
    front2 = False
    left2 = False
    right2 = True
    back2 = False
def profUpAnimation():
    global front2
    global back2
    global left2
    global right2
    front2 = False
    left2 = False
    right2 = False
    back2 = True
def profDownAnimation():
    global front2
    global back2
    global left2
    global right2
    front2 = True
    left2 = False
    right2 = False
    back2 = False

def playerLeftAnimation():
    global front
    global back
    global left
    global right
    left = True
    right = False
    front = False
    back = False
def playerRightAnimation():
    global front
    global back
    global left
    global right
    left = False
    right = True
    front = False
    back = False
def playerUpAnimation():
    global front
    global back
    global left
    global right
    left = False
    right = False
    front = False
    back = True
def playerDownAnimation():
    global front
    global back
    global left
    global right
    left = False
    right = False
    front = True
    back = False
def setLowerLabLights():
    global theLabx
    global theLaby
    win.blit(bookshelf3, (theLabx, theLaby))
    win.blit(bookshelf2, (theLabx, theLaby))
    win.blit(bookshelf1, (theLabx, theLaby))
    win.blit(theLabLights, (theLabx, theLaby))
    win.blit(lower, (0, int((540 * gamey) / 1080)))
    
profVel = int((5  * gamey) / 1080)
spriteVel = int((5  * gamey) / 1080)

for profSteps in range (0, 50): # PROF SITS AT DESK THEN NOTICES YOU
    superDelay()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    pygame.display.update()
    
newText("Oh hello there!") # DIALOGUE
delay(.5)

for profSteps in range (0, 30): # PROF WALKS UP AWAY FROM DESK
    superDelay()
    profUpAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritey2 -= profVel
    pygame.display.update()
    
for profSteps in range (0, 55): # PROF WALKS LEFT TOWARDS YOU
    superDelay()
    profLeftAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritex2 -= profVel
    pygame.display.update()

for profSteps in range (0, 20): # PROF WALKS DOWN TOWARDS YOU
    superDelay()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritey2 += profVel
    pygame.display.update()
newText("Welcome to the Pokemon testing and training center!") # DIALOGUE
newAttackText("Let me show you around ") # DIALOGUE
delay(.5)
newText("Follow me!") # DIALOGUE
delay(.05)
for profSteps in range (0, 6): # PROF WALKS UP AWAY
    superDelay()
    profUpAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritey2 -= profVel
    pygame.display.update()

for profSteps in range (0,30): # YOU FOLLOW HIM UP
    superDelay()
    playerUpAnimation()
    profUpAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritey2 -= profVel
    borderUp()
    pygame.display.update()

for profSteps in range (0,21): # PROF WALKS RIGHT WHILE YOU STILL GO UP
    superDelay()
    playerUpAnimation()
    profRightAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritex2 += profVel
    borderUp()
    pygame.display.update()

win.fill((0, 0, 0))
win.blit(theLab, (theLabx, theLaby))
win.blit(profMoveFront[1], (spritex2, spritey2))
win.blit(playerMoveRight[1], (spritex, spritey))
setLowerLabLights()
pygame.display.update()
delay(.8)
newAttackText("This is a place where people    can come to train their pokemon,") # DIALOGUE
delay(.7)
newAttackText("as well as try out new ones") # DIALOGUE
delay(1)
for profSteps in range (0,40): # PROF WALKS RIGHT WHILE YOU FOLLOW
    superDelay()
    playerRightAnimation()
    profRightAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritex2 += profVel
    borderRight()
    pygame.display.update()
    
for profSteps in range (0,5): # YOU FOLLOW PROF TO THE RIGHT
    superDelay()
    playerRightAnimation()
    profLeftAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    win.blit(profMoveLeft[1], (spritex2, spritey2))
    moveSprite()
    setLowerLabLights()
    borderRight()
    pygame.display.update()
    
win.fill((0, 0, 0))
win.blit(theLab, (theLabx, theLaby))
win.blit(profMoveLeft[1], (spritex2, spritey2))
win.blit(playerMoveRight[1], (spritex, spritey))
setLowerLabLights()
pygame.display.update()
delay(1)
newAttackText("Hmmm...") # DIALOGUE
delay(1)
newText('I see that you dont have any   Pokemon on you.') # DIALOGUE
newText("No worries! we have a few that are ready for training here!") # DIALOGUE
win.fill((0, 0, 0))
win.blit(theLab, (theLabx, theLaby))
win.blit(profMoveBack[1], (spritex2, spritey2))
win.blit(playerMoveBack[1], (spritex, spritey))
setLowerLabLights()
pygame.display.update()
newText("You can take one of these pokeballs       and find a pokemon that suits you!") # DIALOGUE

for profSteps in range (0,15): # YOU GO RIGHT AS PROF GOES DOWN
    superDelay()
    playerRightAnimation()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritey2 += profVel
    borderRight()
    pygame.display.update()

for profSteps in range (0,10): # YOU BOTH WALK DOWN
    superDelay()
    playerDownAnimation()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf()
    moveSprite()
    setLowerLabLights()
    spritey2 += profVel
    borderDown()
    pygame.display.update()

win.fill((0, 0, 0))
win.blit(theLab, (theLabx, theLaby))
win.blit(playerMoveFront[1], (spritex, spritey))
win.blit(profMoveBack[1], (spritex2, spritey2))
setLowerLabLights()
pygame.display.update()
newAttackText("To my right is where you can encounter wild Pokemon,") # DIALOGUE
delay(.8)
newText("a simulation of them at least.") # DIALOGUE
delay(.5)
win.fill((0, 0, 0))
win.blit(theLab, (theLabx, theLaby))
win.blit(playerMoveFront[1], (spritex, spritey))
win.blit(profMoveRight[1], (spritex2, spritey2))
setLowerLabLights()
pygame.display.update()
newAttackText("This area is designed to        function as") # DIALOGUE
delay(.4)
newText("a way to battle wild Pokemon   without having to find them!") # DIALOGUE
newText("This allows us to collect data on Pokemon battles efficiently.") # DIALOGUE

for profSteps in range (0,5): #YOU BOTH WALK DOWN FOR A LIL BIT
    superDelay()
    playerDownAnimation()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritey2 += profVel
    borderDown()
    pygame.display.update()

for profSteps in range (0,15): # PROF WALKS TO THE LEFT WHILE YOU WALK DOWN
    superDelay()
    playerDownAnimation()
    profLeftAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritex2 -= profVel
    borderDown()
    pygame.display.update()

for profSteps in range (0,30): # YOU FOLLOW PROF TO THE LEFT
    superDelay()
    playerLeftAnimation()
    profLeftAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()
    setLowerLabLights()
    spritex2 -= profVel
    borderLeft()
    pygame.display.update()

for profSteps in range (0,10): # YOU FOLLOW PROF TO THE LEFT
    superDelay()
    playerDownAnimation()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveSprite()
    moveProf()   
    setLowerLabLights()
    borderDown()
    spritey2 += profVel
    pygame.display.update()

newAttackText("Should your pokemon faint in     the midst of battle,") # DIALOGUE
delay(.5)
newText("You can use this machine here    to restore its health.") # DIALOGUE
newAttackText("We dont carry potions here, ") # DIALOGUE
delay(.5)
newText("so this is the only way to heal your pokemon if it gets hurt." ) # DIALOGUE

newAttackText("Well,") # DIALOGUE
delay(.5)
newText("Thats about all there is to       know about this place.") # DIALOGUE
delay(.5)
newAttackText("why dont you go and pick a     pokemon ") # DIALOGUE
delay(.4)
newText("you would like to use          in battle.") # DIALOGUE
newAttackText("Ill be at my desk, ") # DIALOGUE
delay(.4)
newText("so go ahead and battle to your hearts content!") # DIALOGUE
for profSteps in range (0,10): # PROF WALKS UP
    superDelay()
    profUpAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    win.blit(playerMoveFront[1], (spritex, spritey))
    moveProf()   
    setLowerLabLights()
    spritey2 -= profVel
    pygame.display.update()

for profSteps in range (0,38): # PROF WALKS TO THE LEFT
    superDelay()
    profRightAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    moveProf() 
    win.blit(playerMoveFront[1], (spritex, spritey))
    setLowerLabLights()
    spritex2 += profVel
    pygame.display.update()

for profSteps in range (0,17): # PROF WALKS TO HIS DESK
    superDelay()
    profDownAnimation()
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    win.blit(playerMoveFront[1], (spritex, spritey))
    moveProf()   
    setLowerLabLights()
    spritey2 += profVel
    pygame.display.update()

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#                                                                                ~While loop that runs the game~
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



while run:
    pygame.event.get()
    superDelay()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        spriteVel = int((3 * gamey) / 1080)
    elif keys[pygame.K_LSHIFT]:
        spriteVel = int((11 * gamey) / 1080)
    else:
        spriteVel = int((7  * gamey) / 1080)
    if keys[pygame.K_ESCAPE]:
        run = False
        print('\n' * 5)
        print("Thanks for playing!")
    if (machineLeftBox <= spritex <= machineRightBox) and (spritey <= machineBottomBox + 50):
        if keys[pygame.K_SPACE]:
            
            win.blit(pokeballSelection, (0, 0))
            pygame.display.update()
            pickAPokemon()
            delay(1)
            
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~PLAYER~~~~~~~~~~~~~~~~~~~~~~~~~~
            
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BORDERS AND HITBOXES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if (thelabWallLeftBox <= spritex <= thelabWallRightBox) and ((thelabWallBottomBox <= spritey) or ( spritey <= thelabWallTopBox)):
        if holderx and not holdery: # LEFT into wall
            borderRight()
            
        elif not holderx and holdery: # RIGHT into wall
            borderLeft()
            
    elif (machineLeftBox <= spritex <= machineRightBox) and (spritey <= machineBottomBox):
        if holderx and not holdery: # LEFT into wall
            borderRight()
            
        elif not holderx and holdery: # RIGHT into wall
            borderLeft()
            
        elif not holderx and not holdery: # UP into wall
            borderDown()
            
        elif holderx and holdery: # DOWN into wall
            borderUp()
            
    elif (spritey <= benchBottomBox) and (spritex <= benchRightBox):
        if holderx and not holdery: # LEFT into wall
            borderRight()   
        elif not holderx and not holdery: # UP into wall
            borderDown()
    elif (deskLeftBox <= spritex <= deskRightBox) and (spritey >= deskTopBox):
        if holderx and not holdery: # LEFT into wall
            borderRight()
            
        elif not holderx and holdery: # RIGHT into wall
            borderLeft()
            
        elif holderx and holdery: # DOWN into wall
            borderUp()
            
    elif (bookShelfBottomBox >= spritey >= bookShelfTopBox) and (spritex <= bookShelfRightBox):
        if holderx and not holdery: # LEFT into wall
            borderRight()
                
        elif not holderx and not holdery: # UP into wall
            borderDown()
                
        elif holderx and holdery: # DOWN into wall
            borderUp()
    elif (dangerZoneBottom >= spritey >= dangerZoneTop) and (dangerZoneLeft <= spritex <= dangerZoneRight):
        delay(1.5)
        win.fill((0, 0, 0))
        win.blit(lower, (0, int((540 * gamey) / 1080)))
        delay(.5)
        pygame.display.update()
        enemyPokemonStuff()# DECIDE THE ENEMY POKEMON
        dangerZone()
        animate()
        pygame.display.update()
    elif (dangerZoneBottom2 >= spritey >= dangerZoneTop2) and (dangerZoneLeft2 <= spritex <= dangerZoneRight2):
        delay(1.5)
        win.fill((0, 0, 0))
        win.blit(lower, (0, int((540 * gamey) / 1080)))
        delay(.5)
        pygame.display.update()
        enemyPokemonStuff()# DECIDE THE ENEMY POKEMON
        dangerZone2()
        animate()
        pygame.display.update()
        
                
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
            
    if keys[pygame.K_LEFT]:
        if spritex <= thelabLeftBox:
            pygame.display.update()
        else: borderLeft()
          
        left = True
        right = False
        front = False
        back = False      
            
    elif keys[pygame.K_RIGHT]:
        if spritex >= thelabRightBox:
            pygame.display.update()
        else: borderRight()
            
        right = True
        left = False
        front = False
        back = False
        
    elif keys[pygame.K_UP]:
        if spritey <= thelabTopBox:
            pygame.display.update()
        else: borderUp()
            
        front = False
        left = False
        right = False
        back = True
        
    elif keys[pygame.K_DOWN]:
        if spritey >= thelabBottomBox:
            pygame.display.update()
        else: borderDown()
            
        back = False
        left = False
        right = False
        front = True
        
    else:
        left = False
        right = False
        front = False
        back = False
        walkCount = 0
        
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PROFESSOR~~~~~~~~~~~~~~~~~~~~~~~~~~
    if keys[pygame.K_a]:
        spritex2 -= spriteVel
        left2 = True
        right2 = False
        front2 = False
        back2 = False      
            
    elif keys[pygame.K_d]:
        spritex2 += spriteVel
        right2 = True
        left2 = False
        front2 = False
        back2 = False
        
    elif keys[pygame.K_w]:
        spritey2 -= spriteVel
        front2 = False
        left2 = False
        right2 = False
        back2 = True
        
    elif keys[pygame.K_s]:
        spritey2 += spriteVel
        back2 = False
        left2 = False
        right2 = False
        front2 = True
        
    else:
        left2 = False
        right2 = False
        front2 = False
        back2 = False
        walkCount2 = 0

    # Set the background    
    win.fill((0, 0, 0))
    win.blit(theLab, (theLabx, theLaby))
    

    
    if spritex > bookShelfBottomBox:
        win.blit(bookshelf3, (theLabx, theLaby))
        win.blit(bookshelf2, (theLabx, theLaby))
        win.blit(bookshelf1, (theLabx, theLaby))
        if spritey2 > spritey:
            moveSprite()
            moveProf()
        else:
            moveProf()
            moveSprite()
        
    else:
        if spritey2 > spritey:
            moveSprite()
            moveProf()
        else:
            moveProf()
            moveSprite()
        win.blit(bookshelf3, (theLabx, theLaby))
        win.blit(bookshelf2, (theLabx, theLaby))
        win.blit(bookshelf1, (theLabx, theLaby))
        
    
   
    win.blit(theLabLights, (theLabx, theLaby))
    win.blit(lower, (0, int((540 * gamey) / 1080)))
    # SECRET SHORTCUTS
    if keys[pygame.K_1]:
        pygame.draw.rect(win, (255, 0, 0), (dangerZoneRight, dangerZoneBottom, int((50 * gamey) / 1080), int((50 * gamey) / 1080)))
        pygame.draw.rect(win, (255, 0, 0), (dangerZoneRight2, dangerZoneBottom2, int((50 * gamey) / 1080), int((50 * gamey) / 1080)))
    if keys[pygame.K_2]:
        dangerZone()
        dangerZone2()
    pygame.display.update()
    if keys[pygame.K_3]:
         playerHealth = 314
         enemyHealth = 314
         print("Health Restored")
    if keys[pygame.K_4]:
        pokemon = turtwigB
        print("Pokemon set to Turtwig")
        
    if keys[pygame.K_5]:
        pokemon = piplupB
        print("Pokemon set to Piplup")
        
    if keys[pygame.K_6]:
        pokemon = chimcharB
        print("Pokemon set to Chimchar")
        
   
    
    
pygame.quit()




'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                        REFERENCES (REDACTED/REDUNDANT CODE)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Player now in position and ready to throw 
'''
    win.fill((0,0,0))
    win.blit(bgrass, (0,0))
    win.blit(lower, (0, int((540 * gamey) / 1080)))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    win.blit(pygame.transform.scale(pygame.image.load('start3.png'), (playerDimensionx, playerDimensiony)), (x, y))
    pygame.display.update()
'''
# Initial battle start animation
'''    
    # First Frame, sets the background and the Players first position
    win.fill((0,0,0))
    win.blit(bgrassTransition, (bgTransitionxi,bgTransitionyi))
    
    
    win.blit(lower, (0, int((540 * gamey) / 1080)))
    win.blit(battleText, (0, int((540 * gamey) / 1080) - ((gamey / 2) * .25)))
    pygame.display.update()
    delay(2)
'''
'''                            
    win.blit(bgrass, (0,0))
    win.blit(pygame.transform.scale(pygame.image.load('start3.png'), (playerDimensionx, playerDimensiony)), (x, y))
    pygame.display.update()
    x -= vel
    time.sleep(.05)

    Original sprite image is 31 x 31

    When scaling to the x and y dimensions of an item. use (x * gamey / 1080)
    When finding the x position of a sprite, use (x * gamex / resx)
    When findinf the y position of a sprite, usse (gamey)
'''
#TYPING TEST
'''
newText("I am not very good at typing butI do knoe how to type ?")
newText("1 2  3   4    5     6      7       8        9         10")
newText
newText('a')
newText('aa')
newText('aaa')
newText('aaaa')
newText('aaaaa')
newText('aaaaaa')
newText('aaaaaaa')
newText('aaaaaaaa')
newText('aaaaaaaaa')
newText('aaaaaaaaaa')
newText('aaaaaaaaaaa')
newText('aaaaaaaaaaaa')
newText('aaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
newText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
'''
# RILEY'S IMAGES
'''
rileyMoveLeft = [pygame.transform.scale(pygame.image.load('al0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('al1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('al2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('al3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
rileyMoveRight = [pygame.transform.scale(pygame.image.load('ar0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('ar1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('ar2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('ar3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
rileyMoveFront = [pygame.transform.scale(pygame.image.load('af0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('af1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('af2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('af3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]
rileyMoveBack = [pygame.transform.scale(pygame.image.load('ab0.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('ab1.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)), pygame.transform.scale(pygame.image.load('ab2.png').convert_alpha(), (spriteDimensionx, spriteDimensiony)),pygame.transform.scale(pygame.image.load('ab3.png').convert_alpha(), (spriteDimensionx, spriteDimensiony))]

'''


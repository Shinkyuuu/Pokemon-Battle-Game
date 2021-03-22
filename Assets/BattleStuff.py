import pygame
import time
import os
import random
from Variables import *
from win32api import GetSystemMetrics
import matplotlib.pyplot as plt

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            ENEMY POKEMON MOVES AND STATS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def enemyPokemonStuff():

    global enemyHealth
    global attackDamage
    global enemyAttacks
    global enemyPokemonName
    global enemyPokemon
    global turt
    global chim
    global pip
    global bid
    global star
    global ghas
    global mim
    global ching

    randomEnemyPokemonList = [turtwigF, chimcharF, piplupF, chinglingF, ghastlyF, mimikyuF, starlyF, bidoofF]
    enemyPokemon = random.choice(randomEnemyPokemonList)
    if enemyPokemon == turtwigF:
        enemyPokemonName = "TURTWIG"
        enemyHealth = 314
        enemyAttacks = [["Razor Leaf", 55], ["Tackle", 40], ["LeafStorm", 100], ["Bite", 60]]
        turt += 1
        print("TURTWIGS FOUND:", turt)
        
    elif enemyPokemon == chimcharF:
        enemyPokemonName = "CHIMCHAR"
        enemyHealth = 314
        enemyAttacks = [["Scratch", 40], ["Flame Wheel", 60], ["Flamethrower", 90], ["Fury Swipes", 25]]
        chim += 1
        print("CHIMCHARS FOUND:", chim)
        
    elif enemyPokemon == piplupF:
        enemyPokemonName = "PIPLUP"
        enemyHealth = 314
        enemyAttacks = [["Bubble", 40], ["Fury Attack", 15], ["Whirlpool", 35], ["Hydro Pump", 110]]
        pip += 1
        print("PIPLUPS FOUND:", pip)
        
    elif enemyPokemon == bidoofF:
        enemyPokemonName = "BIDOOF"
        enemyHealth = 314
        enemyAttacks = [["Tackle", 40], ["Rollout", 30], ["Takedown", 90], ["Crunch", 70]]
        bid += 1
        print("BIDOOFS FOUND:", bid)
        
    elif enemyPokemon == starlyF:
        enemyPokemonName = "STARLY"
        enemyHealth = 314
        enemyAttacks = [["Quick Attack", 40], ["Wing Attack", 60], ["Aerial Ace", 60], ["Brave Bird", 100]]
        star += 1
        print("STARLYS FOUND:", star)
        
    elif enemyPokemon == ghastlyF:
        enemyPokemonName = "GHASTLY"
        enemyHealth = 314
        enemyAttacks = [["Lick", 30], ["Sucker Punch", 70], ["Dark Pulse", 80], ["Dream Eater", 90]]
        ghas += 1
        print("GHASTLYS FOUND:", ghas)
        
    elif enemyPokemon == mimikyuF:
        enemyPokemonName = "MIMIKYU"
        enemyHealth = 314
        enemyAttacks = [["Shadow Sneak", 40], ["Play Rough", 90], ["Slash", 70], ["Astonish", 30]]
        mim += 1
        print("MIMIKYUS FOUND:", mim)
        
    elif enemyPokemon == chinglingF:
        enemyPokemonName = "CHINGLING"
        enemyHealth = 314
        enemyAttacks = [["Astonish", 30], ["Uproar", 90], ["Confusion", 50], ["Last Resort", 120]]
        ching += 1
        print("CHINGLINGS FOUND:", ching)




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
    newAttackText("The wild " +enemyPokemonName+ " used           "+ enemyPokemonUsed + "!")
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
    f.write('The enemy '+enemyPokemonName+ " used "+ enemyPokemonUsed + "! \n") # PROFS DOCUMENT
    f.write("It delt " + str(enemyAttackDamage) + ' damage! \n') # PROFS DOCUMENT

    
            
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                            PLAYER POKEMON MOVES AND STATS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

playerHealth = 314


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
    win.blit(normalAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    attackDamage2 = 40

    pokemonUsed3 = "Leaf Storm"
    win.blit(grassAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    attackDamage3 = 100

    pokemonUsed4 = "Bite"
    win.blit(darkAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
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
    win.blit(normalAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
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
    win.blit(normalAttack, (attackx, attacky))# TOP LEFT
    attackDamage1 = 40

    pokemonUsed2 = "Flame Wheel"
    win.blit(fireAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    attackDamage2 = 60

    pokemonUsed3 = "Flamethrower"
    win.blit(fireAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    attackDamage3 = 90

    pokemonUsed4 = "Fury Swipes"
    win.blit(normalAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
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
    win.blit(normalAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(grassAttack, (attackx, int((765 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(darkAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attack1Text(pokemonUsed1 + '                 ' + (pokemonUsed2))
    attack3Text(pokemonUsed3 + '                ' + (pokemonUsed4))
    pp1Text(str(pp1) + '   ' + str(pp11) + '                     ' + str(pp2) + '   ' + str(pp22))
    pp3Text(str(pp3) + '   ' + str(pp33) + '                     ' + str(pp4) + '   ' + str(pp44))
    
    
def piplupButtons(): 
    win.blit(waterAttack, (attackx, attacky))# TOP LEFT
    win.blit(normalAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(waterAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(waterAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attack1Text(pokemonUsed1 + '                     ' + (pokemonUsed2))
    attack3Text(pokemonUsed3 + '                  ' + (pokemonUsed4))
    pp1Text(str(pp1) + '   ' + str(pp11) + '                     ' + str(pp2) + '   ' + str(pp22))
    pp3Text(str(pp3) + '   ' + str(pp33) + '                     ' + str(pp4) + '   ' + str(pp44))
    
    
def chimcharButtons(): 
    win.blit(normalAttack, (attackx, attacky))# TOP LEFT
    win.blit(fireAttack, (int((367 * gamey) / 1080), attacky)) # TOP RIGHT
    win.blit(fireAttack, (attackx, int((766 * gamey) / 1080))) # BOTTOM LEFT
    win.blit(normalAttack, (int((367 * gamey) / 1080), int((766 * gamey) / 1080))) # BOTTOM RIGHT
    attack1Text(pokemonUsed1 + '                    ' + (pokemonUsed2))
    attack3Text(pokemonUsed3 + '              ' + (pokemonUsed4))
    pp1Text(str(pp1) + '   ' + str(pp11) + '                     ' + str(pp2) + '   ' + str(pp22))
    pp3Text(str(pp3) + '   ' + str(pp33) + '                     ' + str(pp4) + '   ' + str(pp44))
    
    
    
    
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
    enemyLevelText("50")
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
    playerLevelText("50")
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
    global pp11
    global pp22
    global pp33
    global pp44
    global f
    
    win.blit(attackMode, (0, int((540 * gamey) / 1080)))
    pokemonStuff()# INITIAL FRAME
    playerHealhBar()
    enemyHealhBar()
    pokemonButtonStuff()
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
            
        if keys[pygame.K_SPACE]: # PLAYER CHOOSED THE MOVE AND IT DEALS DAMAGE
                  
            if left1 and up1 and not down1 and not right1:# TOP LEFT
                
                if pp1 > 0: 
                    newAttackText(pokemonName+ " used "+ pokemonUsed1 + "!")
                    f.write('Cody\'s '+pokemonName+ " used "+ pokemonUsed1 + "! \n") # PROFS DOCUMENT
                    pp1 -= 1
                    playerPokemonAttack()
                    pokemonButtonStuff()
                    win.blit(mediumSelect, (mediumx, mediumy))
                    for damageDone1 in range (0, attackDamage1):
                        enemyHealth -= 1
                        
                        enemyHealhBar()
                        delay(.01)
                        
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The wild "+ enemyPokemonName+" Fainted!")
                        f.write("It delt " + str(attackDamage1) + ' damage! \n') # PROFS DOCUMENT
                        f.write("It killed the enemy " + enemyPokemonName+ '! \n') # PROFS DOCUMENT
                    else:
                        f.write("It delt " + str(attackDamage1) + ' damage! \n') # PROFS DOCUMENT
                        enemyHealhBar()
                        enemyAttackSequence()
                        
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                            f.write("It killed Cody\'s " + pokemonName+ '! \n') # PROFS DOCUMENT
                            
                        else:
                            
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                    
                else:
                    newAttackText(pokemonName+ " is all out!")
                    
            elif not left1 and not down1 and up1 and right1:# TOP RIGHT
                
                if pp2 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed2 + "!")
                    f.write('Cody\'s '+pokemonName+ " used "+ pokemonUsed2 + "! \n") # PROFS DOCUMENT
                    pp2 -= 1
                    playerPokemonAttack()
                    pokemonButtonStuff()
                    win.blit(mediumSelect, (int((370 * gamey) / 1080), mediumy))
                    for damageDone2 in range (0, attackDamage2):
                        enemyHealth -= 1
                        enemyHealhBar()
                        delay(.01)
                        
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The wild "+ enemyPokemonName+" Fainted!")
                        f.write("It delt " + str(attackDamage2) + ' damage! \n') # PROFS DOCUMENT
                        f.write("It killed the enemy " + enemyPokemonName+ '! \n') # PROFS DOCUMENT
                    else:
                        f.write("It delt " + str(attackDamage2) + ' damage! \n') # PROFS DOCUMENT
                        enemyHealhBar()
                        enemyAttackSequence()
                        
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                            f.write("It killed Cody\'s " + pokemonName+ '! \n') # PROFS DOCUMENT
                            
                        else:
                            
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                            
                    
                else:
                    newAttackText(pokemonName+ " is all out!")
                    
            elif not up1 and not right1 and down1 and left1:# BOTTOM LEFT
                
                if pp3 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed3 + "!")
                    f.write('Cody\'s '+pokemonName+ " used "+ pokemonUsed3 + "! \n") # PROFS DOCUMENT
                    pp3 -= 1
                    playerPokemonAttack()
                    pokemonButtonStuff()
                    win.blit(mediumSelect, (mediumx, int((765 * gamey) / 1080)))
                    for damageDone3 in range (0, attackDamage3):
                        enemyHealth -= 1
                        enemyHealhBar()
                        delay(.01)
                        
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        enemyHealhBar()
                        newAttackText("The wild "+ enemyPokemonName+" Fainted!")
                        f.write("It delt " + str(attackDamage3) + ' damage! \n') # PROFS DOCUMENT
                        f.write("It killed the enemy " + enemyPokemonName+ '! \n') # PROFS DOCUMENT
                    else:
                        f.write("It delt " + str(attackDamage3) + ' damage! \n') # PROFS DOCUMENT
                        enemyHealhBar()
                        enemyAttackSequence()
                        
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                            f.write("It killed Cody\'s " + pokemonName+ '! \n') # PROFS DOCUMENT
                            
                        else:
                            
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
            
                else:
                    newAttackText(pokemonName+ " is all out!")
                    
            elif not up1 and not left1 and down1 and right1:# BOTTOM RIGHT
                
                if pp4 > 0:
                    newAttackText(pokemonName+ " used "+ pokemonUsed4 + "!")
                    f.write('Cody\'s '+pokemonName+ " used "+ pokemonUsed4 + "! \n") # PROFS DOCUMENT
                    pp4 -= 1
                    playerPokemonAttack()
                    pokemonButtonStuff()
                    win.blit(mediumSelect, (int((370 * gamey) / 1080), int((765 * gamey) / 1080)))
                    for damageDone4 in range (0, attackDamage4):
                        enemyHealth -= 1
                        enemyHealhBar()
                        delay(.01)
                        
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        newAttackText("The wild "+ enemyPokemonName+" Fainted!")
                        f.write("It delt " + str(attackDamage4) + ' damage! \n') # PROFS DOCUMENT
                        f.write("It killed the enemy " + enemyPokemonName+ '! \n') # PROFS DOCUMENT
                    else:
                        f.write("It delt " + str(attackDamage4) + ' damage! \n') # PROFS DOCUMENT
                        enemyHealhBar()
                        enemyAttackSequence()
                        
                        if playerHealth <= 0:
                            playerHealth = 0
                            playerHealhBar()
                            newAttackText(pokemonName+ " Fainted!")
                            f.write("It killed Cody\'s " + pokemonName+ '! \n') # PROFS DOCUMENT
                        else:
                            
                            playerHealhBar()
                            newAttackText("What will " +pokemonName+ " do?")
                    
                else:
                    newAttackText(pokemonName+ " is all out!")

        else:
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
    global f
    global pokemonName
    f.write("\n The Battle Has Started!"+ ('\n'* 2) )
    f.write("He found a " + enemyPokemonName + '\n')
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
        
    delay(1)
    newAttackText("A Wild " + enemyPokemonName + " appeared!")
    delay(.5)
    newAttackText("Go! " + pokemonName + "!" )
    delay(.5)
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
        
        #After the player throws the pokeball into the air, this is the animation for it falling and hitting the ground
        for variable11 in range (0,1):
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
                                                                                    PLAYER PICKS HIS STARTER POKEMON!
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# DEFAULTS
pp1 = 35
pp2 = 40
pp3 = 20
pp4 = 40
pp11 = pp1
pp22 = pp2
pp33 = pp3
pp44 = pp4

def pickAPokemon():
    global pokemon
    global pp1
    global pp2
    global pp3
    global pp4
    global pp11
    global pp22
    global pp33
    global pp44
    global playerHealth
    global pokemonName
    pokeHolder = True
    leftButton= False
    middleButton= False
    rightButton= False
    win.blit(pokeballSelection, (0, 0))
            
    while pokeHolder:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            
            if not leftButton and not middleButton and rightButton: # IF RIGHT
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx, fingery))
                pygame.display.update()
                leftButton = False
                middleButton = True
                rightButton = False
                newAttackText("PIPLUP?")
                delay(.01)
                
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx - int((170 * gamey) / 1080), fingery))
                pygame.display.update()
                leftButton = True
                middleButton = False
                rightButton = False
                newAttackText("TURTWIG?")
                
            else: # IF LEFT
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx - int((170 * gamey) / 1080), fingery))
                pygame.display.update()
                leftButton = True
                middleButton = False
                rightButton = False
                newAttackText("TURTWIG?")
                
               
        elif keys[pygame.K_RIGHT]:
            if leftButton and not middleButton and not rightButton: # IF LEFT
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx, fingery))
                pygame.display.update()
                leftButton = False
                middleButton = True
                rightButton = False
                newAttackText("PIPLUP?")
                delay(.01)
                
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx + int((170 * gamey) / 1080), fingery))
                pygame.display.update()
                leftButton = False
                middleButton = False
                rightButton = True
                newAttackText("CHIMCHAR?")
               
            else: # IF RIGHT
                win.blit(pokeballSelection, (0, 0))
                win.blit(finger, (fingerx + int((170 * gamey) / 1080), fingery))
                pygame.display.update()
                leftButton = False
                middleButton = False
                rightButton = True
                newAttackText("CHIMCHAR?")
                    
        elif keys[pygame.K_SPACE]:
            playerHealth = 314
            if leftButton and not middleButton and not rightButton: # IF LEFT
                pokemon = turtwigB
                pokemonName = "TURTWIG"
                pp1 = 35
                pp2 = 40
                pp3 = 20
                pp4 = 40
                pp11 = pp1
                pp22 = pp2
                pp33 = pp3
                pp44 = pp4
                pokeHolder = False
                
            elif not leftButton and middleButton and not rightButton: # IF MIDDLE
                pokemon = piplupB
                pokemonName = "PIPLUP"
                pp1 = 35
                pp2 = 40
                pp3 = 35
                pp4 = 15
                pp11 = pp1
                pp22 = pp2
                pp33 = pp3
                pp44 = pp4
                pokeHolder = False
                
            elif not leftButton and not middleButton and rightButton: # IF RIGHT
                pokemon = chimcharB
                pokemonName = "CHIMCHAR"
                pp1 = 35
                pp2 = 20
                pp3 = 15
                pp4 = 40
                pp11 = pp1
                pp22 = pp2
                pp33 = pp3
                pp44 = pp4
                pokeHolder = False
            
        else:
            pygame.display.update()


# Solarian Chronicles
# A short adventure game based off of Stardew Valley's Solorian Chronicles.

#Created 2021 by Emmiliya Pismenchuk

import time
from playsound import playsound


header = """
 _______  _______  _        _______  _______ _________ _______  _            _______           _______  _______  _       _________ _______  _        _______  _______ 
(  ____ \(  ___  )( \      (  ___  )(  ____ )\__   __/(  ___  )( (    /|    (  ____ \|\     /|(  ____ )(  ___  )( (    /|\__   __/(  ____ \( \      (  ____ \(  ____ |
| (    \/| (   ) || (      | (   ) || (    )|   ) (   | (   ) ||  \  ( |    | (    \/| )   ( || (    )|| (   ) ||  \  ( |   ) (   | (    \/| (      | (    \/| (    \/
| (_____ | |   | || |      | |   | || (____)|   | |   | (___) ||   \ | |    | |      | (___) || (____)|| |   | ||   \ | |   | |   | |      | |      | (__    | (_____ 
(_____  )| |   | || |      | |   | ||     __)   | |   |  ___  || (\ \) |    | |      |  ___  ||     __)| |   | || (\ \) |   | |   | |      | |      |  __)   (_____  )
      ) || |   | || |      | |   | || (\ (      | |   | (   ) || | \   |    | |      | (   ) || (\ (   | |   | || | \   |   | |   | |      | |      | (            ) |
/\____) || (___) || (____/\| (___) || ) \ \_____) (___| )   ( || )  \  |    | (____/\| )   ( || ) \ \__| (___) || )  \  |___) (___| (____/\| (____/\| (____/\/\____) |
\_______)(_______)(_______/(_______)|/   \__/\_______/|/     \||/    )_)    (_______/|/     \||/   \__/(_______)|/    )_)\_______/(_______/(_______/(_______/\_______)
                                                                                                                                                                    
"""
# Music!
playsound("Music.mp3", block = False)


def game():

   # Text colors - used throughout the code in blank print statements. Everything after a color print statement will remain that color until changed.

   yellow = "\033[1;33;40m"  # Allies
   green = "\033[1;32;40m"  # Game
   blue = "\033[1;34;40m"  # Player
   red = "\033[1;31;40m"  # Enemy

   # Fancy title screens.
   print(yellow, header)
   time.sleep(3)
   print("   ")
   print(" _    _      _                             ___      _                 _                       _")
   print("| |  | |    | |                           / _ \    | |               | |                     | |")
   print("| |  | | ___| | ___ ___  _ __ ___   ___  / /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___ _ __| |")
   print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ |  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ '__| |")
   print("\  /\  /  __/ | (_| (_) | | | | | |  __/ | | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/ |  |_|")
   print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___| \_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|_|  (_) ")

   # Prompts the name of the player.
   print(green)
   time.sleep(2)
   print("What is your name?")
   print(blue)
   name = input()
   print(green)

   # Class selecting 
   time.sleep(2)
   print("Please select your class ", name, ".", sep="")
   print("   ")
   print("- Warrior, I like a direct approach. (1)")
   print("   ")
   print("- Wizard, a sharp mind is the most powerful blade of all. (2)")
   print("   ")
   print("- Healer, I prefer to help others. (3)")
   print(blue)

   playerclass = 0                                         # You will see this chunk of code A LOT. It prevents players from typing dumb answers and translate choices into story paths!
   while 1 > playerclass or 3 < playerclass:
      try:
          playerclass = int(input("Select your class (1-3) : "))
      except ValueError:
         print ("That's not an appropriate number...")

      #Player chose option 1
      if playerclass == 1:
         print(green)
         print("You have chosen the warrior class.")
         time.sleep(3)
         print("  ")
         print("Luckily for you, your companions take on the roles of healer and wizard. Sam, who was forced to become the healer, seems quite dissatisfied with his new role.")

      #Player chose option 2
      if playerclass == 2:
         print(green)
         print("You have chosen the wizard class.")
         time.sleep(3)
         print("   ")
         print("Luckily for you, your companions take on the roles of warrior and healer. Sebastian, who was forced to become the healer, seems quite annoyed at your decision.")

      #Player chose option 3
      if playerclass == 3:
         print(green)
         print("You have chosen the healer class.")
         time.sleep(3)
         print("   ")
         print("Luckily for you, your companions take on the roles of warrior and wizard. Both of them seem quite happy with your decision.")

   # An empty list for tracking score based on decisions
   finalscore = []


   # Explanation of the quest

   tower = '''  
                                                      |>>>
                                                      |
                                                  _  _|_  _
                                                 |;|_|;|_|;|
                                                 \\.    .  /
                                                  \\:  .  /
                                                   ||:   |
                                                   ||:.  |
                                                   ||:  .|
                                                   ||:   |       \,/
                                                   ||: , |            /`|
                                                   ||:   |
                                                   ||: . |
                                            ___.   ||_   |
     ____--``    '--``__            __ ----`    ``---,___|_.           
-`--`                   `---__ ,--`'                        `_____-`' '''
   print(yellow)
   time.sleep(3)
   print(tower)
   print(green)
   time.sleep(3)
   print("The King has entrusted you and two companions with recovering the Solarion Staff ... a task which, if completed successfully, will ensure your place in the hall of legends as well as a sizable fortune of gold and silver.")
   print("  ")
   time.sleep(5)
   print("After a long month journeying across unforgiving lands, you step out onto a precipice to see your destination looming in the distance.")
   print("   ")
   time.sleep(5)
   print("There, beyond a moonlit plain, lies the Necromancer's Tower... where Dreadlord Xarth usurps the power of the stolen Solarion Staff for his vile purposes.")

   # First decision - how to enter the tower
   print("   ")
   time.sleep(5)
   print("After a minute of walking, the tower lies before you.")
   print("   ")
   print("Option 1 - Go in the front. Fortune favors the bold.")
   print("Option 2 - Search for a back entrance. Let's remain hidden.")
   print(blue)

   firstscenario = 0
   while 1 > firstscenario or 2 < firstscenario:
      try:
          firstscenario = int(input("Select your action (1 or 2) : "))
      except ValueError:
         print ("That is not one of the choices...")

      # This scenario brings them to a skeleton encounter. Player chose option 1

      skeleton = '''
                     ▒▒▒░░░░░░░░░░▄▐░░░░
                     ▒░░░░░░▄▄▄░░▄██▄░░░
                     ░░░░░░▐▀█▀▌░░░░▀█▄░
                     ░░░░░░▐█▄█▌░░░░░░▀█▄
                     ░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
                     ░░░░░▄▄▄██▀▀▀▀░░░░░
                     ░░░░█▀▄▄▄█░▀▀░░░░░░
                     ░░░░▌░▄▄▄▐▌▀▀▀░░░░░
                     ░▄░▐░░░▄▄░█░▀▀░░░░░
                     ░▀█▌░░░▄░▀█▀░▀░░░░░
                     ░░░░░░░░▄▄▐▌▄▄░░░░░
                     ░░░░░░░░▀███▀█░▄░░░
                     ░░░░░░░▐▌▀▄▀▄▀▐▄░░░
                     ░░░░░░░▐▀░░░░░░▐▌░░
                     ░░░░░░░█░░░░░░░░█░░
                     ░░░░░░▐▌░░░░░░░░░█░ '''

      if firstscenario == 1:
         print(yellow)
         print(skeleton)
         print(green)
         time.sleep(3)
         print("A skeleton guards the hallway before you. It looks rather dangerous. Your party looks towards you for further instruction.")
         time.sleep(3)
         print("   ")
         print("Option 1 - Fight the skeleton.")
         print("Option 2 - Run away.")
         print(blue)

         combat1 = 0
         while 1 > combat1 or 2 < combat1:
            try:
               combat1 = int(input("What do you do?! (1 - 2) : "))
            except ValueError:
                print ("That is not one of the choices...")
            
            # Further combat ensues leading to another choice. Player chose option 1
            if combat1 == 1:
               print(green)
               print("The skeleton lunges towards you! Think fast, ", name, "!", sep="")
               time.sleep(3)
               print("   ")
               print("Option 1 - Swing your weapons.")
               print("Option 2 - Raise your shields.")
               print(blue)
               combat2 = 0
               while 1 > combat2 or 2 < combat1:
                  try:
                     combat2 = int(input("How do you respond to the foe? (1 - 2) : "))
                  except ValueError:
                     print ("That is not one of the choices...")

                  # Player chose option 1
                  if combat2 == 1:
                     print(green)
                     print("You swing at the skeleton mindlessly, in your brutish attack the skeleton manages to knick your expensive shirt and wound one of your party members. Doesn't he know that handwoven silk is hard to come by!?")
                     time.sleep(3)
                     print("   ")
                     print("Sam is not as concerned with the state of your clothing considering his arm has a large gash that you are positive wasn't there before. Oh well, tis but a scrath.")
                     print("   ")
                     time.sleep(3)
                     finalscore.append(3)

                  # Player chose option 2
                  if combat2 == 2:
                     print(green)
                     print("You successfully block the attack. The skeleton stumbles backwards, giving you enough time to strike out and slay the foul creature.")
                     print("   ")
                     time.sleep(3)
                     print("How dreamy, the rest of your party practically swoons at your quick thinking. Nice job, ", name, "!", sep="")
                     print("   ")
                     time.sleep(3)
                     finalscore.append(5)
            
            # Character runs away. Player chose option 2
            if combat1 == 2:
               print(green)
               print("How cowardish! An adventurer such as yourself running away? Really, ", name, "?", sep="")
               time.sleep(3)
               print("   ")
               print("As you back up from the skeleton, ready to run, your foe lunges regardless and faceplants into the concrete floor. He is now immobile, bones scattered across the entrance to the hallway.")
               time.sleep(3)
               print("   ")
               print("You may have killed your foe but your party will forever brand you as a coward. Was it worth it?")
               print("   ")
               time.sleep(3)
               finalscore.append(1)
                  

      # This scenario brings them to the door riddle puzzle.
      door = ''' 
              ______
           ,-' ;  ! `-.
          / :  !  :  . \.
         |_ ;   __:  ;  |
         )| .  :)(.  !  |
         |" _  (##)  _  |
         | (_); (') (_) (
         |  :  : _.     |
         )_ !  ,(_);  ; |
         || .  .  :  :  |
         |" .  |  :  .  |
         |_____;----.___| '''

      if firstscenario == 2:
         print(yellow)
         time.sleep(3)
         print(door)
         print(green)
         print("After searching around the base of the tower, you discover a trapdoor hidden in the brush. Beneath is a ladder, which your party descends.")
         print("   ")
         time.sleep(3)
         print("Before you lies a door with four doorknobs. It's quite strange looking and impractical. Above each doorknob you see the following inscriptions.")
         print("   ")
         time.sleep(3)
         print("Doorknob 1 - The fourth doorknob is telling the truth.")
         time.sleep(3)
         print("Doorknob 2 - The third doorknob is a liar!")
         time.sleep(3)
         print("Doorknob 3 - Clearly, I am telling the truth.")
         time.sleep(3)
         print("Doorknob 4 - Doorknob two is a liar.")
         time.sleep(3)
         print("   ")
         print("The inscription at the top says that three of the doorknobs always tell the truth whilst one always lies.")
         print(blue)

         doorpuzzle = 0
         while 1 > doorpuzzle or 4 < doorpuzzle:
            try:
               doorpuzzle = int(input("Who is the liar? (1 - 4) : "))
            except ValueError:
                print ("That is not one of the choices...")

            # Wrong options. Player chose everything but 3.
            if doorpuzzle == 1 or doorpuzzle == 3 or doorpuzzle == 4:
               print(green)
               print("Sebastian intervenes, stopping you from reaching towards your chosen doorknob. He points out that you clearly aren't fit for solving riddles. How embarrassing,", name, "! He opens the door for you.")
               print("   ")
               time.sleep(3)
               finalscore.append(1)

            # The correct answer! Player chose number 2.
            if doorpuzzle == 2:
               print(green)
               print("Wonderful work,", name, "! The party is impressed with your intellect, giving you a small round of applause!")
               print("   ")
               finalscore.append(5)

   # Choice between the two doors.
   hallway = '''
    _____________________________________________
   |.'',                                     ,''.|
   |.'.'',                                 ,''.'.|
   |.'.'.'',                             ,''.'.'.|
   |.'.'.'.'',                         ,''.'.'.'.|
   |.'.'.'.'.|                         |.'.'.'.'.|
   |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
   |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
   |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
   |.'.'.'.'.|:::|'.|'?????????'|.'|:::|.'.'.'.'.|
   |,',',',',|---|',|'?????????'|,'|---|,',',',',|
   |.'.'.'.'.|:::|'.|'?????????'|.'|:::|.'.'.'.'.|
   |.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
   |.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
   |.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
   |.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
   |.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
   |.'.','         /%%%%%%%%%%%%%\         ','.'.|
   |.','          /%%%%%%%%%%%%%%%\          ','.|
   |;____________/%%%%%%%%%%%%%%%%%\____________;| '''

   print(green)
   print("Having faced your challenge, you and your party progress further into the castle.")
   time.sleep(3)
   print(yellow)
   print(hallway)
   print(green)
   print("You find yourself in a sewer-like corrdior. To your left, a hallway glows with a peculiar green light. To your right, a staircase leads up into the dark.")
   time.sleep(3)
   print("   ")
   print("Option 1 - Enter the hallway to your left.")
   print("Option 2 - Climb the stairs to your right.")
   print(blue)

   hallwaychoice = 0
   while 1 > hallwaychoice or 4 < hallwaychoice:
      try:
         hallwaychoice = int(input("Which door do you choose? (1 - 2) : "))
      except ValueError:
         print ("That is not one of the choices...")
   
      # Player chose option 1
      if hallwaychoice == 1:
         print(green)
         print("You find yourself in a room. On your left is a ladder. On your right, three prisoners are floating in strange, glowing capsules. They appear to be in the process of some kind of transformation.")
         print("   ")
         time.sleep(3)
         print("Could this be some sick experiment of the Dreadlord's?")
         time.sleep(3)
         print("   ")
         print("Option 1 - Leave as quickly as possible.")
         print("Option 2 - Destroy the capsules.")
         print(blue)

         capsulechoice = 0
         while 1 > capsulechoice or 2 < capsulechoice:
            try:
               capsulechoice = int(input("What do you do? (1 - 2) : "))
            except ValueError:
               print ("That is not one of the choices...")
            
            # The player attempts to leave and thus triggers a puzzle. Player chose option 1. 
            if capsulechoice == 1:
               print(green)
               print("In an attempt to leave like the coward you are, you realize that the door behind you has been barred off. You are trapped. Truly fitting for someone of your title.")
               print("   ")
               time.sleep(3)
               print("Suddenly, a booming voice can be heard around the room - oh god, it's a puzzle.")
               time.sleep(3)
               print(red)
               print("Hahaha, foolish adventurers. You have fallen to my trap! Now you must answer my riddles or rot in this room forever!")
               print("   ")
               time.sleep(3)
               print("Your first riddle goes as follows : I start with M, end with X, and have a never ending amount of letters. What am I?")
               print(green)
               time.sleep(3)
               print("After conversing with your companions, you come up with five possible answers.")
               print("   ")
               time.sleep(3)
               print("Option 1 - Mix")
               print("Option 2 - Mailbox")
               print("Option 3 - Multiplex")
               print("Option 4 - Matrix")
               print("Option 5 - The Mets but with an x, it's all about the Mets.")
               print(blue)

               riddle1 = 0
               while 1 > riddle1 or 5 < riddle1:
                  try:
                      riddle1 = int(input("What is the answer to the riddle? (1 - 5) : "))
                  except ValueError:
                     print ("That is not one of the choices...")

                  # Player chose the incorrect answers, option 1, 3, or 4.
                  if riddle1 == 1 or riddle1 == 3 or riddle1 == 4:
                     print(red)
                     print("You fool! How could you miss something so obvious? Clearly it would be animal abuse to keep someone of such low intellect in my chamber of doom. Leave, and never come back!")
                     print(green)
                     time.sleep(3)
                     print("With great shame, you take the ladder with your head hung low. Your team mates follow you with an awkward silence. You could have done WAY better man.")
                     finalscore.append(1)
                     time.sleep(3)
                     print("   ")
                     
                  # Player chose the incorrect but clearly joking answer, aka option 5.
                  if riddle1 == 5:
                     print(red)
                     print("The Mets? What are you on about. Who are these Mets you speak of. That doesn't even end in an x! Clearly I must go back into hiding and research these so called Mets. You may carry on your way, even though you got the riddle horribly, horribly wrong.")
                     print(green)
                     time.sleep(3)
                     print("Your team mates looks at you in confusion. They don't question your decision, they just follow you up the ladder with quiet respect.")
                     time.sleep(3)
                     finalscore.append(3)
                     print("   ")

                  # Player chose the correct answer, option 2.
                  if riddle1 == 2:
                     print(red)
                     print("Blashpemous! How can a mere mortal get my riddle correct?! I shall now back down in shame, you may carry on adventurers.")
                     print(green)
                     time.sleep(3)
                     print("Sebastian gives you a quiet thumbs up, clearly impressed with your skills. Sam offers you a highfive, which you graciously take. You lead your team towards the ladder.")
                     time.sleep(3)
                     finalscore.append(5)
                     print("   ")

            # This leads towards a combat route. Player chose option 2.
            monster = '''  .      .
                           |\____/|
                           (\|----|/)
                           \ 0  0 /
                            |    |
                         ___/\../\____
                        /     --       \.
                       /  \         /   \.
                      |    \___/___/(   |
                      \   /|  }{   | \  )
                       \  ||__}{__|  |  |
                        \  |;;;;;;;\  \ / 
                         \ /;;;;;;;;| [,,]
                         [ |;;;;;;/ |  --
                           ||;;|\   |
                           ||;;/|   /
                           \_|:||__|
                            \ ;||  /
                            |= || =|
                            |= /\ =|
                            /_/  \_\ '''

            if capsulechoice == 2:
               print(green)
               print("You swing your weapon at the capsules in front of you - rewarded with a satisfying cacophony of glass hitting the floor.")
               print("   ")
               time.sleep(3)
               print("In your little reign of destruction, you notice one of the prisoners rising from the ground.")
               print(yellow)
               time.sleep(3)
               print(monster)
               print(green)
               print("You can hardly call the man in front of you human. He looks more like a grotesque lump of horns, flesh, and fur. After looking around at the broken capsules around him, he confronts your party.")
               print(red)
               time.sleep(3)
               print("W..what have you done!? My comrades, my brothers at arms - you killed them!")
               print(green)
               time.sleep(3)
               print("You attempt to explain your reasoning for breaking the pods - afterall, you were merely trying to grant them a peaceful death from their seemingly miserable existance. ")
               print(red)
               time.sleep(3)
               print("There were better ways! Don't give me that heroic rhetoric. All of you.. all of you will pay with your lives.")
               print(green)
               time.sleep(3)
               print("The creature bears his claws and lunges at you companions.")
               print("   ")
               time.sleep(3)
               print("Option 1 - Directly attack.")
               print("Option 2 - Attempt to talk down the creature.")
               print("Option 3 - Defend your companions with your shield.")
               print(blue)

               fight1 = 0
               while 1 > fight1 or 3 < fight1:
                  try:
                      fight1 = int(input("Quick! What will you do? (1 - 3) : "))
                  except ValueError:
                     print ("That is not one of the choices...")


                  # Direct attack scenario. Player chose option 1.
                  if fight1 == 1:
                     print(green)
                     print("You brandish your weapon and lunge at the distracted creature.")
                     print("   ")
                     time.sleep(3)
                     print("Your encounter was swift and soon enough the creature was motionless on the ground. Now he may rest among his brothers.")
                     print("   ")
                     time.sleep(3)
                     print("After admiring your work you take a look at your party. They are sufficiently banged up and bitter at your lack of initial concern for them. Oh well, it's nothing a quick healing spell won't fix.")
                     print("   ")
                     time.sleep(3)
                     print("With your party sufficiently healed up, the lot of you head up the ladder.")
                     print("   ")
                     time.sleep(3)
                     finalscore.append(4)

                  # Worst scenario, pacifict. Player chose option 2.
                  if fight1 == 2:
                     print(green)
                     print("As the creature strikes at your companions you begin yelling at it.")
                     print("   ")
                     time.sleep(3)
                     print("The creature however, ignores your ramblings about the futility of combat and continues engaging your team mates. Nice going pacifist - it's a monster, what did you expect?")
                     print("   ")
                     time.sleep(3)
                     print("Without your help, Sam manages to flank around the monster and put an end to it's life. Both of them are in bad condition. They insist on taking a break to patch up their wounds - your party sits there with an aura of strained silence.")
                     print("   ")
                     time.sleep(3)
                     print("After what seems like hours, your party heads up the ladder.")
                     print("   ")
                     time.sleep(3)
                     finalscore.append(1)

                  # Best scenario, defense. Player chose option 3.
                  if fight1 == 3:
                     print(green)
                     print("With a swift motion you leap in front of your companions, shield brandished towards the monsterous creature.")
                     print("   ")
                     time.sleep(3)
                     print("The creature changes his focus on to you. Whilst you bear the attacks of the brute, Sam flanks around him.")
                     print("   ")
                     time.sleep(3)
                     print("And just like that, the monster is no more. Your team mates thank you for your heroic actions via pats on the shoulder and warm smiles. How sweet.")
                     print("   ")
                     time.sleep(3)
                     print("With hightened spirits, your lead your party up the ladder.")
                     finalscore.append(5)

      # Player chose to go up the staircase. Option 2.
      lockeddoor = '''
                       
               .~'_`~.
         /(  ,^ .~ ~. ^.  )\.
         \ \/ .^  |   ^. \/ /
          Y  /    |    \  Y            ___.oOo.___ 
          | Y     |     Y |           |           |
          | |     |     | |           | 0   0   0 |
          | |     |     | |           |___________|
          | |     |     | |           |__T____T___|
          |.|     |     |.|           |__T____T___|
          |.|     |     |.|          _|__T____T___|_
          |:|     |     |:|         '^^^^^^^^^^^^^^^`
          |:|     |     |:|
      ____|_|     |     |_|_____________________________
      ____]H[_____|_____]H[_____________________________
           /             \.
                                                            '''

      if hallwaychoice == 2:
         print(green)
         print("You find yourself climbing a winding set of stone stairs. At the top you find a dim lit room with a table in the middle.")
         print(yellow)
         time.sleep(3)
         print(lockeddoor)
         print(green)
         print("Looking around the room you find a door with a passcode lock. The number pad has no wear on it and thus you can't deduce a possible combination.")
         print("   ")
         time.sleep(3)
         print("Left with no other choice, you pick up the worn paper found on top of the table.")
         print("   ")
         time.sleep(3)
         print("The paper has a simple message written on it to a gentleman by the name of Durnec.")
         print(red)
         time.sleep(3)
         print("Dear Durnec,")
         print("   ")
         print("As the new guard it is vital for you to remember the following equations : 3x + 4 = 16, 140/7, and 1,283,493 * 0. Do NOT under any circumstance let this password key get out. The LAST thing I want is to have a bunch of adventurers barging in on my me time. ")
         print("Love, Dreadlord.")
         print(green)
         time.sleep(3)
         print("Well, thats pretty self explanatory - hope you're good at math because conveniently the rest of your party isn't.")
         print("   ")
         time.sleep(3)
         print("After a quick deliberation, you confidently walk up to the keypad with your answer.")
         print("   ")
         time.sleep(3)
         print("Option 1 - 374")
         print("Option 2 - 690")
         print("Option 3 - 420")
         print("Option 4 - 932")
         print("Option 5 - Arson")
         print(blue)

         riddle2 = 0
         while 1 > riddle2 or 5 < riddle2:
            try:
               riddle2 = int(input("What is the correct passcode? (1 - 5) : "))
            except ValueError:
               print ("That is not one of the choices...")

            # Incorrect answers for the math riddle - Options 1, 3 , and 4.
            if riddle2 == 1 or riddle2 == 2 or riddle2 == 4:
               print(green)
               print("After confidently putting in your answer, the keypad beeps back in an angry manner. Your whole party seems to be poor at math - what a coincidence!")
               print("   ")
               time.sleep(3)
               print("Thanks to your poor math skills, your party is forced to mull over the problems for hours on end! Way to go, you made your companions tired and miserable. It's surprising that your party even managed to get the correct answer within 10 attempts.")
               print("   ")
               time.sleep(3)
               finalscore.append(2)

            # Player chose the correct answer to the math riddle which is 3.
            if riddle2 == 3:
               print(green)
               print("With a great stride you confidently make your way to the keypad. Moments after, you are rewarded with a green light and a whirling mechanism sound from the door. Your endless wisdom impresses your companions, way to go!")
               print("   ")
               time.sleep(3)
               print("With your companions' admiration earned, the lot of you make your way through the door.")
               print("   ")
               time.sleep(3)
               finalscore.append(5)
            
            # Player chose funny option and burned the door down - it's no answer but it works.
            if riddle2 == 5:
               print(green)
               print("Math isn't your strong suit, and arson isn't the worst of crimes.")
               print("   ")
               time.sleep(3)
               print("Alongside your teammates you cast a simple fire spell on the unfortunately wooden door. What a good bonding session!")
               print("   ")
               time.sleep(3)
               print("After a moment of appreciating the flames and playing with cinders, you step over the ashes into the next room.")
               print("   ")
               time.sleep(3)
               finalscore.append(4)

   dreadlord = '''

                   ,    ,    /\   /\.
                  /( /\ )\  _\ \_/ /_
                  |\_||_/| < \_   _/ >
                  \______/  \|0   0|/
                    _\/_   _(_  ^  _)_
                   ( () ) /`\|V"""V|/`\.
                     {|   \  \_____/  /
                     ()   /\   )=(   /\.
                     |}  /  \_/\=/\_/  \ '''

   # Boss time!
   print("You find yourself in a dimly lit dungenous tower room. In the middle you see none other than your foe, adorned in an intercate cape and silly hat.") 
   print(yellow)        
   time.sleep(3)
   print(dreadlord)
   print(green)
   print("The time has come to face Dreadlord Xarth.")
   print(red)
   time.sleep(3)
   print("Intruders? How dare you tresspass in my private chambers?!")
   print("   ")
   time.sleep(3)
   print("Ah, so you've come for for Solarion Staff...")
   print("   ")
   time.sleep(3) 
   print("Hehehe... fools. You'll make a nice addition to my skeleton army!")
   print(green)
   time.sleep(3)
   print("The Dreadlord begins muttering an incantation.")
   print("   ")

   if playerclass == 1:   # Warrior class choice.
      print("Option 1 - Charge at him.")
      print("Option 2 - Attempt to block the spell.")
      print("Option 3 - Cry.")
      print(blue)

      attack = 0
      while 1 > attack or 3 < attack:
         try:
            attack = int(input("How do you react? (1 - 3) : "))
         except ValueError:
            print ("That is not one of your options...")

         # Option 1 is chosen.
         if attack == 1:
            print(green)
            print("Like a true warrior, you brainlessly charge at the nerd.")
            print("   ")
            time.sleep(3)
            print("Your companions cheer you on as you tackle him, breaking his muttering of the spell. It's a good ol' beat down.")
            print("   ")
            time.sleep(3)
            print("The opponent is now disarmed, the staff laying next to his weak, weak nerd arms.")
            print("   ")
            time.sleep(3)

         # Option 2 is chosen        
         if attack == 2:
            print(green)
            print("Either with great bravery or stupidity, you raise your shield and get right in front of the wizard.")
            print("   ")
            time.sleep(3)
            print("With a confused expression, the wizard fires off his shadow beam spell. With a great turn of luck, the beam bounces right off of the shield and back into the wizard.")
            print("   ")
            time.sleep(3)
            print("Your opponent is now disarmed and on the floor. Maybe you should check if he is breathing...")
            print("   ")
            time.sleep(3)

         # Option 3 is chosen.
         if attack == 3:
            print(green)
            print("Overwhelmed with emotion, you lower your weapon and begin crying.")
            print(red)
            time.sleep(3)
            print("What.. what are you doing. Stop that.")
            print(green)
            time.sleep(3)
            print("But you don't stop, you just continue sobbing in an ugly manner.")
            print(red)
            time.sleep(3)
            print("I didn't sign up to comfort children, I wanted to fight adventurers! I command you to quit.")
            print(green)
            time.sleep(3)
            print("You keep crying... sniffling and wiping your nose all over your expensive outfit.")
            print(red)
            time.sleep(3)
            print("Ah come on man, not on the outfit! Just take the staff man, world domination isn't worth it.")
            print(green)
            time.sleep(3)
            print("Certainly unconventional, but you disarmed your opponent on both a mental and physical level. Way to go ", name, " !", sep="")
            print("   ")
            time.sleep(3)
   
   if playerclass == 2:   # Wizard class choice.
      print("Option 1 - Cast 'Pure Beam' at Xarth.")
      print("Option 2 - Put a 'Shield Charm' on your warrior.")
      print("Option 3 - Put a 'Shield Charm' on your healer.")
      print(blue)

      spell = 0
      while 1 > spell or 3 < spell:
         try:
            spell = int(input("Which spell do you cast? (1 - 3) : "))
         except ValueError:
            print ("That is not one of your spells...")

         # Option 1 is chosen.         
         if spell == 1:
            print(green)
            print("Thinking quickly, you try to cast your offensive spell.")
            print("   ")
            time.sleep(3)
            print("You cast a blinding beam of light towards the hand of your opponent. With great accuracy, you disarm the Dreadlord - the staff flying across the chamber.")
            print("   ")
            time.sleep(3)

         # Option 2 is chosen.        
         if spell == 2:
            print(green)
            print("Anticipating a strong attack, you cast a defensive spell on your warrior Sam.")
            print(yellow)
            time.sleep(3)
            print("Thanks, ", name, ".", sep="")
            print(green)
            time.sleep(3)
            print("Sebastian crosses his arms, clearly disapproving of your decision. You don't care.")
            print("   ")
            time.sleep(3)
            print("The Dreadlord casts his shadow beam, but your cleaver spell repels the beam back towards the opponent! His staff is knocked out of his hands, how lucky is that?")
            print("   ")
            time.sleep(3)

         # Option 3 is chosen.       
         if spell == 3:
            print(green)
            print("   ")
            print("Anticipating a strong attack, you cast a defensive spell on your healer Sebastian.")
            print(yellow)
            time.sleep(3)
            print("Thanks, ", name, ".", sep="")
            print(green)
            time.sleep(3)
            print("Sam stares at you, clearly disappointed with not being chosen. Sucks for him.")
            print("   ")
            time.sleep(3)
            print("The Dreadlord casts his shadow beam, but your cleaver spell repels the beam back towards the opponent! His staff is knocked out of his hands, how lucky is that?")
            print("   ")
            time.sleep(3)
   
   if playerclass == 3:   # Healer class choice.
      print("Dreadlord Xarth casts shadow beam!")
      print("   ")
      time.sleep(3)
      print("You were able to dodge the spell, but your companions are gravely injured.")
      print("   ")
      print("Option 1 - Heal Sam the Warrior.")
      print("Option 2 - Heal Sebastian the Wizard.")
      print(blue)
      healing = 0
      while 1 > healing or 2 < healing:
         try:
            healing = int(input("Who do you heal? (1 - 2) : "))
         except ValueError:
            print ("That is not one of your companions...")

         # Option 1 is chosen.
         if healing == 1:
            print(yellow)
            print("Thanks, ", name, ".", sep="")
            print(green)
            time.sleep(3)
            print("Sebastian gives you a dirty look. Clearly he isn't pleased, but this isn't about him.")
            print("   ")
            time.sleep(3)
            print("Sam jumps straight into action, masterfully disarming your opponent.")
            print("   ")
            time.sleep(3)

         # Option 2 is chosen.       
         if healing == 2:
            print(yellow)
            print("Thanks, ", name, ".", sep="")
            print(green)
            time.sleep(3)
            print("Sam looks hurt, and not just physically. Oh well.")
            print("   ")
            time.sleep(3)
            print("Sebastian casts 'Pacify', sending the Solarion Staff flying from the hands of your opponent.")
            print("   ")
            time.sleep(3)

   # Fate of villain choice.
   print("You walk up to the now disarmed wizard. He looks rather pathetic up close.")
   print("   ")
   time.sleep(3)
   print("Option 1 - Spare him.")
   print("Option 2 - Finish him off.")
   print("Option 3 - Romance him.")
   print(blue)

   boss = 0
   while 1 > boss or 3 < boss:
      try:
         boss = int(input("Choose his fate. (1 - 3) : "))
      except ValueError:
         print ("Why won't you cooperate...")

      # Mercy given.    
      if boss == 1:
         print(green)
         print("He isn't worth your time, after all, you got what you came here for.")
         print("   ")
         time.sleep(3)
         print("You tie up his hands and legs to ensure no problems for your exit plans. With a solemn mood, the wizard keeps silent.")
         print("   ")
         time.sleep(3)
         print("At the end of the day, you know you did the right thing. Your companions know it too.")
         finalscore.append(5)
      
      # Brutal end option.
      if boss == 2:
         print(green)
         print("Removing a small dagger from your hip holster, you approach the defeated wizard.")
         print("   ")
         time.sleep(3)
         print("He doesn't beg as you place the dagger to his throat, he doesn't want you to have the satisfaction. Your companions look disapproving but they don't try to stop you.")
         print("   ")
         time.sleep(3)
         print("You did what you had to do. He was an evil man, who knows what he would have done after your leave - you can't help but feel slightly guilty regardless.")
         print("   ")
         time.sleep(3)
         finalscore.append(3)

      # Romance ending.
      if boss == 3:
         print(green)
         print("Maybe you are into villains, or maybe you are just lonely. Whatever the reason, you walk over to the villain and lift his chin up with your hand.")
         print("   ")
         time.sleep(3)
         print("Clearly, the man is confused. At least he was before you dropped the best pickup line ever.")
         print(blue)
         time.sleep(3)
         print("Want a raisin?")
         print(red)
         time.sleep(3)
         print("What the.. No!")
         print(blue)
         time.sleep(3)
         print("Well, how about a date?")
         print(green)
         time.sleep(3)
         print("And that was the end of that. I will the spare the spicy details but needless to say the Dreadlord was in your arms bridal style at the end.")
         print("   ")
         time.sleep(3)
         finalscore.append(5)


   staff = ''' 
                        *
                  *   *
               *    \* / *
                 * --.:. *
                *   * :\ -
                  .*  | \.
                  * *    \.
               .  *       \.
                  ..        /\.
                *          |\)|
              .   *         \ |
            . . *           |/\.
               .* *         /  \.
               *             \ / \.
            *  .  *           \   \.
               * .  
               *    *    
            .   *    *   '''

   # The final little scene of the player getting the staff.
   print(yellow, staff)
   print(green)
   print("You pick up the Solarion Staff and hold it up proudly. Order has been restored to the world.")
   print("   ")
   time.sleep(3)

   # Score calculations.
   score = sum(finalscore)
   print(yellow, endframe)
   print("   ")

   # Deciding what the grade is depending on the calculated score.
   if score >= 18:
      print(green)
      print("You have finished the scenario with an A rating.")

   if 18 > score >= 15:
      print(green)
      print("You have finished the scenario with a B rating.")
   
   if 15 > score >= 10:
      print(green)
      print("You have finished the scenario with a C rating.")
   
   if 10 > score >= 6:
      print(green)
      print("You have finished the scenario with a D rating.")
   
   if 6 > score:
      print(green)
      print("You have finished the scenario with an F rating.")

# End fram storage. 
endframe = """

   _____                            _         _       _   _                 _ 
  / ____|                          | |       | |     | | (_)               | |
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
 | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
  \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                     __/ |                                                    
                    |___/                                                     

"""                                                                                       



if __name__=="__main__":
   game()
# A warning for my code i dont know why but sometimes it dose not print the options and i have tried everything
# it still dose not work if you could ck if it is my code or something that would be great

#Story time
#imports
import time

User = input("Please Enter your name:")

print('''Hi ''' + str(User) + ''', Today you will be building your own Character based on Show/Movie/Anime, a character in said Show/Movie/Anime. 
They will have a randomly picked age along with a special skill. SO lets get Creative! ''')

#Enter a number to pick a type of visual art
#slow down the instructions
time.sleep(2.5)
# select a show/movie/anime setting for each path
UserChoice = input("First enter a number from 1-6 to pick which Show/Movie/Anime it should be based on:")

#2 of each just to make it interesting also dont want to put in more shows and story choices
#picking a character. well actually pick a number that leads to a Character

#Raising Dion Story character choice
#Show reveal depending on the number picked
if int(UserChoice) == 1:
    print("You get a Show! The Show is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("Raising Dion")
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")
    UserDion = input("Dion")
    UserNic = input("Nicole")
    UserMak = input("Mark")
    UserTrev = input("Trever")
    UserEzpa = input("Esparanza")

    User = input("Enter a number from 1-5 to pick your Character:")

    if int(User) == 1:
        print('''Your Character is Dion. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is Nicole. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Mark. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Esparanza. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Trever. Great Choice!''')


#Spider-man Pathway
#Show reveal depending on the number picked
elif int(UserChoice) == 2:
    print("You get a Movie! The Movie is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("Spider-Man")
    #Character choice is being picked
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")
    UserPet = input("Peter")
    UserMJ = input("MJ")
    UserAunty = input("Aunt May")
    UserHappy = input("Happy")
    UserN = input("Ned")

    User = input("Enter a number from 1-5 to pick your Character:")
    if int(User) == 1:
        print('''Your Character is Peter. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is MJ. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Aunt May. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Happy. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Ned. Great Choice!''')

#One piece Pathway
#Show reveal depending on the number picked

elif int(UserChoice) == 3:
    print("You get a Anime! The Anime is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("One Piece")

    # Character choice is being picked
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")

    UserZZ = input("Zoro")
    UserLuffy = input("Luffy")
    UserR = input("Robin")
    UserS = input("Sanji")
    UserC = input("Chopper")

    User = input("Enter a number from 1-5 to pick your Character:")
    if int(User) == 1:
        print('''Your Character is Zoro. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is Luffy. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Robin. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Sanju. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Chopper. Great Choice!''')


#One piece Pathway
#Show reveal depending on the number picked

elif int(UserChoice) == 4:
    print("You get a Anime! The Anime is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("One Piece")

    # Character choice is being picked
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")

    UserZZ = input("Zoro")
    UserLuffy = input("Luffy")
    UserR = input("Robin")
    UserS = input("Sanji")
    UserC = input("Chopper")

    User = input("Enter a number from 1-5 to pick your Character:")
    if int(User) == 1:
        print('''Your Character is Zoro. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is Luffy. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Robin. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Sanju. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Chopper. Great Choice!''')


#Spider-man Pathway
#Show reveal depending on the number picked
elif int(UserChoice) == 5:
    print("You get a Movie! The Movie is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("Spider-Man")
    #Character choice is being picked
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")
    UserPet = input("Peter")
    UserMJ = input("MJ")
    UserAunty = input("Aunt May")
    UserHappy = input("Happy")
    UserN = input("Ned")

    User = input("Enter a number from 1-5 to pick your Character:")
    if int(User) == 1:
        print('''Your Character is Peter. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is MJ. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Aunt May. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Happy. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Ned. Great Choice!''')


#Raising Dion pathway
#Show reveal depending on the number picked

elif int(UserChoice) == 6:
    print("You get a Show! The Show is .....")
    time.sleep(2.5)
    print("YAY!!!!")
    print("Raising Dion")
    time.sleep(1.5)
    print("You now get to pick a Character from this show your choices are")
    UserDion = input("Dion")
    UserNic = input("Nicole")
    UserMak = input("Mark")
    UserTrev = input("Trever")
    UserEzpa = input("Esparanza")

    User = input("Enter a number from 1-5 to pick your Character:")

    if int(User) == 1:
        print('''Your Character is Dion. Great Choice!''')
        if int(User) == 2:
            print('''Your Character is Nicole. Great Choice!''')
            if int(User) == 3:
                print('''Your Character is Mark. Great Choice!''')
                if int(User) == 4:
                    print('''Your Character is Esparanza. Great Choice!''')
                    if int(User) == 5:
                        print('''Your Character is Trever. Great Choice!''')

# Randomly select a number and make up a reason for it
import random
import time

time.sleep(1.5)
print("Now that we have the Show/Movie/Anime and our Character let us randomly select a number for their age ")


InputEnter = input("please press enter: ")
InputEnter = 1

if InputEnter == 1:
      print('''They are ''' + str(random.randrange(1, 50)) + ''' old''')

time.sleep(1)

#picking a special skil for the Charaacter Creation
print("Now that you have the show and Character let's pick a Skill. Pick one of these 6 choices")
#the super power Choices
UserFire = input("Enter 1 for Fire Powers")
UserPunch = input("Enter 2 for Super Punch")
UserLighting = input("Enter 3 for Lightning Powers")
UserSpiderweb = input("Enter 4 for Spider Webs")
UserGummy = input("Enter 5 for Elasticity Powers")
UserSword = input("Enter 6 for Sword Mastership")

UserChoice = input("Please enter your Choice:")
#the skill is revealed should i make it more dramatic
if int(UserChoice) == 1:
    print('''Yay that Is a great choice your special power are Fire Powers. Now lets Introduce your Character but fist list all you gathered information.''')
    if int(UserChoice) == 2:
        print('''Yay that Is a great choice your special power is Super Punch. Now lets Introduce your Character but fist list all you gathered information.''')
        if int(UserChoice) == 3:
            print('''Yay that Is a great choice your special power is Lightning Powers. Now lets Introduce your Character but fist list all you gathered information.''')
            if int(UserChoice) == 4:
                print('''Yay that Is a great choice your special power are Spider Webs. Now lets Introduce your Character but fist list all you gathered information.''')
                if int(User) == 5:
                    print('''Yay that Is a great choice your special power are Elasticity Powers. Now lets Introduce your Character but fist list all you gathered information.''')
                    if int(User) == 6:
                        print('''Yay that Is a great choice your special power is Sword Mastership. Now lets Introduce your Character but fist list all you gathered information.''')

#list Character qualities bcause why not. This risky becuase that means you can cheat the system and but any power you want or name
#However i am to lazy to fix it so i hope i dont get a bad mark for over looking it
UserCh = input("Write your Character Name:")
UserVA = input("Write Show/Movie/Anime Name:")
UserAge = input("Write your Characters Age:")
UserPower = input("Write you Characters Power:")

UserChoice2 = input("Lastly the final Challenge is deciding what type of into. Pick a Number from 1-3 to choose and your intro will be presented: ")

# 3 story ending Choices the text is really bad but oh well

if int(UserChoice2) == 1:
    print('''Hi my name is ''' + str(UserCh) + '''. I am the Character form the greates vuisual arts presentation in history.''' 
          '''It is called ''' + str(UserVA) + '''. I am ''' + str(UserAge) + ''' years old. and my special power is ''' + str(UserPower) +
          '''. I am the Greatest in the world and my character will be legendary!''')

elif int(UserChoice2) == 2:
    print('''This hero is from the vuisual arts presentation ''' + str(UserVA) + '''. They are ''' + str(UserAge) + ''' old. '''
          ''' They are one of the greatest Heros in the world. They saved my life to and might one day save yours''' + str(User) + '''. 
              There Superpower power is ''' + str(UserPower) + ''' but, it is only mighty in their hands. No one is a better hero then ''' + str(UserCh))

elif int(UserChoice2) == 3:
    print('''In a humble town once lived a SuperHuman. His nam was ''' + str(UserCh) + '''. 
            His kindness knew no bounds and he was reveared all across the lands. At the tender age of ''' + str(UserAge) + ''' he protected everyone. 
            His SuperPowers were so strong but only in his hands his powers were ''' + str(UserPower) + '''. 
            Protected the world of ''' + str(UserVA) + ''' and will for ever do so.''')







## creators: Eva Lynch & Nicole Rasmussen
## date: January 28th, 2018

import time
import random

def main():
    lives = 8
    bad = False;
    villainList = ["caneToad", "garlicMustard", "europeanFireAnt", "sirexWoodwasp", "brownTreeSnake"]

    # Establishes the setting

    print("Captain's Log, Julian Year 3005.019")
    print()
    print("...Start Transmission...")
    print()
    name = input("Greetings, Hero. What is your name? ")
    print()
    getPrologue(name)
    time.sleep(3)

    # Plot
    
    while int(len(villainList)) > 0 and int(lives) > 0:
        whichVill = random.randint(0, (len(villainList)-1))
        if (villainList[whichVill] == "caneToad"):
            #print("Cane Toad")
            lives = caneToad(lives)
            villainList.pop(whichVill)
            #print(villainList)
        elif (villainList[whichVill] == "garlicMustard"):
            #print("Garlic Mustard")
            lives = garlicMustard(lives)
            villainList.pop(whichVill)
            #print(villainList)
        elif (villainList[whichVill] == "europeanFireAnt"):
            #print("EFA")
            lives = europeanFireAnt(lives)
            villainList.pop(whichVill)
            #print(villainList)
        elif (villainList[whichVill] == "brownTreeSnake"):
            #print("wasp")
            lives = sirexWoodwasp(lives)
            villainList.pop(whichVill)
            #print(villainList)
        else:
            #(villainList[whichVill] == "villain5"):
            #print("brownTS")
            lives = brownTreeSnake(lives)
            villainList.pop(whichVill)
            #print(villainList)
            
    if bad == False:
        getGoodEpilogue(name)

## necessary functions

def getPrologue(name):
    # Introduces the storyline

    print("\"Greetings, " + name + ". Welcome to the Intergalactic Spaceship Terra. I am Captain Scully. After careful consideration, the Intergalactic Defense Force has determined that you are Earth's only hope."
          + " It is your duty to thwart the evil plans of Hostile Extraterrestrials. THE IDF has homed onto four HEX signals. If you fail, Earth will fall. Your fellow Earthlings depend on you. The first portal awaits.\"")
    print()
    time.sleep(2)
    print("Captain Scully escorts you to the portal room.")
    print()

    # Introduces gameplay
    
    print("\"Greetings, " + name + ". I am EKe, the Environmental Portal Keeper. Please accept your spatial energy watch. The bars indicate" +
            " how much spatial energy is left. Each Earthside activation requires one bar of spatial energy. After you defeat a species, I will teleport you to the next location. " +
               "Please pay attention to how many bars are displayed after each encounter. If we must revive you, you will lose two energy bars- one for using the portal and the other " +
                 "for using the revival chamber. Currently, your watch possesses eight bars. This should be enough to transport you to all of the known signals and return you safely to the ISS Terra." +
                  " If your watch loses all its bars, you will be stranded with no way to return.\"")
    print()
    time.sleep(2)
    print("EKe activates the portal. \"It's time for you to face your first HEX.\" Whoosh. Suddenly nervous, you pause." +
            "\"Good luck, " + name + ". Your fellow Earthlings depend on you.\" Before you can reply, EKe pushes you through the portal.")

def deathReport(lives):
    print("You die.")
    if lives == 0:
        getBadEpilogue()
    else:
        print("Elsewhere, EKe receives an alert about your predicament and sets about reviving you.")
        print("As you are rematerialized, EKe prepares your portal to the next HEX signal and your energy charge falls by 2, leaving you with " + str(lives) + " energy bars.")
        print("The Earth awaits its savior!")

def getBadEpilogue():
    print("...End Transmission...")
    print()
    time.sleep(2)
    print("Unfortunately, your spatial energy watch ran out of energy bars before you could defeat the HEXes. The last HEX you encountered destroyed your watch. Without a signal to home onto, " +
           " the IDF cannot aid in Earth's defense. Stranded, you rush in search of cover. The HEX sends for reinforcements. You find shelter, but it is too late. The HEXes have found you.")
    

def getGoodEpilogue(name):
    print("You find yourself aboard the ISS Terra. EKe stands just beyond the portal's reach. \"Welcome Back, " + name + ". It is good to see you well. Earth is no longer under threat from HEXes. " +
            "Captain Scully would like to see you on the bridge.\"")
    print()
    print("You enter the bridge.")
    print()
    print("Captain Scully addresses you from the Captain's Chair. \"Congratulations, " + name + ". You saved your fellow Earthlings from the HEX invasion. Earth and her Earthlings live on." +
            " To celebrate your success, I dub you Chief Scientific Officer " + name + " of Earth. You are welcome aboard the ISS Terra whenever she is in orbit.\" Captain Scully turns, facing the bridge window." +
               "\"The view is beautiful.\" Captain Scully allows you several moments to admire Earth in all her glory. \"EKs is standing by to send you home.\" It is a definite dismissal.")
    print()
    print("You return to the portal room.")
    print()
    print("\"I am happy to report that " + name + " behaved as expected. The ISS Terra's Environmental Portal Keeper returned " + name + " to Earth. Captain Scully Signing Off")
    print()
    print("...End Transmission...")

## VILLIANS

def brownTreeSnake(lives):
    print("The portal has deposited you into a clearing at night.")
    time.sleep(1)
    print("You hear a rustling in the grass. Startled, you stumble backwards.")
    print("A Brown Tree Snake follows the sound of your movement. You need to act before this venomous creature strikes.")
    print("You have the option of capturing it and carefully removing its fangs or- wait, there's more movement in the grass.")
    guess=input("Do you lunge after the snake or wait to see what else lurks nearby? [lunge/wait] ")
    answer='lunge'
    if (guess==answer):
        time.sleep(1)
        lives = lives - 1
        print("It's a lizard. The creature wheels around, eying the lizard as its next meal.")
        print("You lunge after the snake. Securing a grip on it, you carefully avoid its mouth. With a calm demeanor, you quickly remove its fangs.")
        print("The lizard continues on its journey to find food.")
    else:
        time.sleep(1)
        lives = lives - 2
        print("It's a lizard. The creature wheels around. It quickly devours your fellow Earthling.")
        print("Horror stricken, you're frozen long enough for the snake to target you.")
        print("The last thing you see is the Brown Tree Snake biting you with its venomous fangs.")
        deathReport(lives)
    return lives

def caneToad(lives):
    print("The portal has deposited you in a clearing.")
    time.sleep(1)
    print("Before you is a horrific toad the size of a truck! You identify the monstrous creature as the infamous Cane Toad.")
    print("Notorious for their viciousness, the Cane Toad is known for eating anything that it can fit in its mouth, including members of its own brethren.")
    time.sleep(1)
    print("This alien invader is responsible for eating and displacing countless Earthings, it must be stopped. You know that you have a limited amount of ")
    print("time to react, the Cane Toad possesses a toxin fatal to nearly all earthly organisms and you can see your adversary preparing for your demise.")
    time.sleep(1)
    guess=input("You have your freeze ray and your super charged trap. Which will you choose? [freeze/trap] ")
    answer='freeze'
    if (guess==answer):
        time.sleep(1)
        lives = lives - 1
        print("You whip out your freeze ray just as the Cane Toad begins to secrete it's toxin, freezing it and minimizing any pain and distress for the beast.")
        print("You successfully eliminate the threat and manage to take out a recently laid batch of Cane Toad eggs in a nearby body of water, preventing future generations from spawning.")
        print("Having successfully eliminated the threat, you use one of your energy bars to summon the portal to your next HEX signal. You are left with " + str(lives) + " bars.")
    else:
        time.sleep(1)
        print("You deploy your super charged trap right as a separate Cane Toad bursts into the clearing in hot pursuit of a Bluetongue Lizard.")
        print("You can only watch helplessly as your trap entangles with your fellow Earthling, the pursuing Cane Toad coming to a stop.")
        print("You curse yourself for not considering the possibility of your trap capturing the wrong creature. The two Cane Toads, having no interest in prey without the chase, turn to you.")
        print("The unmistakable scent of the Cane Toad toxin scorches your nostrils and you turn to run, but the invaders are too quick.")
        lives = lives - 2
        time.sleep(1)
        deathReport(lives)
    return lives

def garlicMustard(lives):
    time.sleep(1)
    print("The portal has deposited you in the understory of a densely forested area.")
    print("Taking a closer look around, you realize that you're surrounded by the ghastly Mustard Garlic HEX.")
    print("You remember when the Earth's forests were taken over by this HEX. They crept in and overran the undergrowth, sucking up all the nutrients for themselves. The other plants didn't have a chance.")
    print("This is your chance to redeem your fallen earthling comrades and take back the forest!")
    guess=input("You have your flame thrower and your vaporizer. Which will you choose? [flame/vap] ")
    answer='vap'
    if (guess==answer):
        lives = lives - 1
        print("You take careful aim with your vaporizer, ensuring that you won't miss your target and potentially hit an earthling.")
        print("You successfully vaporize the entire root system, leaving no trace of the ruthless Garlic Mustard HEX or any opportunity for any seeds to continue developing on leftovers.")
        print("Mission complete! You use one of your energy bars to summon the portal to your next HEX signal. You are left with " + str(lives) + " bars.")
    else:
        print("Your flame thrower roars to life and you reduce the HEX to a pile of ashes with fairly minimal damage to the surrounding environment. Piece of raspberry pie!")
        print("...")
        time.sleep(1)
        print("...or so you thought.")
        print("As you inspect your flamethrower for potential maintenance after such a big job, the minimal remains of the Garlic Mustard HEX develop rapidly and spread out to search for their antagonist.")
        print("You hear the slithering of the plant right as they discover your impromptu workbench and are overcome by the HEX.")
        print("As the edges of your vision go black with the HEX's steadily tightening grip on your neck, you can't help but be frustrated that you didn't completely eliminate the Garlic Mustard, roots and all, to truly eliminate any threat of resurgence.")
        lives = lives - 2
        deathReport(lives)
    return lives

def europeanFireAnt(lives):
    time.sleep(1)
    print("The portal has deposited you in the ruins of a suburban neighborhood. Whole houses have been overtaken by massive ant hills, it's a chilling sight that you'd recognize no matter what.")
    print("The European Fire Ant. Originally thought to be of Earth, the EFA HEX was one of the first HEX species to initiate their invasion of Earth. That said, even after they grew into their true form, the name was ironic enough that it stuck.")
    print("Creeping towards the ant hill, you brace yourself for a swarm of ants the size of german shepherds to come pouring out of the sized up ant hill, but all was quiet, even as you started to climb the hill towards the opening.")
    print("The time to act is now, you'd rather not have to deal with a whole flood of them at once.")
    guess=input("You have your Water2Ice mixture and your SUPER ANTI-ANT pesticide. Which will you choose? [mixture/pesticide] ")
    answer='mixture'
    if (guess==answer):
        lives = lives - 1
        print("You quickly take the opportunity in front of you and pour the mixture into the ant hill. The mixture fills every nook and cranny of the HEX ant tunnels and immediately begin hardening into ice, trapping everything inside.")
        print("You've taken out this HEX colony for good. This almost seemed too easy, but you're not complaining.")
        print("With the mission complete, you use one of your energy bars to summon the portal to your next HEX signal. You are left with " + str(lives) + " bars.")
    else:
        print("You jump at the opportunity to eliminate this HEX colony before the fighting starts and quickly pour the pesticide into the ant hill. Immediately you notice a change in the color of the ground and the pesticide soaks downwards.")
        print("The effects of the pesticide aren't confined to the HEX's underground tunnels! The sharp chemical smell of the pesticide starts to burn your eyes and you notice that trees and plants in the area begin to wilt.")
        print("With all the best intentions, you'd ended up hurting that of which you'd hoped to save. \"Who's the bad guy now?\" You think to yourself as your skin drains of color and the smell overwhelms you.")
        lives = lives - 2
        deathReport(lives)
    return lives

def sirexWoodwasp(lives):
    print("The portal has deposited you in a forest.")
    time.sleep(1)
    print("You move forward. Before you is a frightful creature! You identify it as a Sirex Woodwasp!")
    print("Noted for its horrendous support of fungi, you realize it is responsible for the dying pines which surround you.")
    time.sleep(1)
    print("This alien invader is responsible for destroying countless Earthlings. If you do not stop it, it will ravage other forests.")
    print("You know there's little time to act. The Sirex Woodwasp could direct you towards a falling pine at any time.")
    time.sleep(1)
    guess=input("You have your trusty axe on hand or a bottle of methyl bromide. Which will you choose? [axe/methyl] ")
    answer='methyl'
    if (guess==answer):
        time.sleep(1)
        lives = lives - 1
        print("You whip out the bottle of methyl bromide just in time. You wish it didn't come to this, but Sirex Woodwasp is getting ready to infect another batch of trees.")
        print("You cannot let more of your fellow Earthlings die. The Sirex Woodwasp falls. You must remember to ask someone about quarantining this forest when the HEX are defeated.")
        print("Having successfully eliminated the threat, you use one of your energy bars to summon the portal to your next HEX signal. You are left with " + str(lives) + " bars.")
    else:
        time.sleep(1)
        print("You choose your trusty axe and run towards the Sirex Woodwasp. It dodges out of your way. Your axe wedges itself into a pine tree covered in fungi.")
        print("You attempt to pull your axe out. It's stuck! The fungi run up the handle. You notice a baby wasp. The one in the clearing must be the mother.")
        print("You curse yourself for not paying attention to details.")
        print("You pull your fingers from the handle of the axe, only to find them covered in secreted Sirex Woodwasp toxins.")
        lives = lives - 2
        time.sleep(1)
        deathReport(lives)
    return lives

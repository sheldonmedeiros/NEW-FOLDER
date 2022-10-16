name =input('Enter your name! ')
print(f'Greetings {name}! Welcome to your adventure! ')
start = input('Would you rather PLAY the game or DIE? ')
if start.lower() == 'play':
    print("Great! Let's play the game!" )
    setting = input('Want to go to the JUNGLE or DESERT? ')
else:
    print("Lame! Okay well you're dead now... ")
    quit(0)

if setting.lower() == 'jungle':
        print("Welcome to the Amazon! A great and mighty rainforest! You were with your tourguide and he heard a strange noise and went to invesitgate...")
        response = input("But he has been gone for hours... Do you FOLLOW him or WAIT? ")
        if response.lower() == 'follow':
            print("You follow in the direction that he went off to... ")
            inspection = input("You start walking down the path and you see that the roads splits in two... Do you take the LEFT or the RIGHT?")
            if inspection.lower() == "left":
                print("You take the muddy slopes down and see a river with a canoe... ")
                transport = input("Do you RIDE the canoe or keep on WALKING? ")
                if transport.lower() == "ride":
                    print("You take the canoe and start heading down the river.... As you are traveling you noitce the rapids are getting stronger.... You notice to late that there is a big dip and you go down the waterfall falling to your death.... YOU ARE DEAD!")
                elif transport.lower() == "walking":
                    print( "You do not get in the canoe and make your way donw the slops some more.... You hear bushes shake and you have a bad feeling that you are not alone... All of a sudden a jaguar jumps out of the trees and he mauls you to death.....YOU ARE DEAD!")
            elif inspection.lower() == "right":
                print("You follow down the the road and all of a sudden you hear a loud thud.... As you turn around there is a huge snake that strakes wraps you up and eats you whole... YOU ARE DEAD!")
        elif response.lower() == 'wait':
            print("You wait for another hour and he still has not come back! ")
            patience = input("You start to worry and don't know if he will ever be back..... Do you WAIT some more or INVESTIGATE? ")
            if patience.lower() == "wait":
                print("You wait even more and there is not much day light in the sky.")
                success = input("You are so worried that something bad might off happened to him but you keep waiting..... You are getting hungry.... Do you WAIT or LOOK for food? ")
                if success.lower() == "wait":
                    print("You agree to hang out a little more and as the sun starts to set almost losing hope the tour guide came back for you and you were able to survive the jungle making it out alive! YOU WIN.")
                elif success.lower() == "look":
                    print("You start to look for food that is near the camp grounds so you do not wonder off.. You notice some fruit that you are not to sure what it is... You eat the fruit and it is posinous and you slowly start to fade deeper and deeper into blac and finally it is your end...... YOU ARE DEAD!")
            elif patience.lower() == "investigate":
                print("You go off looking for the tour guide... with no luck you are now lost because you did not remember which way he went... As the days get longer you eventually cannot survive out in the wild and die to the natrual causes..... YOU ARE DEAD!")

        else:
            print("Don't cheat the system... You lose... ")
            quit()

elif setting.lower() == 'desert':
        print("Welcome to the Sahara desert! A great and hot land! You are on the hunt for the lost tombs of buried treasure and been out in the sun for a while... ")
        response = input("You see a merchant in the distance..... do you APPROCH or keep TRAVELING?  ")
        if response.lower() == 'approch':
            print("You cautionly approch the stranger who looks like he is in bad shape no food or water for days and he is holding on for his dear life... ")
            grateful = input("He thanks you for saving his life as you graciously gave him a but of your water and food. He asks what are you doing out here all by your self? Do you LIE or tell him the TRUTH? ")
            if grateful.lower() == "lie":
                print("You just give him a generic answer saying you are sight seeing and touring the plains..")
                robbed = input("As you tell him this he just noodes and notice you have a lot of stuff for just sight seeing... He pulls out a sword and holds it to your throat... He is robbing you for all of your stuff... Do you surrender or fight?")
                if robbed.lower() == "surrender":
                    print("You regretfully give him all your stuff and he leaves you in the desert to die... YOU ARE DEAD!")
                elif robbed.lower() == "fight":
                    print(" You act like you are giving him your stuff and then surprise him with a sneak attack knocking rthe sword to the floor.. as you guys tussel you are able to get a good choke on him.... But before he passes out he let's out a werid noise and passes out.")
                    decision = input("You won the fight and now wondering about the noise that he blurted out.... You try to shake it off but it is in the back of your head... Do you pack up everything and LEAVE as quickly as you can or INSPECT the stranger? ")
                    if decision.lower() == "leave":
                        print("Trusting your instincts you high tail it out of there and get as far as possible and are on the way home for that was too much action in one day to live to see another day. YOU WIN!")
                    elif decision.lower() == "inspect":
                        print(" You look at the graud to see if he has any valuables.. As you are doing this you hear footsteps from the east... As you get on the top of the dunes to have a better look there is a hurd of people racing to your area.. You try and flee but they are on horse back and they catch up to your camel.. They rob and tourte you and you die... YOU DIE!!!!")
            elif grateful.lower() == "Truth":
                print("You tell him that you are on the hunt for the lost treasure of the Sahara you heard about...")
                deception = input("As he hears your answer he says that he has heard of the tales but never was able to make it to the place... He asks if he acould accompany you on this journey.. Do you let him COME or NO? ")
                if deception.lower() == "come":
                    print("You allow him to come since the more the merrier and as you guys take off you find the temple that you were looking for. Inside as you try to access the temple the stranger called his people and they finished you off so that they can take the gold all for themselves... YOU ARE DEAD!")
                elif deception.lower() == "not":
                    print("You are hesiatant and tell him no. You want the money all for yourself and as you travel away and see the figure fade in the distance they followed right behind you... As you find the temple and do all the task and get to the final treasure the band of theives confrot you... As you try to fight out the man power is too strong and you are killed... YOU ARE DEAD!!")
        elif response.lower() == 'traveling':
            print("You high tail it out of there and leaving the figure as it disappers in the rear veiw as you travel further away... ")
            mirage = input("As you travel down the path you run out of water and are thristy... You see in the distance a body of water looking like an oasis... You do not know if it is you mind playing tricks on you... Do you GO to the oasis or keep on your TRAVELS? ")
            if mirage.lower() == "go":
                print("You are just so thristy that it has too be true.. So you make your way over and too your surprise it is an actually place...")
                choices = input("As you look around there is trees and shade and there is a big lake of water to drink from.. There is much to do you just get so excited.. What do you do first do you RELAX under the tress for a short nap, JUMP in the water and cool off and take a nice bath, or do you drink the water till your QUENCH is fulfilled? ")
                if choices.lower() == "relax":
                    print("You decide that you are more tired than thirsty and take a nap. As you are napping one of the coconuts fall from the trees and hits you pn the head. Never to wake up from the nap you are having... YOU ARE DEAD!")
                elif choices.lower() == "jump":
                    print("You get so excited that you run full sprint to the water jumping and feeling nice and refreshing on your body.. As you are cooling off you notice that you are getting itching and it is hurting to be in there. There is leeches that are all over your body and sucking you dry... You incorrectly remove a leech and the blood starts flowing out of you body uncontrollably.. You have mutiple leeches and you either let them stay or lose more blood.. YOu decide to remove them but lose too much blood passing out and never able to wake up again.... YOU ARE DEAD!!")
                elif choices.lower() == "quench":
                    print("You hop off your camel and go to drink the water and you quench yourself feeling good and refreshed... You notice that the water taste a little funky but that is it. You put more in your water bottle and decide it is time to move on. But then you start throwing up like crazy and losing fluids more and  more till you collaspe and die... YOU ARE DEAD!!!")
            elif mirage.lower() == "Travels":
                print("You do not want to get your hope up and you keep on the path because you eill not be fooled by the deserts trickery...")
                end = input("You continue you on your way and get to the temple. You are ready for the adventure but start getting dizzy... You shake it off and enter the temple... There is just an empty room in the temple and a treasure chest right on the pedstal.. Do you TAKE it or RETURN home to rest? ")
                if end.lower() == "take":
                    print(" You go foward in the tomb and reach out. heart is nbeating fast not know what to expect. As you remove it from the stand nothing happens. You look inside and there is the money and treasure and walk out with no problems.... YOU HAVE WON!!!")
                elif end.lower() == "return":
                    print("You are getting affect by the dizzness and the exhausten that you have abd want to leave but it is a trap and the wall closes down and traps you in the treasure room... As you wonder why knopw you are mortified bt the answer... On the wall it reeads if ye enter the room ye mnust take the chest others you seal you and the treasure down here for all eternity... YOU ARE DEAD!!!")
        else:
            print("Don/t cheat the system... You lose... ")
            quit()

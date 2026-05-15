import easygui
import sys 
#reusable msgbox function used alongside non wrapped msgbox functions to test if this function working
def usable(text):
    return easygui.msgbox(text)
#intro 

easygui.msgbox("hello dear player")
easygui.msgbox("""this is my first ever gui
programm using easygui frame work made for python""")
easygui.msgbox("this is an rpg character creator test i made for fun and to practice my skills")
easygui.msgbox("well hope you have fun testing my code")
#continue the demo

yes_no = easygui.choicebox(
    "start the demo?",
     choices=["yes", "no"]
)
#check and respong to the yes or no inputs

if yes_no =="yes":
    easygui.msgbox("thanks for testing my app keep in mind this is just a prototype")
    easygui.msgbox("made by 16 year old teenager living in morocco")
elif yes_no == "no":
    easygui.msgbox("well maybe at anoter time bye")
    sys.exit()
easygui.msgbox("welp click ok to start(at your own risk)")
#character name
name = easygui.enterbox("what is your characters name?")
easygui.msgbox(f"{name} huh?,pretty basic name but i wont judge")
#choosing a location
location = easygui.choicebox(
    "choose a starter spawn area",
    choices=["finland", "burundi", "georgia"]
)
#checking and responding to location inputs

if location == "finland":
    easygui.msgbox("ah yes,you would like to start off careful and easy")
elif location == "georgia":
    easygui.msgbox("you are a normal player and would like to have some difficulty")
elif location == "burundi":
    easygui.msgbox("bruh")
    easygui.msgbox("well looks like you are a masochist and you would like to torture yourself")
#clan picker and color picker

clan = easygui.enterbox("name your clan")
easygui.msgbox(f"{clan} is quite a name a shit one that is")
color = easygui.enterbox("enter a color for your clan")
easygui.msgbox(f"great,{color} is such a shit color")
#choosing difficulty
difficulty = easygui.choicebox(
    "pick difficulty",
    choices=["easy", "meduim", "hard", "ASIAN(very hard and not reccomended for non asians)"]
)
#checking and responding to diffuclty and how the location picked influences it

if difficulty == "easy":
    if location == "finland":
        easygui.msgbox("playing it very safe and easy i see easy difficulty plus finland is an easy start for beginners")
    elif location == "georgia":
        easygui.msgbox("a you chose an easy experience whit a tiny bit of challenge,georgia whit easy is a great start after tutorail")
    elif location == "burundi":
        easygui.msgbox("well it is below meduim difficulty but still a bit challenging to play burundi even whit easy")
elif difficulty == "meduim":
    if location == "finland":
        usable("finland whit meduim is still easy for beginners")
    elif location == "burundi":
        usable("now whit burundi in meduim difficulty we are getting into some serious stuff")
    elif location == "georgia":
        usable("meduim difficulty whit georgia is basiaclly the normal way to play")
elif difficulty == "hard":
    if location =="burundi":
        usable("bruh")
        usable("i mean just bruh")
    elif location == "finland":
        usable("finland whit hard is meduim if that makes sense idk i am too stupid")
    elif location == "georgia":
        usable("ah yes georgia whit hard difficulty, that is basiaclly what every georgian difficult is")
elif difficulty =="ASIAN(very hard and not reccomended for non asians)":
    usable("no matter the difficulty if asian is on you are going to,idk i ran out of jokes give me a break")

import easygui
age = easygui.enterbox("what is the age of whatever abomination you have created")
age = int(age)
if age <= 18:
    easygui.msgbox("a youth huh? you might struggle a bit but you would live longer") 
elif age >= 50:
    usable("wow you choose hard difficulty")
elif age <= 999:
    usable("ah yes golden age nice choice")

strength = easygui.choicebox(
    "choose your strength",
    choices=["health", "speed", "charisma"]
)
if strength == "health":
    usable("playing it safe i see")
elif strength == "speed":
    usable("you would like to outrun your enemies? nice i am coward like you too")
elif strength == "charisma":
    usable("you would like to be the star you will never become")

usable("and finally")
skill = easygui.enterbox("choose your skill")
usable(f"{skill} is a nice skill even tho i dont know what you typed there,hope you didnt type any bad words")

easygui.msgbox(f"well well well {name} the {age} year old {skill} a {location} citizen and proud leader of the {color} {clan} who choose {difficulty} difficulty")
usable("well uh good adventures i guess idk this is kind of cringe that i am sorry you got to witness first hand")
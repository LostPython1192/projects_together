import random
import sys
import time


def clean_input(input:str):
    input = input.lower()
    if not input.strip():
        # Not a valid input

        print("Not a valid answer")
        
        return 1
    
    # Valid input

    return 0

def loading():

    #print("CREATING STORY PLEASE HOLD")

    sys.stdout.write("CREATING STORY PLEASE WAIT")
    sys.stdout.flush()

    time.sleep(random.randrange(3, 10))

    sys.stdout.write("\rAdding spice              ")
    sys.stdout.flush()

    time.sleep(4)
    
    sys.stdout.write("\rAdding humor              ")
    sys.stdout.flush()

    sys.stdout.write("\rCOMPLETED!              \n")

def wait():

    time.sleep(random.randrange(3, 5))

def ask(question, space=True):

    while True:

        if space:
            answer = input(f"{question} ")
        else:
            answer = input(f"{question}")


        if clean_input(answer) == 0:
            return answer

        else:
            continue

# 
def ask_options(question, space=True, allowed=[], non_allowed=[], error_message=""):

    while True:

        if space:
            answer = input(f"{question} ")
        else:
            answer = input(f"{question}")

        if allowed != []:

            if clean_input(answer) == 0 and answer in allowed:
                return answer
        
        else:

            if clean_input(answer) == 0 and answer not in non_allowed:
                return answer
            
            else:
                print(f"{error_message}")
                continue
        print(f"{error_message}")

print("Welcome to mad libs!")

game_style = ['[1] Going to the store', ' [2] My fist high school dance', ' [3] My first barbeque', ' [4] My first time driving']
    
scenario = ""

scenario = ask_options(f"What scenario would you like to play?\n{game_style[0]} {game_style[1]} {game_style[2]} {game_style[3]}\n", False, ["1", "2", "3", "4"], [], "\nPlease enter a vaild story ID\n")

# Going to the store
def store():

    mainchar = ask("Give me a name")
    store = ask("Give me a store")
    noun1 = ask("Give me a noun")
    enemy = ask("Give me someone you dislike")
    noun2 = ask("Give me another noun")
    verb1 = ask("Give me a verb ending in 'ed'")
    verb2 = ask("Give me a violent verb")
    verb3 = ask("Give me another violent verb")
    noun3 = ask("Give me a noun")
    age = ask("Give me an age")
    gender = ask("Give me a gender(good luck...)")
    verb4 = ask("Give me a verb ending in 'ing'")
    verb4new = verb4.removesuffix("ing")
    bodypart1 = ask("Give me a body part")
    bodypart2 = ask("Give me a different body part")
    place = ask("Give me a place")
    
    loading()
    
    print(f"""One day, {mainchar} went to {store} to get {noun1}.""")
    wait()
    print(f"Unfortuantly, {mainchar} didn't find any {noun1} on the shelves, but did find it in {enemy}'s shopping cart!")
    wait()
    print(f"{mainchar} took a {noun2} from the shelves and {verb1} it on {enemy}'s head! ")
    wait()
    print(f"{enemy} grabbed {mainchar}'s {bodypart1} and {verb2} {mainchar} in the {bodypart2}!")
    wait()
    print(f"With all the commotion, {store}'s security showed up to {verb3} {enemy} and {mainchar}!")
    wait()
    print(f"{mainchar} tried to get out of there, but ended up tripping on a {age} year old {gender}! ")
    wait()
    print(f"The {store}'s security ended up chatching {mainchar}, and has brought them to {place} for interrogation, and strapped {mainchar} to a chair!")
    wait()
    print(f"'I cought you {verb4}! Now you're coming with me to the {place}!' Said the {store}'s security. ")
    wait()
    print(f"'I didn't {verb4new}! I just wanted to get {noun1}, then {enemy} attacked me! I'm innocent!' said {mainchar}")
    wait()
    print(f"'don't you lie, it was all recorded on the {store}'s {noun3}s.' ")
    wait()
    print(f"'I'm not lying, just check the {noun3}.' as the {store}'s security walked away, {mainchar} got out of the chair and ran away.")
    wait()
    print(f"Hopeful that dosen't happen again! The next day, {mainchar} went to {store}...")

def driving():

    mainchar = ask("Give me a name")
    noun1 = ask("Give me a noun")
    feeling1 = ask("Give me a Feeling")
    if feeling1 == "happy":
        feeling1 = "happi"
    instr = ask("Give me a person you know")
    
    cardir = ask("Give me a cardinal direction")
    
    noun2 = ask("Give me a noun")
    
    mph = ask("Give me a number")
    
    obj1 = ask("Give me a plural object")
    obj2 = ask("Give me a plural object")
    obj3 = ask("Give me a plural object")

    io = ask_options("In or On", True, ["in", "on"])

    place = ask("Give me a place")

    vehicle = ask("Give me a vehicle")

    verb1 = ask("Give me a verb ending in 'ing'")
    loading()

    speak = ask("Give me a way of speaking (i.e whisper, yell, etc...)")

    updown = ask_options("Up or down", True, ["up", "down"])

    if updown == "up":
        updown = "Speed up"

    else:
        updown = "Slow down"

    noun3 = ask("Give me a noun")

    print(f"""
    
    One day {mainchar} was getting ready for the first time driving.
    {mainchar} almost forgot to bring their {noun1} with them.
    {mainchar} was very {feeling1} about driving for their first time.
    'Get in the {vehicle} {mainchar}! You're taking so long!" said driving teacher {instr}.
    'fine' said {mainchar} {feeling1}ly.
    'So, which pedal does what?' asked driving teacher {instr}.
    '{cardir}!' said {mainchar} confidently. 'What?' {instr} said.
    Then, {mainchar} floored the gas pedal!
    'AAAAAAAAAAAHHH!!!' screamed {instr}.
    {mainchar} hit a {noun2} at {mph} mph!
    dodging and weaving through {obj1}, {obj2}, and {obj3}, eventually ending up {io} {place}!
    almost hitting other {vehicle}s, {mainchar} starts {verb1}! 
    'WHAT ARE YOU DOING {mainchar}!?' {speak}'s {instr}. '{updown}! {updown}!!!!'
    all of the sudden, a {noun3} hits the windsheild, and the {vehicle} flips over!
    """)

match scenario:

    case "1":
        store()

    case "2":
        driving()

    case other:
        print("Sorry that story is not ready yet!")

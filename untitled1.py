print("you are on a deserted island in a 2D world.")
print("Try to survive until rescue arrives!")
print("Available commands are in CAPITAL letters.")
print("Any other command exits the program")
print("First LOOK around...")
do=input(" ")
if do== "LOOK":
    print("You are stuck in a sand ditch." )
    print("Crawl out LEFT or RIGHT.")
    do=input(" ")
if do== "LEFT":
    print("You see a CRAB and a STARFISH!")
    print("You are hungry, which one to eat?")
    do==input(" ")
    if do== "STARFISH":
        print("You feel unwell, you did not survive.")
    elif do== "CRAB":
        print("Raw crab should be fine, right? YES or NO?")
        do==input("")
        if do== "YES":
            print("you ate it raw, it helped you find a TREE.")
            do==input("")
            if do=="TREE":
                print("It's a coconut tree! You are thristy, do you wamt to drink the water? YES or NO?")
                do==input("")
                if do=="YES":
                    print("coconut water and raw crab did not mix.")
                    print("you did not survuve")
                elif do=="NO":
                    print("great choice! The rescue ship has come! You survived!")
    elif do=="NO":
        print("There is nothing else to eat, you did not survuve.")
            
elif do=="RIGHT":
        print("No can do. That side is very slippery.")
        print("You fall very far into some weird cavern.")
        print("You do not survive.")
else:
    print("Try again")
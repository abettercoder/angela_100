print("Welcome to treasure Island")
print("Your mission is to find the treasure")

darkcave = input("You are in a dark cave. You can see a light to the left. Choose left or right?")
if (darkcave == "left"):
    swim = input("You see a wooden plank. Do you swim across or walk on?")
    if (swim == "walk"):
        print("You walked and fell in a pit. You are dead.You've lost")
    elif (swim == "swim across"):
        print("You managed to get to the other side. You reached a castle. There are two doors. Do you enter door #1 or door #2?")
        castle = input("Which door do you choose?")
        if (castle == "1"):
            print("You enter the room and see a sleeping guard. You are awoken by a noise. You see a sword and shield. Do you take the sword or the shield?")
            sword = input("Which do you choose?")
            if (sword == "sword"):
                print("You take the sword and walk out the room. You see a light at the end of the tunnel. Do you go towards the light or towards the other side?")
                light = input("Which do you choose?")
                if (light == "light"):
                    print("You walk towards the light. You see a treasure chest. Do you open it or leave it alone?")
                    chest = input("Which do you choose?")
                    if (chest == "open"):
                        print("You open the chest and found the treasure. Congratulations, You've won!")
                    else :
                        print("You leave the chest alone. You walk out of the room and guard catches you, You are imprisoned. You've lost")
                else:
                    print("You walk towards the other side. It is dark, you fell in a pit and die?")
            else:
                print("You take the shield and droppped it accidentally. You ran out of the room and guard catches you. You are imprisoned. You've lost")
        else:
            print("You've entered the wrong room. There is a troll there. You fight him and die. You've lost")
    else:
        print("You've to swim across or walk")
else:
    print("You've taken the wrong path. A lion is there in the dark. He attacks and you die. You've lost.")

                    
                            
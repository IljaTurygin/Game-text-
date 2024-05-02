import tkinter as tk
import time
import sys
import random

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def encounter_wolf():
    enemies = random.randint(1, 4)

    wolf_HP = [40] * enemies
    player_HP = 100

    slow_print("You are surrounded by " + str(enemies) + " wolves. ")

    # Loop for the encounter
    while True:
        # Player's turn
        slow_print("What will you do? ")
        print("Attack, Defend, Item, Run")
        choice = input("Enter choice: ").lower()  # Convert input to lowercase

        if choice == "attack":
            slow_print("What type of attack would you like to perform? ")
            attack = input("1. Unarmed strike 2. Kick(1 or 2): ")
            if attack == "1":
                slow_print("Select a target (1 to " + str(enemies) + "):")
                target = int(input())
                if 1 <= target <= enemies:
                    accuracy = random.randint(1, 100)
                    if accuracy < 10:
                        print("You missed the target")
                    else:          
                        damage = random.randint(5, 10)
                        wolf_HP[target - 1] -= damage
                        slow_print("You attack the wolf " + str(target) + " with an unarmed strike! "
                                   "Dealing " + str(damage) + " damage.\n")
                else:
                    slow_print("Invalid target!\n")
            elif attack == "2":
                slow_print("Select a target (1 to " + str(enemies) + "): ")
                target = int(input())

                if 1 <= target <= enemies:
                    accuracy = random.randint(1, 100)
                    if accuracy < 31:
                        print("You missed the target")
                    else:
                        damage = random.randint(10, 20)
                        wolf_HP[target - 1] -= damage
                        slow_print("You attack the wolf " + str(target) + " with a kick! "
                                   "Dealing " + str(damage) + " damage.\n")
                else:
                    slow_print("Invalid target!\n")
            else:
                slow_print("Invalid choice!\n")
        
        elif choice == "defend":
            slow_print("You chose to defend yourself\n")
        elif choice == "item":
            slow_print("You don't have any items\n")
        elif choice == "run":
            slow_print("You have chosen to escape\n")
            escape = random.randint(1, 100)
            if escape < 16:
                slow_print("You have escaped\n")
                return "escape"
            else:
                slow_print("You failed to escape\n")
        else:

        
        # Check if all wolves are defeated
            if sum(wolf_HP) <= 0:
                slow_print("You defeated all the wolves!\n")
                break
        
        # Wolves' turn
        for i in range(enemies):
            if wolf_HP[i] > 0:
                wolf_hit = random.randint(1, 100)
                wolf_attack = random.randint(10, 18)
                if wolf_hit < 16:
                    print("Wolf " + str(i+1) + " missed his attack\n")
                else:
                    player_HP -= wolf_attack
                    print("Wolf " + str(i+1) + " attacks you, dealing " + str(wolf_attack) + " damage!\n")
        
        # Check if the player is defeated
        if player_HP <= 0:
            slow_print("You were defeated by the wolves...")
            sys.exit()  # End the game if the player is defeated by the wolves

def main():
    slow_print("You wake up.......")
    slow_print("The sky is dark and the moonlight barely reaches you. After looking around, you find yourself in a forest.\n")

    # Start the cold counter
    cold_counter = 0

    while True:  # Loop until the player decides to wait for daylight or chooses another option
        slow_print("What will you do?\n")
        slow_print("1. Wait for daylight\n")
        slow_print("2. Find a way out of the forest\n")

        decision = int(input("Enter your choice: "))
        if decision == 1:
            slow_print("You decided to wait for the day\n")
            check = random.randint(1, 100)
            if check < 21:
                slow_print("You are attacked by wolves\n")
                encounter_wolf()
            elif 21 <= check < 60:
                slow_print("You feel a chill down your spine as the night grows colder\n")
                cold_counter += 1
                if cold_counter >= 3:
                    slow_print("You've felt too cold too many times and succumbed to the elements. Game over.\n")
                    return  # End the game
            else:
                slow_print("You wait for daylight to come...\n")
                continue  # Continue with the loop if the player waits for daylight
        elif decision == 2:
            slow_print("You decide to find a way out of the forest\n")
            slow_print("After wandering, you come across three paths.\n")
            slow_print("Next to the path there is a sign\n")
            slow_print("First(1) path leads to the city\n")
            slow_print("Second(2) path leads to the village\n")
            slow_print("Third(3) path leads to the sea\n")
            decision2 = int(input("Which will you choose? "))
            if decision2 == 1:
                slow_print("You decided to journey to the city\n")
                slow_print("While you journey to the city, the sun has come out\n")
                slow_print("After walking for hours you feel tired,but all is not lost\n")
                slow_print("You can see the city on the horizon\n")
                slow_print("After reaching the gates the guards stop you\n")
                slow_print("One of the guards says-Please pay the fee to enter the city!\n")
                slow_print("How will you respond?(you don't have any money)\n")
                print("1. Negotiate with the guards\n"
                      "2. Try to convince someone entering the city to give you money to enter\n"
                      "3. Attack the guards")
                decision3 = input("Enter your choice: ")
                if decision3 == "1":
                    chance = random.randint(1, 100)
                    if chance < 36:
                        slow_print("The guards let you in\n")
                        slow_print("After entering the city What will you do?\n")
                        slow_print("1. Find a palce to eat\n"
                                   "2. Find a place to sleep\n"
                                   "3. Find a job\n")
                        
                        decision4 = input("Enter your choice: ")
                        
                        if decision4 == "1":
                            chance2 = random.randint(1, 100)
                            if chance2 < 26:
                                slow_print("You found a place to eat if you clean up afterwards\n")
                                slow_print("")
                            elif 26 <= chance2 < 70:
                                slow_print("Some locals gave you a loaf of bread\n")
                            else:
                                slow_print("You found nothing\n")
                        elif decision4 == "2":
                            chance2 = random.randint(1, 100)
                            if chance2 < 36:
                                slow_print("You found a place to sleep in\n")
                            else:
                                slow_print("You found nothing and will sleep on the street\n")
                        elif decision4 == "3":
                            chance2 = random.randint(1, 100)
                            if chance2 < 80:
                                slow_print("you found a job\n")
                            else:
                                slow_print("You were unlucky and did not find a job.\n")
                    else:
                        slow_print("They tell you to get lost\n")

                elif decision3 == "2":
                    chance = random.randint(1, 100)
                    if chance < 41:
                        slow_print("They gave you money and you have entered the city!\n")
                        slow_print("The guards let you in\n")
                        slow_print("After entering the city What will you do?\n")
                        slow_print("1. Find a palce to eat\n"
                                   "2. Find a place to sleep\n"
                                   "3. Find a job\n")
                        
                        decision4 = input("Enter your choice: ")
                        
                        if decision4 == "1":
                            chance2 = random.randint(1, 100)
                            if chance2 < 26:
                                slow_print("You found a place to eat if you clean up afterwards\n")
                                slow_print("")
                            elif 26 <= chance2 < 70:
                                slow_print("Some locals gave you a loaf of bread\n")
                            else:
                                slow_print("You found nothing\n")
                        elif decision4 == "2":
                            chance2 = random.randint(1, 100)
                            if chance2 < 36:
                                slow_print("You found a place to sleep in\n")
                            else:
                                slow_print("You found nothing and will sleep on the street\n")
                        elif decision4 == "3":
                            chance2 = random.randint(1, 100)
                            if chance2 < 80:
                                slow_print("you found a job\n")
                            else:
                                slow_print("You were unlucky and did not find a job.\n")

                    else:
                        slow_print("They refused")

                elif decision3 == "3":
                    slow_print("The guards killed you")
                    return #the game ends here


            elif decision2 == 2:
                slow_print("You decided to journey to the village\n")
            elif decision2 == 3:
                slow_print("You decided to journey to the sea\n")
            return  # End the game if the player chooses to find a way out of the forest
        else:
            slow_print("Invalid choice. Please try again.\n")
            break  # Break the loop if the player chooses an invalid option

if __name__ == "__main__":
    main()  # Run the text-based version of the game


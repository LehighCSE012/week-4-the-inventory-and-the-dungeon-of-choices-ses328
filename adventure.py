'''
Coding Assignment 3
'''
import random
def acquire_item(inventory,item):
    #'''Add an item to the inventory and notifies the user'''
    inventory.append(item) #add an item to the inventory
    print(f"You aquired a {item}!")
    return inventory

def display_inventory(inventory):
    #'''Display the user's inventory'''
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    #Handles dungeon exploration phase
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(f"\{room_description}")

        if item:
            acquire_item(inventory, item)
            print(f"You found a {item} in the room!")
        
        if challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        else:
            success_message, failure_message, health_change = challenge_outcome
            if challenge_type == "puzzle":
                print("You encounter a puzzle!")
                choice = input("Do you want to solve it? (solve/skip):").strip().lower()
                if choice == "solve":
                    success = random.choice ([True, False])
                    if success:
                        print(success_message)
                        player_health += health_change #health change can be negative
                    else:
                        print(failure_message)
            elif challenge_type == "trap":
                print("You see a potential trap!")
                choice = input("Do you want to disarm it? (disarm/bypass):").strip().lower()
                if choice == "disarm":
                    success = random.choice([True, False])
                    if success:
                        print(success_message)
                    else:
                        print(failure_message)
                        player_health += health_change #Ensure health_change is negative

        player_health = max(0, player_health) #ensures health does not go below zero
        if player_health == 0:
            print("You are barely alive!")
            break

        display_inventory(inventory)
    print(f"You exit the dungeon with {player_health} health left.")
    return player_health, inventory

def main():
    #'''Main fuction to run the game'''
    player_health = 100
    inventory = []
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", 
            ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", 
            ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]

    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    print("Game Over!")

if __name__ == "__main__":
    main()

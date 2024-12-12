# Nicholas Candanoza
# 11/19/2024
# P5HW1
# Create a text-based game using functions

import random

def create_character():
    character = {
        "name": input("Enter the character's name: "),
        "health": int(input("Enter the character's health (e.g., 100): ")),
        "mana": int(input("Enter the character's mana (e.g., 50): ")),
        "sword": input("Enter the name of the character's sword: ")
    }
    return character

def display_character(character):
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

def simulate_battle(attacker, victim):
    # Calculate damage
    damage = random.randint(0, attacker["mana"])
    print(f"{attacker['name']} attacks {victim['name']} for {damage} damage!")
    
    # Apply damage to the victim's health
    victim["health"] -= damage
    
    # Ensure health doesn't go below zero
    if victim["health"] < 0:
        victim["health"] = 0
    
    # Display the updated health of the victim
    print(f"{victim['name']}'s health is now {victim['health']}.")

def victim_attack(attacker, victim):
    # Calculate damage from victim to attacker
    damage = random.randint(0, victim["mana"])
    print(f"{victim['name']} counters and attacks {attacker['name']} for {damage} damage!")

    # Apply damage to the attacker's health
    attacker["health"] -= damage

    # Ensure attacker's health doesn't go below zero
    if attacker["health"] < 0:
        attacker["health"] = 0

    # Display the updated health of the attacker
    print(f"{attacker['name']}'s health is now {attacker['health']}.")

def heal_attacker(attacker):
    # Generate random healing value between 0 and 100
    healing = random.randint(0, 100)
    print(f"Healing {attacker['name']} for {healing} health!")
    
    # Apply healing to the attacker's health
    attacker["health"] += healing
    
    # Display the updated health of the attacker
    print(f"{attacker['name']}'s health is now {attacker['health']}.")

def special_attack_and_charge(attacker, victim):
    # Check if attacker has enough mana
    if attacker["mana"] < 10:
        print(f"{attacker['name']} does not have enough mana to perform a special attack!")
        print(f"{attacker['name']} must recharge mana first.")
        return False  # Attack not successful
    
    # Perform the special attack
    damage = random.randint(10, attacker["mana"])
    print(f"{attacker['name']} uses a special attack on {victim['name']} for {damage} damage!")

    # Deduct mana and apply damage
    attacker["mana"] -= 10
    victim["health"] -= damage

    # Ensure victim's health doesn't drop below zero
    if victim["health"] < 0:
        victim["health"] = 0

    print(f"{victim['name']}'s health is now {victim['health']}.")
    print(f"{attacker['name']}'s mana is now {attacker['mana']}.")

    # Charge mana automatically after special attack
    recharge = random.randint(5, 20)
    attacker["mana"] += recharge
    print(f"{attacker['name']} recharges {recharge} mana after the special attack.")
    print(f"{attacker['name']}'s mana is now {attacker['mana']}.")
    return True  # Attack was successful

def game_over():
    print("\n=== GAME OVER ===")
    print("You have been defeated. Better luck next time!")

def game_menu(attacker, victim):
    while attacker["health"] > 0 and victim["health"] > 0:
        print("\n=== Game Menu ===")
        print("1. Regular Attack")
        print("2. Special Attack with Charge")
        print("3. Heal Yourself (Attacker)")
        print("4. Victim Attacks You")
        print("5. Display Characters")
        print("6. Quit Game")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            simulate_battle(attacker, victim)
        elif choice == "2":
            success = special_attack_and_charge(attacker, victim)
            if success and victim["health"] == 0:
                print(f"{victim['name']} has been defeated! {attacker['name']} wins!")
                break
        elif choice == "3":
            heal_attacker(attacker)
        elif choice == "4":
            victim_attack(attacker, victim)
            if attacker["health"] == 0:
                game_over()
                break
        elif choice == "5":
            print("\nAttacker's Stats:")
            display_character(attacker)
            print("\nVictim's Stats:")
            display_character(victim)
        elif choice == "6":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    print("Game is starting....")
    print("\nCreate your characters!")
    attacker = create_character()
    victim = create_character()
    
    print("\nCharacters created successfully! Let's start the game.")
    game_menu(attacker, victim)

if __name__ == "__main__":
    main()

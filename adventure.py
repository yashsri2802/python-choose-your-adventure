import sys
from typing import List

def get_choice(num_options: int) -> int:
    while True:
        try:
            choice_str = input(f"Choose an option (1-{num_options}): ").strip()
            if not choice_str:
                print("Please enter a number.")
                continue
            # Allow quick quit
            if choice_str.lower() in ('q', 'quit', 'exit'):
                print("Exiting the adventure. Goodbye!")
                sys.exit(0)
            choice = int(choice_str)
            if 1 <= choice <= num_options:
                return choice
            else:
                print(f"Please choose a number between 1 and {num_options}.")
        except ValueError:
            print("That's not a number. Try again (or type 'q' to quit).")
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D / Ctrl+C gracefully
            print("\nInterrupted. Goodbye!")
            sys.exit(0)

def intro() -> None:
    print("=" * 60)
    print("THE RUINS OF KAL-HAR")
    print("=" * 60)
    print(
        "You are an explorer who has traveled far to reach the ruined temple of Kal-Har.\n"
        "Legends say the temple holds an ancient artifact with vast knowledge — and danger.\n"
        "As you step into the moonlit entrance, three paths reveal themselves."
    )
    print()

def ending_good() -> None:
    print("\n" + "-" * 50)
    print("GOOD ENDING: Light of Kal-Har")
    print("-" * 50)
    print(
        "You emerge from the temple with the artifact safely wrapped in cloth. The knowledge\n"
        "you gained will change the world for the better. Townsfolk sing of your journey.\n"
        "You feel fulfilled and hopeful about the future."
    )
    print("-" * 50)
    print("THE END\n")

def ending_bad() -> None:
    print("\n" + "-" * 50)
    print("BAD ENDING: The Silence")
    print("-" * 50)
    print(
        "A hidden trap triggers. The walls groan and a cold darkness fills the chamber.\n"
        "You fought bravely, but the temple keeps its secrets. The last thing you hear\n"
        "is the echo of your own footsteps fading away."
    )
    print("-" * 50)
    print("THE END\n")

def ending_neutral() -> None:
    print("\n" + "-" * 50)
    print("NEUTRAL ENDING: A Walk Away")
    print("-" * 50)
    print(
        "You decide that some mysteries are too dangerous. You leave the ruins empty-handed\n"
        "but alive. Life goes on, and sometimes wisdom is knowing when to walk away."
    )
    print("-" * 50)
    print("THE END\n")

def left_corridor() -> None:
    print("\nYou take the left corridor. Torches flicker as you move deeper.")
    print("At the end you find a heavy door with a strange sun emblem.")
    print("1) Try to open the door carefully.")
    print("2) Search around the door for traps or hidden mechanisms.")
    choice = get_choice(2)
    if choice == 1:
        # Risky direct approach — chance of triggering a trap (we simulate with a story branch)
        print("\nYou push the heavy door. It resists, then gives with a grinding sound.")
        print("A dart shoots from a small hole, but you see it late.")
        ending_bad()
    else:
        # Safer approach leads to the artifact — good ending
        print("\nYou inspect the edges and find a recessed lever disguised as decoration.")
        print("With careful hands you disable a mechanism and open the door safely.")
        print("Inside sits the glowing artifact upon a pedestal.")
        ending_good()

def right_chamber() -> None:
    print("\nYou take the right path and enter a circular chamber with inscriptions.")
    print("An old voice echoes: 'Answer true: The key to Kal-Har is not taken but earned.'")
    print("1) Speak confidently: 'Knowledge and patience.'")
    print("2) Attempt to take a small key from the pedestal without answering.")
    choice = get_choice(2)
    if choice == 1:
        print("\nThe inscriptions glow and a hidden shelf opens, revealing a small key.")
        print("With the key you unlock a secret passage that leads you to the artifact room.")
        ending_good()
    else:
        print("\nAs your hand closes on the key, the floor shifts and you are sealed in a safe alcove.")
        print("You wait hours until the mechanism resets and you find your way back outside.")
        ending_neutral()

def center_stairs() -> None:
    print("\nYou descend the center staircase into the heart of the temple.")
    print("The air grows colder and the sounds of the outside world fade.")
    print("1) Continue down toward the faint humming sound.")
    print("2) Light a torch and explore the side niches instead.")
    choice = get_choice(2)
    if choice == 1:
        print("\nThe humming grows into a roar. You step into a vast hall of gears and ancient engines.")
        print("A misstep causes the mechanism to lock and the hall seals. You cannot escape.")
        ending_bad()
    else:
        print("\nWith your torch you cautiously inspect the niches and discover ancient murals.")
        print("One mural contains instructions to safely navigate the temple — you use it to exit.")
        ending_neutral()

def crossroads() -> None:
    print("Three paths lie before you:")
    print("1) Left corridor — the way of hidden doors.")
    print("2) Right chamber — the way of riddles and tests.")
    print("3) Center stairs — down to the heart of Kal-Har.")
    choice = get_choice(3)
    if choice == 1:
        left_corridor()
    elif choice == 2:
        right_chamber()
    else:
        center_stairs()

def play_again_prompt() -> bool:
    while True:
        try:
            ans = input("Would you like to play again? (y/n): ").strip().lower()
            if ans in ('y', 'yes'):
                return True
            if ans in ('n', 'no'):
                return False
            print("Please type 'y' or 'n'.")
        except (EOFError, KeyboardInterrupt):
            print("\nInterrupted. Goodbye!")
            sys.exit(0)

def main() -> None:
    while True:
        intro()
        crossroads()
        # After an ending, offer to play again
        if not play_again_prompt():
            print("Thanks for playing! Farewell, adventurer.")
            break
        print("\n" + "=" * 60 + "\n" )

if __name__ == "__main__":
    main()

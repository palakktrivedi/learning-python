def show_intro():
    print("=== Mystery Lab Adventure ===")
    print("You wake up in a mysterious laboratory.\n")

def make_choice():
    choice = input("Do you EXPLORE the room or LEAVE? ").lower()

    if choice == "explore":
        print("You discover a glowing device on a table.")
    elif choice == "leave":
        print("You escape safely... for now.")
    else:
        print("You hesitate and nothing happens.")

def play_game():
    playing = True

    while playing:
        show_intro()
        make_choice()
    
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
                playing = False

    print("\nThanks for playing!\n")

# Start the game
play_game()
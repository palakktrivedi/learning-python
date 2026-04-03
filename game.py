print("=== Mystery Lab Adventure ===")

playing = True

while playing:
    print("You wake up in a mysterious laboratory.\n")

    choice = input("Do you EXPLORE the room or LEAVE? ").lower()

    if choice == "explore":
        print("You discover a glowing device on a table.")
    elif choice == "leave":
        print("You escape safely... for now.")
    else:
        print("You hesitate and nothing happens.")

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        playing = False

print("\nThanks for playing!\n")
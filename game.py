# === Game Data ===

rooms = {
     "lab": {
          "description": "You are in a mysterious lab. There is a door to the north.",
          "items": ["key"],
          "exits": {"north": "hallway"}
     },

     "hallway": {
          "description": "A long hallway. There is a locked door to the east.",
          "items": [],
          "exists": {"south": "lab", "east": "treasure"}
     },

     "treasure": {
          "description": "A room filled with treasure! You win!",
          "items": [],
          "exists": {}
     }
}

inventory = []
current_room = "lab"

# === Functions ===
def show_status():
     print("\n====================")
     print(f"You are in the {current_room}.")
     print(rooms[current_room]["description"])
     print(f"Inventory: {inventory}")

     if rooms[current_room]["items"]:
          print(f"You see: {rooms[current_room]['items']}")

def get_command():
     return input("\nWhat do you want to do? ").lower()


    










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
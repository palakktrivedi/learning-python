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
        "exits": {"south": "lab"},
        "locked": True
    },
    "treasure": {
        "description": "A room filled with treasure! You win!",
        "items": [],
        "exits": {}
    }
}

inventory = []
current_room = "lab"


# === Functions ===

def show_status():
    print("\n======================")
    print(f"You are in the {current_room}.")
    print(rooms[current_room]["description"])
    print(f"Inventory: {inventory}")

    if rooms[current_room]["items"]:
        print(f"You see: {rooms[current_room]['items']}")


def get_command():
    return input("\nWhat do you want to do? ").lower()


def move(direction):
    global current_room

    if direction in rooms[current_room]["exits"]:
        next_room = rooms[current_room]["exits"][direction]

        # Check for locked door
        if next_room == "treasure" and "key" not in inventory:
            print("The door is locked. You need a key.")
        else:
            current_room = next_room
            print(f"You move {direction}.")
    else:
        print("You can't go that way.")


def take_item(item):
    if item in rooms[current_room]["items"]:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"You picked up {item}.")
    else:
        print("That item is not here.")

def drop_item(item):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"You dropped the {item}.")
    else:
        print("You do not have that item.")

def use_item(item):
    if item not in inventory:
        print(f"You do not have the {item}.")
        return
    
    if item == "key" and current_room == "hallway":
        if rooms["hallway"]["locked"]:
            print("You unlock the door to the east!")
            rooms["hallway"]["exits"]["east"] = "treasure"
            rooms["hallway"]["locked"] = False
        else:
            print("The door is already unlocked.")
    else:
        print(f"You can't use the {item} here.")

def process_command(command):
    words = command.split()

    if len(words) == 0:
        return

    if words[0] == "go" and len(words) > 1:
        move(words[1])

    elif words[0] == "take" and len(words) > 1:
        take_item(words[1])

    elif words[0] == "look":
        show_status()

    elif words[0] == "inventory":
        if len(inventory) == 0:
            print("You are carrying nothing.")
        else:
            print("You are carrying:")
            for item in inventory:
                print(f"- {item}")

    elif words[0] == "drop" and len(words) > 1:
        drop_item(words[1])

    elif words[0] == "use" and len(words) > 1:
        use_item(words[1])

    elif words[0] == "quit":
        return False
    
    else:
        print("Invalid command.")

    return True


# === Game Loop ===

def play_game():
    print("=== Adventure Game ===")

    playing = True
    while playing:
        show_status()
        command = get_command()
        playing = process_command(command)

    print("Thanks for playing!")


# Start game
play_game()
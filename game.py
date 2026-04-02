print("You wake up in a mysterious laboratory.")

name = input("What is your name, explorer? ")

print(f"Welcome, {name}.")

choice = input("Do you EXPLORE the room or LEAVE? ").lower()

if choice == "explore":
    print("You discover a glowing device on a table.")
elif choice == "leave":
    print("You escape safely... for now.")
else:
    print("You hesitate and nothing happens.")
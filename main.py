# 12 rooms text adventure game.
# Optimized for TI-nspire CX II python.
# Press Ctrl+R to play!

# Time libary used to add wait time during printing
import time

# Load the map file
from map import *
inventory = []

# Defining print room function
def gotoRoom(number):

  # Get the room from it's number
  room = m["rooms"][number]

  # Tell about the room
  print(room["name"])
  print(room["description"])

  # Quit the game if finished
  if number == m["finish"]:
    quit()

  # Show the inventory
  print("Inventory:"+str(m["inventory"]))
  input()

  # Display the menu
  while True:

    # Wait one second
    time.sleep(1)

    # Ask the user how they would like to continue
    print("What would you like to do? \nHint: Enter the first letter of the corresponding with the action you would like to make")
    if "item" in room:
      print("- Look around")
    if "n" in room["exits"]:
      print("- North")
    if "s" in room["exits"]:
      print("- South")
    if "w" in room["exits"]:
      print("- West")
    if "e" in room["exits"]:
      print("- East")
    print("- Quit")
    UserChoice = input()

    # Defining walk to room function
    def walk(direction):
      print("You have chosen to walk " + direction + "...\n ")
      if UserChoice in room["exits"]:
        nextRoom = m["rooms"][room["exits"][UserChoice]]
        # Check if all the reqiured items are in the inventory
        if "require" in nextRoom:
          if set(nextRoom["require"]).issubset(set(m["inventory"])):
            gotoRoom(room["exits"][UserChoice])
          else:
            print(nextRoom["clue"],"red")
        else:
          gotoRoom(room["exits"][UserChoice])
      else:
        print("You cannot walk " + direction + ", there is a wall blocking your way.\n ")

    # Look around
    if UserChoice == "l":
      print("You have chosen to look around...")
      if "item" in room:
        if room["item"] in m["inventory"]:
          print("You have already looked through this room.\n ")
        else:
          print(m["items"][room["item"]])
          time.sleep(1)
          print(room["item"] + " added to your inventory.\n ")
          m["inventory"].append(room["item"])
      else:
        print("You found nothing of value.\n ")
    # Walk in direction
    elif UserChoice == "n":
      walk("north")
    elif UserChoice == "s":
      walk("south")
    elif UserChoice == "w":
      walk("west")
    elif UserChoice == "e":
      walk("east")
    elif UserChoice == "q":
      quit()
    # Invalid answer
    else:
      print("Please select a valid answer.\n ")

# Print the title and rules
print(m["title"]+" by "+m["author"])
print(m["rules"])

# Start the game on enter
print("Press enter to continue")
input()
gotoRoom(m["start"])

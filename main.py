# Importing libraries
import json # Used to parse the map.json file
import time # Used to add wait time during printing
from termcolor import cprint # Used to print in different colors

# Load the map file
m = json.loads(open("map.json").read())
inventory = []

# Defining print room function
def gotoRoom(number):

  # Get the room from it's number
  room = m["rooms"][number]

  # Tell about the room
  cprint(room["name"],"blue")
  print(room["description"]+"\n")
  time.sleep(1)

  # Quit the game if finished
  if number == m["finish"]:
    quit()

  # Show the inventory
  cprint("Inventory:"+str(m["inventory"])+"\n", "yellow")

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
    print() # Print blank newline
    UserChoice = input().lower()

    # Defining walk to room function
    def walk(direction):
      print("You have chosen to walk " + direction + "...\n")
      if UserChoice in room["exits"]:
        nextRoom = m["rooms"][room["exits"][UserChoice]]
        # Check if all the reqiured items are in the inventory
        if "require" in nextRoom:
          if set(nextRoom["require"]).issubset(set(m["inventory"])):
            gotoRoom(room["exits"][UserChoice])
          else:
            cprint(nextRoom["clue"]+"\n","red")   
        else:
          gotoRoom(room["exits"][UserChoice])
      else:
        cprint("You cannot walk " + direction + ", there is a wall blocking your way.\n", "red")

    # Look around
    if UserChoice == "l":
      print("You have chosen to look around...")
      if "item" in room:
        if room["item"] in m["inventory"]:
          print("You have already looked through this room.\n")
        else:
          print(m["items"][room["item"]]+"\n")
          time.sleep(1)
          cprint(room["item"] + " added to your inventory.\n", "yellow")
          m["inventory"].append(room["item"])
      else:
        print("You found nothing of value.\n")
    # Walk in direction
    elif UserChoice == "n":
      walk("north")
    elif UserChoice == "s":
      walk("south")
    elif UserChoice == "w":
      walk("west")
    elif UserChoice == "e":
      walk("east")
    # Invalid answer
    else:
      cprint("Please select a valid answer.", "red")

# Print the title and rules
cprint(m["title"]+" by "+m["author"]+"\n","green")
cprint(m["rules"]+"\n","green")

# Start the game on enter
print("Press enter to start")
input()
gotoRoom(m["start"])
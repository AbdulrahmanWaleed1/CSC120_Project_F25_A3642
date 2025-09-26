import random
game_name = "Leviathan Plunge" # name your game project
print(f"Welcome to {game_name}!") # print greetings with game name
print("============================") # add or remove equal symbol to align the greetings

# Ask for the character's name
name = input("Before your quest starts. What is your name?\n> ")

# Print the name
print(f"Wonderful! Welcome, {name}, Let us begin the story.")

# Player Stats
player = {
        "name": name,
        "health": 100,
        "coin": 0,
}

# (Potential monster list) monsters = ["wolf", "dristini", "zombie mushroom", "shrieker"]
# monster = random.choice(monsters)

# Events and what happen
events = ["find a coin","do nothing", "meet a monster"]
event = random.choice(events)
print(f"While exploring, you {event}!")
if event == "find a coin":
    player["coin"] += 1
    print(f"{name} found a coin, {name} now has {player["coin"]} coins")
if event == "meet a monster":
    player["health"] -= 10
    print(f"{name} got hurt during the combat with a monster, {name} now has {player["health"]} health")


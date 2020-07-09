#
#  INTERACTIVE FICTION by Eärendelmir
#  https://github.com/earendelmir
#
from os import system

# to change in "cls" if running on Windows
CLEAR_SCREEN = "clear"


class Action():
	def __init__(self, description, consequence):
		# every action has a description that will be printed out for the
		# player to get a sense of what the action does
		self.description = description
		# this value represents the identificative number of the scene that 
		# has to be displayed when the user chooses this particolar action
		self.consequence = consequence
	
	# prints the index of the action (n) and its description
	# (e.g. "1. go north")
	def print(self, n):
		print("{}. {}".format(n, self.description))



class Scene():
	def __init__(self, id, status, title, description, actions):
		# each scene has its own identificative number
		self.id = id
		# this value is != 0 when the game ends in the scene
		# it is 0 in any other case
		self.game_status = status
		# title of the scene to be printed out
		self.title = title
		# description of the scene to be printed out
		self.description = description
		# the array of actions available in the scene
		self.actions = actions
	
	# prints the current scene
	def print(self):
		# clears the screen from the previous output
		system(CLEAR_SCREEN)
		# prints the title
		print(self.title, end="\n\n")
		# prints the description
		print(self.description, end="\n\n")
		# and the actions
		for i in range(len(self.actions)):
			self.actions[i].print(i+1)
		
	# returns true if the game_status property is other than 0
	def game_over(self):
		return (self.game_status != 0)



# this function takes a number in input and returns the correspondent
# index of the action choosen by the user
def user_input(num_actions):
	# gets the string in input
	string = input("> ")
	try:
		# tries converting the string into an integer
		n = int(string, base=10)
	# but in case the string was not a number (or if it was empty)
	except ValueError:
		# it prints the error and asks again
		print("Invalid choice. You must choose a number between 1 and", num_actions)
		return user_input(num_actions)

	# checks that the input is both > 0 and < num_actions
	if (n < 1 or n > num_actions):
		print("Invalid choice. You must choose a number between 1 and", num_actions)
		return user_input(num_actions)
	else:
		# this function returns n-1 because the user can choose between 1 and N
		# but in the array, the 1st element is at index 0
		return n-1



# searches for the scene with the new_id in the array 
def next_scene(scenes, new_id, curr_id):
	# for every scene
	for i in range(len(scenes)):
		# if its id matches the one 
		if (scenes[i].id == new_id):
			# it is returned
			return scenes[i]
		# if its id matches the one of the current scene it saves that scene
		# into a variable
		elif (scenes[i].id == curr_id):
			currentScene = scenes[i]
	# the current scene is returned in case no match is found with the new id
	# this might be caused by the user re-writing the story and messing up the ids
	return currentScene



# this function prints the end credits once the game is completed
def my_credits():
	print("\nA GAME DEVELOPED BY Eärendelmir\nGITHUB: https://github.com/earendelmir", end="\n\n")
	print("This is just a demo story. You can create your own by following the instructions in the README.md file.", end="\n\n")




# the array of scenes
SCENES = [
	Scene(0, 0, "IN THE FOREST", "You wake up in the middle of a forest. You don't recall how you got here.\nOn your left there's a path leading up a hill. Right in front of you there's a chest.", [Action("Open chest.", 1), Action("Walk towards the top of the hill.", 3)]),
	Scene(1, 0, "UNUSUAL GIFTS", "You open the chest with small effort thus revealing a small bottle containing a strange blue liquid. You take it.\nThere's a note attached to the bottle; it reads: \"Drink carefully. It is not what it seems.\"", [Action("Walk towards the top of the hill.", 4), Action("Drink liquid.", 2)]),
	Scene(2, 0, "BLUEBERRY JUICE", "With great courage you take the bottle and drink its content in one big sip.\nBlueberry. It tasted like blueberries. \"That's nice!\" is the last thought that crosses your mind.\nYou collapse on the ground paralized; it's a matter of seconds before you loose conscience.", [Action("Wake up.", 0)]),
	Scene(3, 0, "THE HILL", "You start walking, hoping to recognize something.\nOnce you get on the top of the hill you find a small town by the river in the valley below.\nOn your right there's a path leading down towards the valley, on your left the same path goes upwards.", [Action("Go down towards the valley.", 5), Action("Go up.", 7)]),
	Scene(4, 0, "THE HILL", "You start walking, hoping to recognize something.\nOnce you get on the top of the hill you find a small town by the river in the valley below.\nOn your right there's a path leading down towards the valley, on your left the same path goes upwards.", [Action("Go down towards the river.", 6), Action("Go up.", 8), Action("Drink liquid.", 2)]),
	Scene(5, 0, "RIVER OF DREAMS", "You take the path leading down but as you walk a snake crosses the road scaring the life out of you!\nYou jump scared and scream like a little girl. You faint.", [Action("Wake up.", 0)]),
	Scene(6, 0, "RIVER OF DREAMS", "You take the path leading down but as you walk a snake crosses the road scaring the life out of you!\nYou jump scared and scream like a little girl. You faint.", [Action("Wake up.", 0), Action("Drink liquid.", 2)]),
	Scene(7, 0, "CLOSER TO THE GODS", "You take the path on your left that leads you to a mystic temple hidden in the clouds.", [Action("Enter the temple.", 9), Action("Go away.", 10)]),
	Scene(8, 0, "CLOSER TO THE GODS", "You take the path on your left that leads you to a mystic temple hidden in the clouds.", [Action("Enter the temple.", 9), Action("Go away.", 11), Action("Drink liquid.", 2)]),
	Scene(9, 1, "TURNING THE LIFE UPSIDE DOWN", "You enter the temple discovering a community of monks. You join them and live the rest of your life meditating.\nYou never discovered the thruth about your past.", []),
	Scene(10, 0, "THE HILL", "You reached the top of the hill. On your left a path leading upwards, on your right a path leading to a small town in the valley below.", [Action("Go down towards the valley.", 5), Action("Go up.", 7)]),
	Scene(11, 0, "THE HILL", "You reached the top of the hill. On your left a path leading upwards, on your right a path leading to a small town in the valley below.", [Action("Go down towards the valley.", 6), Action("Go up.", 8), Action("Drink liquid.", 2)]),
]




if __name__ == "__main__":
	# my game starts from the top of the array. It depends on how the story is build
	currentScene = SCENES[0]

	while (True):
		# prints the current scene
		currentScene.print()
		# checks wether it is the "last" (if the game is over) and, if it is, the loop gets broken
		if (currentScene.game_over()):
			break
		# gets in input the choice for the action to perform
		choice = user_input(len(currentScene.actions))
		# updates the value of the current scene by searching for the next one in the array
		currentScene = next_scene(SCENES, currentScene.actions[choice].consequence, currentScene.id)
	
	my_credits()

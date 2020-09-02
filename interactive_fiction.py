#
#  INTERACTIVE FICTION by Eärendelmir
#  https://github.com/earendelmir
#
from os import system


class Action():
	def __init__(self, prompt, consequence):
		# every action has a prompt that will be printed out for the player to get a sense of what the action does
		self.prompt = prompt
		# this is the identificative number of the scene that has to be displayed when the user chooses this particolar action
		self.consequence = consequence

	# prints the index of the action (n) and its prompt (e.g. "1. go north")
	def show(self, n):
		print("{}. {}".format(n, self.prompt))



class Scene():
	def __init__(self, ID, status, title, description, actions):
		self.id = ID                   # each scene has its own identificative number
		self.status = status           # this value is != 0 when the game ends in the scene
		self.title = title             # title of the scene to be printed out
		self.description = description # description of the scene to be printed out
		self.actions = actions         # the array of actions available in the scene

	# prints the current scene
	def show(self):
		# clears the screen before printing the new scene.
		system("clear") # change "clear" with "cls" if running on Windows
		print(self.title, end="\n\n")
		print(self.description, end="\n\n")
		for i in range(len(self.actions)):
			self.actions[i].show(i+1)

	# returns true if the status property is other than 0
	def gameOver(self):
		return (self.status != 0)



# this function takes a number in input and returns the correspondent index of the action choosen by the user
def userInput(num_actions):
	# gets the string in input
	string = input("> ")
	# it tries converting the string into an integer. This fails if the string is not a number or if it is empty
	try:
		n = int(string, base=10)
	except ValueError:
		print("Invalid choice. You must choose a number between 1 and", num_actions)
		return userInput(num_actions)

	# checks that the input is both > 0 and < num_actions
	if (n < 1 or n > num_actions):
		print("Invalid choice. You must choose a number between 1 and", num_actions)
		return userInput(num_actions)
	else:
		# this function returns n-1 because even though the user can choose between 1 and N, the 1st element is at index 0
		return n-1



# searches for the scene with the newID in the array
def nextScene(scenes, newID, currID):
	for i in range(len(scenes)):
		if (scenes[i].id == newID):
			return scenes[i]
		elif (scenes[i].id == currID):
			currentScene = scenes[i]
	# the current scene is returned in case no match is found with the new ID
	# this might be caused by the user re-writing the story and missing one or more IDs
	return currentScene



# This function prints the end credits once the game is completed
def myCredits():
	print("\nA GAME DEVELOPED BY Eärendelmir\nGITHUB: https://github.com/earendelmir", end="\n\n")
	print("This is just a demo story. You can create your own by following the instructions in the README.md file.", end="\n\n")




# The array of scenes. Only the 9th one has its status set to something other than 0 because it is the only scene which leads to the completion of
# the game. If you intend to rewrite the story please make sure to include one - or more, even better - scenes which lead to the end of your game.
# That way you'll be sure the player won't be stuck in the loop forever.
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
		currentScene.show()
		if (currentScene.gameOver()):
			break
		choice = userInput(len(currentScene.actions))
		currentScene = nextScene(SCENES, currentScene.actions[choice].consequence, currentScene.id)

	myCredits()

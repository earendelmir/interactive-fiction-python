# INTERACTIVE FICTION

This is a simple game I made in python in which the player has to create and develop his own adventure by making all the decisions.<br>
The story will have a different ending every time you play.<br>
Feel free to change the story as you like. It is not a difficult operation. The instructions on how to do so are below.<br>

Check out the [C version](https://github.com/earendelmir/interactive-fiction-c) I made of this project.

<p>&nbsp;</p>

# How to play:
The following is an example of a scene you will find in the game:

*****
*__OUTSIDE THE SALOON__*  
You finally reached the town.<br>
You are just outside the saloon and you hear whispers coming from the alley on your right.

**1.** _enter the saloon_
**2.** _check the alley_
__>__
*****
+ Choose one of the possible actions listed above to progress in the story.
+ Type its number
+ Press enter
+ Repeat

Eventually - by making all the right choices - you will ~~loose~~ win the game.

<p>&nbsp;</p>

# How to tweak the story:
In the source file you can find an array of _Scenes_; that is what you want to modify.<br>
Each _Scene_ has:
+ an **ID**<br>
a **_unique_** integer that identifies that particular scene.
+ a **TITLE**<br>
a string that will be printed right above the
+ **DESCRIPTION**<br>
another string which explains what the character is doing and what (s)he sees around him/her.
+ the **GAME STATUS**<br>
an integer which will be **_ANYTHING BUT 0_** if by reaching that _Scene_ the player completes (or looses) the game.<br>
It is **_0_** in any other case.
+ an **ARRAY OF ACTIONS**<br>
where each of the _N_ actions contains:
  + the **DESCRIPTION**<br>
	a string that explains the effect of that action.
  + the **CONSEQUENCE**<br>
	the **ID** of whichever _Scene_ follows the current one if the player chooses this action.

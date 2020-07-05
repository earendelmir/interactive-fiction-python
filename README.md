# INTERACTIVE FICTION

This is a simple game I made in python in which the player has to create and develop his own adventure by making all the decisions.  
The story will have a different ending every time you play.

Bear in mind I did not implement a way to save or load progress. The story I developed is short and it wouldn't take more than 5 minutes to finish it.

<p>&nbsp;</p>

# Compile and run:
Run this command to play:
<pre><code>python3 interactive_fiction.py</pre></code>

<p>&nbsp;</p>

# How to play:
The following is an example of a scene you will find in the game:

*****
*__OUTSIDE THE SALOON__*  
You finally reached the town.  
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
In the source file you can find an array of _Scenes_; that is what you want to modify.  
Each _Scene_ has:
+ an **ID**  
a **_unique_** integer that identifies that particular scene.
+ a **TITLE**  
a string that will be printed right above the
+ **DESCRIPTION**  
another string which explains what the character is doing and what (s)he sees around him/her.
+ the **GAME STATUS**  
an integer which will be **_EVERYTHING BUT 0_** if by reaching that _Scene_ the player completes (or looses) the game.  
It is **_0_** in any other case.
+ the **NUMBER OF ACTIONS**  (only in the *C* version)  
an integer which stores the number of actions that the player can perform in that _Scene_.
+ an **ARRAY OF ACTIONS**  
where each of the _N_ actions contains:
  + the **DESCRIPTION**  
	a string that explains the effect of that action.
  + the **CONSEQUENCE**  
	the **ID** of whichever _Scene_ follows the current one if the player chooses this action.
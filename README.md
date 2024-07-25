# Flappy Bird

## Objectives

- Understanding:
  - Variable types
  - Loops
  - if / then statements
  - classes / objects
  - import statemets (using external code)

## What elements do we need for our game?

- Canvas -- A place to draw the elemets of the game
- Objects -- Not in the sense of a Python object, just the things that need to be drawn on the canvas
  - Player characters
  - Obstacles
- Logic
  - Is the player moving? Which direction?
  - Has the player passed an obstacle?
  - Has the player collided with an obstacle?
  - Has the player gone off the screen?
- State
  - What is the location of the player?
  - What are the locations of the objects?
  - What is the size of the game grid?
  - What is the player's score?
  - What is the game speed? (i.e. how much time between each frame of the game animation)

## Getting Started

Ensure that you have installed the dependencies for this project. You can do this
by running `pip install -r requirements.txt` from the root directory of your
project folder. This will install all external libraries you need, which are specified in the `requirements.txt` file. There should be only one library, `keybaord` that is required, but using a requirements file makes it easy for other people using your code to install the correct dependencies without having to know exactly what they are.

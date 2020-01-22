from pygame_functions import *
import random
screenSize(800,800)

# This demo shows you the textBox (for easy typed input) and the label (for text output)


instructionLabel = makeLabel("Please enter a word", 40, 10, 10, "blue", "Agency FB", "yellow")
showLabel(instructionLabel)

wordBox = makeTextBox(10, 80, 300, 0, "Enter text here", 15, 24)
showTextBox(wordBox)
hideLabel(instructionLabel)
endWait()
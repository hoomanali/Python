# Ali Hooman
# alhooman@ucsc.edu
#
# Class Problem 21: Dice rolling

from flask import Flask
from random import randrange

app = Flask("CMPS5P Class Problem 21")

@app.route("/")
def roll_dice():
    print("test")
    dice = randrange(1,7)
    roll = str(dice)
    return roll

app.run(debug=True)

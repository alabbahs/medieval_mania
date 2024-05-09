# medieval_mania

This is my capstone project for the Sigma Labs pre-work.

The project is a turn based terminal game named Medieval Mania.

Medieval Mania is meant to simulate warfare in the medieval era, around the 12-13th century, there are four armies to pick from, the Mongols, Japanese, Romans and Mamluks.

Simply, the player and the cpu they are battling against, each have a turn at engaging the other in battle.

Each army has a light, medium and heavy unit that can be used in warfare, each with unique names. The concept is a glorified Rock, Paper, Scissors game where the heavy unit beats the medium unit, the medium unit beats the light unit and the light unit beats the medium unit however, instead of outright winning or losing, the units do varying levels of damage to each units respective army.

To spice up the logistics of these wars, I added a terrain element, where each army has a turn to essentially roll the dice on what terrain they get to engage the other army on, each unit (light, medium and heavy) is advantaged or disadvantaged by different terrains.

The light units are advantaged on the Forest terrain, the medium units have an advantage on the Open Field and the heavy units have the edge on the Hill. These terrains will give a boost or stunt to the attacking units when engaging with the opposing force.

I will outline the point system in a spreadsheet payoff matrix that you can access here: https://docs.google.com/spreadsheets/d/12W1S7lyT0v5sPfmN9g8eNwuOaWGndYJDAPtB236EQdw/edit?usp=sharing


How to play:

Start by running the python file, the only imported module is random for now, there might be additions later that require you to install external packages before running the game.

You will be met with a main menu screen and have the ability to navigate between 1. Play Game 2. How to Play 3. Quit Game.

by entering 1, 2 or 3 this will select the options at hand, this is the layout for all your actions in the game, you will be prompted to enter a number given certain options and your input is a number that corresponds to one of the options. N.B that when an invalid input is entered you will be asked to re-enter one of the given options.

When playing the game it will ask you to pick and empire and then the war starts, you will be fighting three wars with the remaining armies that you didn't select.

Each war will consist of turns striking each other until one of the armies health falls to (or below) zero.

Since you are taking turns attacking, only the attacking turn will give you a prompt to enter and roll the dice for a random terrain to fight on, adding an extra dimension of uncertainty and luck, as with real life warfare.

once the war is finished, you will proceed until the next army and repeat the same until all three wars have been fought.

Given your score out of all three wars, you will be given a medal of honour or shame named with an appropriate historical counterpart.

3-0 THE KHANS TRIUMPH.

2-1 Sun Tzu's Success.

1-2 Hannibal's Retreat.

0-3 Napoleons Waterloo.

The game will then execute the program when finished and you will have to rerun the python program to play again.
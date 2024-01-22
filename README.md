## Card Creation Tool
This project is a tool to help facilitate card generation for a card game. The user should provide a CSV file with the correct headers so that the python program can use each data entry to generate cards. Headers are General Name,Specific Card Name,Tags,Rules Text,Card Type,Card Functionality Type,Mana Cost,Flavor Text. The program will then draw the text data taken from the CSV onto a provided image and save the image in its specified path. The Program will avoid duplicate card image names by enumerating the name where conflicts arise.

The artFinder script opens each image in the art folder and only draws these images to their corresponding card. It will not alter the cards without art in any way and will save the cards with art in the 'final' folder. 



### Built in Python and utilizing Pillow
This is a work in progress

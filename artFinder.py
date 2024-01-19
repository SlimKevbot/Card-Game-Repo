#This script will open up our art folder and open the corresponding card from the deck folder
#then it will paste the art atop the card and save the final card to a separate folder
import csv
import os
import textwrap
import shutil
from PIL import Image, ImageDraw, ImageFont

def main():
    #do something
    myDeck = 'deck1'
    outputFolder = 'final'
    myArt = 'art'

    if os.path.exists(outputFolder):
        #folder exists empty contents
        for file_name in os.listdir(outputFolder):
            file_path = os.path.join(outputFolder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        # Folder doesn't exist, create it
        os.makedirs(outputFolder)

    openArt(outputFolder, myArt)

def openArt(outputFolder, artFolder):
    for file_name in os.listdir(artFolder):
        base_name, extension = os.path.splitext(file_name)
        myCard = base_name
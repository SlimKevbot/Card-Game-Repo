#This script will open up our art folder and open the corresponding card from the deck folder
#then it will paste the art atop the card and save the final card to a separate folder
import os
import shutil
from PIL import Image
def main():
    #folder variables
    blankCardFolder = 'deck1'
    outputFolder = 'final'
    myArtFolder = 'art'

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

    openArt(outputFolder, myArtFolder, blankCardFolder)

def openArt(outputFolder, artFolder, blankCardFolder):
    for file_name in os.listdir(artFolder):
        myArtPath = os.path.join(artFolder, file_name) #set path for the art we wish to access
        base_name, extension = os.path.splitext(file_name)
        blankCardPath = f'{blankCardFolder}/{base_name}_card.png'
        myOutputPath = f'{outputFolder}/{base_name}_card.png'

        #now find myCard in the deck folder
        if os.path.exists(blankCardPath):
            textCard = Image.open(blankCardPath)
            myArtImage = Image.open(myArtPath).convert("RGBA")
            max_width = textCard.width - 2 * 150  # Adjust the margin as needed
            max_height = textCard.height - 2 * 150
            myArtImage.thumbnail((max_width, max_height))
            textCard.paste(myArtImage, (150, 125), myArtImage)  # Adjust the position as needed
            #Save the generated image in the Final Folder
            textCard.save(myOutputPath) #this just needs to be a path name. We are saving the image as this path name
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 
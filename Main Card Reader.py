#General Name,Specific Card Name,Tags,Rules Text,Card Type,Card Functionality Type,Mana Cost,Flavor Text
#This program will loop through a CSV to create 69 unique cards for a card game

import csv
import os
from PIL import Image, ImageDraw, ImageFont

def main():
    #do something
    csv_path = 'card_table.csv'
    blankCardPath = 'mtgcard.jpg'
    output_folder = 'deck1'
    num_cards = 10

    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count ==0:
                print(f'Column names are {",".join(row)}')
                line_count += 1 #this ensures that the first row is named so that we understand what is going on
            else:
                print(f'card {line_count} {",". join(row)} ')
                line_count += 1
        print(f'Processesd {line_count} lines.')

    generate_cards(csv_path, blankCardPath, output_folder, num_cards)



def create_card_image(trueName, tags, rules, mana, flavorText, blankCardPath, outputPath, output_folder):
    #open the template image
    blankCard = Image.open(blankCardPath)
    #get a drawing context
    draw = ImageDraw.Draw(blankCard)
    #load font
    font_path = "/path/to/DejaVuSans.ttf"
    myFont = ImageFont.truetype("arial.ttf", 30)
    #define the text position
    trueNamePos = (65,60)
    tagsPos = (70,590) #the card class type
    rulesPos = (70, 650)
    flavorTextPos = (65, 700)
    manaPos = (550, 925)
    #draw the text on the image
    draw.text(trueNamePos, f"Name: {trueName}", font=myFont, fill="red")
    draw.text(rulesPos, f"rules: {rules}", font=myFont, fill="red")
    draw.text(flavorTextPos, f"Flavor: {flavorText}", font=myFont, fill="red")
    draw.text(manaPos, f"Mana: {mana}", font=myFont, fill="red")
    draw.text(tagsPos, f"Tags: {tags}", font=myFont, fill="red")
    
    # Check if the file already exists, add a counter to the filename if needed
    counter = 1
    while os.path.exists(outputPath):
        outputPath = f"{output_folder}/{trueName.replace(' ', '_')}_{counter}_card.png"
        counter += 1

    #save the card with the general name as the image name
    blankCard.save(outputPath)

def generate_cards(csv_path, blankCardPath, output_folder, num_cards):
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for i, row in enumerate(reader):
            if i >= num_cards:
                break
            generalName = row['ï»¿General Name']
            trueName = row['Specific Card Name']
            tags = row['Tags']
            rules = row['Rules Text']
            card_type = row['Card Type']
            card_func = row['Card Functionality Type']
            mana = row['Mana Cost']
            flavorText = row['Flavor Text']
            #generate the unique file name for each card image
            print(f"#{i} card generating.")
            outputPath = f"{output_folder}/{trueName.replace(' ', '_')}_card.png"
            #call the create a card function
            create_card_image(trueName, tags, rules, mana, flavorText, blankCardPath, outputPath, output_folder)

# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 
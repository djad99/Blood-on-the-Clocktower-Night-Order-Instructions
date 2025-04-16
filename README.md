# BOTC Night Order Generator

This project is used to generate a CSV file of night order charts from a JSON file in the Blood on the Clocktower old JSON format. 

This is a fan project and is no way officially affiliated with The Pandemonium Institude or any other entities realted to Blood on the Clocktower. 

## Setup
### From Python Code
To use this from the code, make sure you have the following
1) The python script itself as well as Python 3 installed on your development environment. 
2) The night.json file provided within the same folder as the python script. This has an entry for every character currently released up to the Wizard, with a night order instruction.
3) An Output_CSV_files folder within the folder you have the python script.
4) An Output_Night_Order_Sheets within the folder you have the python script.
5) The BOTC JSON scripts that you wish to turn into night order. The current iteration only supports the new format for JSON scripts (the same format received from script.bloodontheclocktower.com). These can be placed anywhere with the new GUI changes.

### Using prebuilt executable
There is a prebuilt executable that is much easier to use for people who don't want to bother installing Python on their computers.
Simply unzip the executable and run the application from the directory you unzipped it from.

## Start Menu
There is a GUI now available to use the tool properly. You can add a character or create a night chart by clicking the applicable buttons.
You may execute either action as many times as you want.

## Custom Night Order Files
### CURRENTLY DISABLED DUE TO GUI CHANGES

Occasionally, a user may want to create a homebrew character that wakes at night, or use a whole script full of them. Never fear, this
tool can accommodate! The second question asked of the prompt will be asking if you want to use a custom night order. Simply enter something 
with 'y' in it and then it will prompt you to enter in a file name. Enter in a valid file name or the program will crash, you have been warned. 

If you are creating a character sheet with none of the official characters, I strongly recommend using the night_template.json file as a 
starting spot. Copy it to another file by whatever name you wish, and add characters to it. The template contains Dusk, Travelers, Minion
Info, Demon Info, and Dawn by default. 

If you want to throw in a homebrew character on top of the normal night order, I would do the same as above but with the night.json file. 

## Adding/Updating a character
It is expected that TPI will continue releasing characters in the game for the foreseeable future. As such, there is a way to add characters that have night order instructions into the tool.

The expectation is that when the new character is released, anyone who desires to update the night order chart could go and grab a fishbucket script (like the one found here: https://botc-scripts.azurewebsites.net/script/all_roles), load it into the official app, and enter in the needed information here in the appropriate text boxes. Then click the button to add the character, and everything is alright.

If a character that already exists is added your entry will override the previous entry on the nights you upload. It will not, however, update say if a character that originally woke on the first night no longer wakes up on that night.

## Creating a night chart
The primary function of this application. Simply load in your script in the input button (it will open a dialog to navigate your file system) as well as your printable height.

This assumes legal paper (8.5" Width by 14" Height) and roughly 10.5-11 inches of that is printable, by default I recommend using 10.5 to 11 as your input. However if you want to make it shorter because it's a Teensyville or you want to stretch the limits, the option is there. The output will be spit out to Output_Night_Order_Sheets/<SCRIPT>_Formatted_Night.docx

If you do not think the formatting here is what you want and you want to just have the raw information and do it yourself, the csv file with just the night order information is output to Output_CSV_files/<SCRIPT>_Night_Order.csv
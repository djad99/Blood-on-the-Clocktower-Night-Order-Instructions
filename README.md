# BOTC Night Order Generator

This project is used to generate a CSV file of night order charts from a JSON file in the Blood on the Clocktower old JSON format. 

This is a fan project and is no way officially affiliated with The Pandemonium Institude or any other entities realted to Blood on the Clocktower. 

## Setup

To use this, make sure you have the following
1) The python script itself as well as Python 3 installed on your development environment. 
2) The night.json file provided within the same folder as the python script. This has an entry for every character currently released 
as of 3/25/2024, with a night order instruction. 
3) The Input_Json_files folder within the folder you have the python script. 
4) An Output_CSV_files folder within the folder you have the python script.
5) The BOTC json scripts in the old format that you wish to turn into night order (the current iteration does not support the new format, 
however there is a script I've made to go between the script formats). 

## Custom Night Order Files
Occassionally, a user may want to create a homebrew character that wakes at night, or use a whole script full of them. Never fear, this
tool can accomodate! The second question asked of the prompt will be asking if you want to use a custom night order. Simply enter 1 and 
then it will prompt you to enter in a file name. Enter in a valid file name or the program will crash, you have been warned. 

If you are creating a character sheet with none of the official characters, I strongly recommend using the night_template.json file as a 
starting spot. Copy it to another file by whatever name you wish, and add characters to it. The template contains Dusk, Travelers, Minion
Info, Demon Info, and Dawn by default. 

If you want to throw in a homebrew character on top of the normal night order, I would do the same as above but with the night.json file. 

## Adding a character
When a new character is added to Blood on the Clocktower, you should add it to the night order json, this automates the task of updating the
order position for each character. Only do this if the new character has a position in either night order.

When you boot the application, it will ask an initial start question of if you want to add a character or create a night order chart: Enter '1'

After this, there will be a series of questions asked, here are the questions below. 
The questions asked:
### New Character Name 
Fill in the character name as written on the character token

### 1) First Night, 2) Other Nights, 3) Both
Enter in 1 if the character wakes only on the first night, enter 2 if the character only wakes 
on each night except the first, enter 3 if the character wakes every night.

### If they wake the first night
#### New Character First Night Description
Fill in the official description of the new character on the first night. (can be accessed from online.bloodontheclocktower.com)

#### What character do they go after in first night order: 
Enter in the name of the character directly before the new character in the night order.

### If they wake on a night other than the first
#### New Character Other Night Description
Fill in the official description of the new character on the other night (can be accessed from online.bloodontheclocktower.com)

#### What character do they go after in other night order
Enter in the name of the character directly before the new character in the night 
order. 

### New Character Alignment - Enter in the alignment of the character


## Creating a night chart
The primary function of this application. When you boot the application, it will ask if you want to add a character or create a night order 
chart. Enter '2' (technically any non 1 integer will do the trick)

After this it will ask you to input a file name. Enter the name of the json file in the Input_Json_files folder you want to create a night chart 
out of. 

It will then output the name of the script, then ask if it is a Teensyville script or a full script. If you enter '0' for a Teensyville script,
this will just add the characters to the night order chart on the script, dusk, and dawn. If you enter '1' for a full script, this will add 
everything in the Teensyville script, a night order position for all Travellers, and Minion and Demon info steps. It will output the csv file
into the Output_CSV_files folder. From there you can take it and format it however you wish. 

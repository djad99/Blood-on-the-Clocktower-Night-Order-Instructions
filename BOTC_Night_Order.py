import json

file_name = ""

# night order on the first night
first_night_order = []
# night order on other nights
other_night_order = []

# Character names that appear on night one
night_one_characters = []
# Character names that appear on other nights
night_x_characters = []
# Global file with the json data from night.json
night_file = json.load(open('night.json', 'r'))
night_file_name = "night.json"


# This will populate the night_one_characters and night_x_characters arrays
def init_characters():
  for i in night_file["first_night_characters"]:
    night_one_characters.append(i)

  for i in night_file["other_night_characters"]:
    night_x_characters.append(i)


# This will scan through the passed in .json file and if there is a first night
# wake, add that to the first night order. If there is a wake on other nights,
# add that to the other night order
def found_character(character_name):
  if character_name in night_one_characters:
    first_night_order.append(night_file["first_night"][character_name])

  if character_name in night_x_characters:
    other_night_order.append(night_file["other_night"][character_name])


# This will scan a script's json file provided in the same format as the
# official script tool return a list of all the characters in the script
def search_script(script_file_name):
  script_file = json.load(open(script_file_name))
  characters_appearing = []
  for i in script_file:
    if i['id'] != '_meta':
      characters_appearing.append(i['id'])

  return characters_appearing


def transform_character_name(character_name):
  character_name = character_name.lower()
  character_name = character_name.replace(" ", "_")
  character_name = character_name.replace("'", "")
  return character_name


# This method sorts the night orders by order_pos, using Selection Sort
def sort_night_order():

  for i in range(len(first_night_order)):
    min = first_night_order[i][3]['order_pos']
    min_index = i
    for j in range(i + 1, len(first_night_order)):
      if first_night_order[j][3]['order_pos'] < min:
        min = first_night_order[j][3]['order_pos']
        min_index = j

    first_night_order[i], first_night_order[min_index] = first_night_order[
        min_index], first_night_order[i]

  for i in range(len(other_night_order)):
    min = other_night_order[i][3]['order_pos']
    min_index = i
    for j in range(i + 1, len(other_night_order)):
      if other_night_order[j][3]['order_pos'] < min:
        min = other_night_order[j][3]['order_pos']
        min_index = j

    other_night_order[i], other_night_order[min_index] = other_night_order[
        min_index], other_night_order[i]


# This will create the night order and output the night order
def create_night_order(file_name_begin):
  # adding the boiler plate night order spots in every script
  found_character("dusk")
  found_character("dawn")

  # adding full script info if it's a full script
  if (int(input("Is this a Teensyville (0) or a full script (1): "))) == 1:
    found_character("demon_info")
    found_character("minion_info")
    found_character("travelers")

  sort_night_order()

  with open("Output_CSV_files/" + file_name_begin + "_Night_Order.csv",
            'w') as f:
    for i in first_night_order:
      f.write(i[0]["name"] + " ,|," + '"' + i[1]["description"] + '"\n')
    f.write("\n\n\n\n\n")

    for i in other_night_order:
      f.write(i[0]["name"] + " ,|," + '"' + i[1]["description"] + '"\n')

# This drives night order instructions creation. Read the script, see what characters on the script have night order instructions, 
# then put those characters in a proper order. (Characters include dawn, dusk, and possibly travelers, Minion Info, and Demon Info. 
def create_chart():
  file_name = input("Enter the script file name: ")
  characters = search_script("Input_Json_files/" + file_name)
  file_name = file_name.replace(".json", "")
  print(file_name)
  for character in characters:
    found_character(character)

  create_night_order(file_name)

# This function drives adding a character. In short, it reads in the user input on the character data, finds the character
# that the new character is after (assuming all characters will be after dawn, will get around to changing that if the need
# arises), and remakes the json file with the correct night order placements. If the game was thousands of characters long 
# that's inefficient, but given we have a low upper bound around 250 characters (227 is the count, round up because homebrew),
# this is fine.
def add_character():
  name = input("New Character Name: ")
  nights = int(input("1) First Night, 2) Other Nights, 3) Both: "))
  first_night_description = ""
  first_night_order_pos = ""
  other_night_description = ""
  other_night_order_pos = ""

  if nights != 2:
    first_night_description = input("New Character First Night Description: ")
    first_night_order_pos = transform_character_name(
        input("What character do they go after in first night order: "))
  if nights != 1:
    other_night_description = input("New Character Other Night Description: ")
    other_night_order_pos = transform_character_name(
        input("What character do they go after in other night order: "))

  first_night_alignment = input("New Character alignment: ")

  if first_night_order_pos != "":
    spot_to_add_character = night_one_characters.index(first_night_order_pos)
    night_one_characters.insert(spot_to_add_character + 1, name.lower())
    first_night_addition = [{
        "name": name.title()
    }, {
        "description": first_night_description
    }, {
        'default_alignment': first_night_alignment.title()
    }, {
        "order_pos":
        night_one_characters.index(name.lower()) + 1
    }]

    for character in night_file["first_night"]:
      night_file["first_night"][character][3][
          "order_pos"] = night_one_characters.index(character) + 1

    night_file["first_night"].update({name.lower(): first_night_addition})
    night_file["first_night_characters"].insert(spot_to_add_character + 1,
                                                name.lower())

  if other_night_order_pos != "":
    spot_to_add_character = night_x_characters.index(other_night_order_pos)
    night_x_characters.insert(spot_to_add_character + 1, name.lower())
    other_night_addition = [{
        "name": name.title()
    }, {
        "description": other_night_description
    }, {
        'default_alignment': first_night_alignment.title()
    }, {
        "order_pos":
        night_x_characters.index(name.lower()) + 1
    }]

    for character in night_file["other_night"]:
      night_file["other_night"][character][3][
          "order_pos"] = night_x_characters.index(character) + 1

    night_file["other_night"].update({name.lower(): other_night_addition})
    night_file["other_night_characters"].insert(spot_to_add_character + 1,
                                                name.lower())

  with open(night_file_name, 'w') as f:
    json.dump(night_file, f, indent=4)

choice = int(input("Would you like to 1) add a character to the night order or 2) create a night order chart: "))

# These three lines allow for a custom character list to be used
if int(input("Do you want to do this to a custom character list (1) or the default (0): ")) != 0:
  night_file_name = input("Enter the custom character list filename: ")
  night_file = json.load(open(night_file_name, 'r'))
  
init_characters()
if choice == 1:
  add_character()
else:
  create_chart()

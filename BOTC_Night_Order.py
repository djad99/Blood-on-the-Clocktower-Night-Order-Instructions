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
night_file = json.load(open("night.json"))

print(night_file)


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

    with open("Output_CSV_files/" + file_name_begin + "_Night_Order.csv", 'w') as f:
        for i in first_night_order:
            f.write(i[0]["name"] + " ,|," + '"' + i[1]["description"] + '"\n')
        f.write("\n\n\n\n\n")

        for i in other_night_order:
            f.write(i[0]["name"] + " ,|," + '"' + i[1]["description"] + '"\n')


def create_chart():
    file_name = input("Enter the script file name: ")
    characters = search_script("Input_Json_files/" + file_name)
    file_name = file_name.replace(".json", "")
    print(file_name)
    for character in characters:
        found_character(character)

    create_night_order(file_name)


def add_character():
    name = input("New Character Name: ")
    nights = int(input("1) First Night, 2) Other Nights, 3) Both: "))
    first_night_description = ""
    first_night_order_pos = ""
    other_night_description = ""
    other_night_order_pos = ""

    first_night_json = night_file["first_night"]
    other_night_json = night_file["other_night"]

    if nights != 2:
        first_night_description = input("New Character First Night Description: ")
        first_night_order_pos = input("What character do they go after in first night order: ").lower()
    if nights != 1:
        other_night_description = input("New Character Other Night Description: ")
        other_night_order_pos = input("What character do they go after in other night order: ").lower()

    first_night_alignment = input("New Character alignment: ")

    if first_night_order_pos != "":
        spot_to_add_character = night_one_characters.index(first_night_order_pos)
        night_one_characters.insert(spot_to_add_character + 1, name.lower())
        first_night_addition = [{"name": name.title()},
                                {"description": first_night_description},
                                {'default_alignment': first_night_alignment.title()},
                                {"order_pos": night_one_characters.index(name.lower()) + 1}]

        for character in night_file["first_night"]:
            night_file["first_night"][character][3]["order_pos"] = night_one_characters.index(character) + 1

        night_file["first_night"].update({name.lower(): first_night_addition})
        night_file["first_night_characters"].append(name.lower())

    if other_night_order_pos != "":
        spot_to_add_character = night_x_characters.index(other_night_order_pos)
        night_x_characters.insert(spot_to_add_character + 1, name)
        other_night_addition = [{"name": name.title()},
                                {"description": first_night_description},
                                {'default_alignment': first_night_alignment.title()},
                                {"order_pos": night_one_characters.index(name.lower()) + 1}]

        for character in night_file["other_night"]:
            night_file["other_night"][character][3]["order_pos"] = night_x_characters.index(character) + 1

        night_file["other_night"].update({name.lower(): other_night_addition})
        night_file["other_night_characters"].append(name.lower())

    with open("night.json", 'w') as f:
        json.dump(night_file, f, indent=4)


#init_characters()
#choice = int(input("Would you like to 1) add a character to the night order or 2) create a night order chart: "))

#if choice == 1:
    #add_character()
#else:
    #create_chart()


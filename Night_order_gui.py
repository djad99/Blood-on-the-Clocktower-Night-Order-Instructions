import tkinter as tk
from tkinter import filedialog as fd
import Night_order_creation

page_attributes = []
root = tk.Tk()
filename = ""

def createStartPage():
    destroyPage()
    night_order_button = tk.Button(root, text="Create Night Order", command=createNightOrderGUI)
    add_character_button = tk.Button(root, text="Add Character", command=addCharacterGUI)
    night_order_button.pack()
    add_character_button.pack()
    page_attributes.append(night_order_button)
    page_attributes.append(add_character_button)

def destroyPage():
    global page_attributes
    for attribute in page_attributes:
        attribute.destroy()
    page_attributes.clear()

def selectFile():
    global filename
    filetypes = [
        ('Json', '*.json')
    ]

    filename = fd.askopenfilename(title="Choose a script:", initialdir="Input_Json_Files/", filetypes=filetypes)
    print(filename)

def createNightOrderGUI():
    destroyPage()
    global filename
    script_label = tk.Label(root, text="Input script in Input_Json_Files/:")
    script_button = tk.Button(root, text="Choose script", command=selectFile)
    script_label.grid(column=0, row=0, sticky=tk.W)
    script_button.grid(column=1, row=0)

    printable_label = tk.Label(root, text="Printable Height (in.):")
    printable_entry = tk.Entry(root)
    printable_label.grid(column=0, row=1, sticky=tk.W)
    printable_entry.grid(column=1, row=1)

    status_label = tk.Label(root, text="")

    create_night_button = tk.Button(root, text="Create Night sheet", command=lambda : Night_order_creation.create_chart(filename, status_label, printable_entry.get()))
    create_night_button.grid(column=0, row=2)
    return_button = tk.Button(root, text="Return to start", command=createStartPage)
    return_button.grid(column=1, row=2)
    status_label.grid(column=0, row=3)

    page_attributes.append(script_label)
    page_attributes.append(script_button)
    page_attributes.append(create_night_button)
    page_attributes.append(printable_label)
    page_attributes.append(printable_entry)
    page_attributes.append(return_button)
    page_attributes.append(status_label)

def addCharacterGUI():
    destroyPage()
    row_num = 0
    name_label = tk.Label(root, text="Name:")
    name_entry = tk.Entry(root)
    name_label.grid(column=0, row=row_num, sticky=tk.W)
    name_entry.grid(column=1, row=row_num)

    row_num += 1
    
    first_night_label = tk.Label(root, text="First night description:")
    first_night_entry = tk.Entry(root)
    first_night_label.grid(column=0, row=row_num, sticky=tk.W)
    first_night_entry.grid(column=1, row=row_num)

    row_num += 1

    first_night_anchor_label = tk.Label(root, text="What character does this one go after:")
    first_night_anchor_entry = tk.Entry(root)
    first_night_anchor_label.grid(column=0, row=row_num, sticky=tk.W)
    first_night_anchor_entry.grid(column=1, row=row_num)

    row_num += 1

    other_night_label = tk.Label(root, text="Other night description:")
    other_night_entry = tk.Entry(root)
    other_night_label.grid(column=0, row=row_num, sticky=tk.W)
    other_night_entry.grid(column=1, row=row_num)

    row_num += 1

    other_night_anchor_label = tk.Label(root, text="What character does this one go after:")
    other_night_anchor_entry = tk.Entry(root)
    other_night_anchor_label.grid(column=0, row=row_num, sticky=tk.W)
    other_night_anchor_entry.grid(column=1, row=row_num)

    row_num += 1

    alignment = tk.StringVar()
    alignment.set("good")

    good = tk.Radiobutton(root, text="Good", variable=alignment, value="good")
    evil = tk.Radiobutton(root, text="Evil", variable=alignment, value="evil")
    good.grid(column=0, row=row_num)
    evil.grid(column=1, row=row_num)

    row_num += 1

    status_label = tk.Label(root, text="")
    status_label.grid(column=0, row=row_num+1)
    add_character_button = tk.Button(root, text="Add character!", command= lambda: Night_order_creation.add_character(name_entry.get(), 
                                                                                                                      first_night_entry.get(), 
                                                                                                                      first_night_anchor_entry.get(), 
                                                                                                                      other_night_entry.get(), 
                                                                                                                      other_night_anchor_entry.get(), 
                                                                                                                      alignment.get(),
                                                                                                                      status_label))
    add_character_button.grid(column=0, row=row_num)
    return_button = tk.Button(root, text="Return to start", command=createStartPage)
    return_button.grid(column=1, row=row_num)

    row_num += 1

    page_attributes.append(name_label)
    page_attributes.append(name_entry)
    page_attributes.append(return_button)
    page_attributes.append(add_character_button)
    page_attributes.append(first_night_label)
    page_attributes.append(other_night_label)
    page_attributes.append(first_night_entry)
    page_attributes.append(other_night_entry)
    page_attributes.append(first_night_anchor_label)
    page_attributes.append(other_night_anchor_label)
    page_attributes.append(first_night_anchor_entry)
    page_attributes.append(other_night_anchor_entry)
    page_attributes.append(good)
    page_attributes.append(evil)
    page_attributes.append(status_label)


def createGUI():
    root.title("BOTC Night order creation")
    root.geometry("600x400")
    Night_order_creation.init_characters()
    createStartPage()
    root.mainloop()

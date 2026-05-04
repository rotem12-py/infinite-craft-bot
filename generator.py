from conv import convert
import json

with open("discoveries.json", "r", encoding="utf-8") as f:
    current_data = json.load(f)

more = True

while more:
    name = input("Name the element: ")
    emoji = input("Emoji: ")
    index = input("Index of the element: -1 for last, 0 for first, or n for next item to be checked")

    new_element = {"name": name, "emoji": emoji, "is_first_discovery": False}

    if index.isdigit():
        index = int(index)
        current_data.append(new_element)
    else:
        with open("checked.txt") as f:
            checked = set(f.read().splitlines())
            current_data.insert(len(checked), new_element)


    with open("discoveries.json", mode="w", encoding="utf-8") as f:
        json.dump(current_data, f, indent=4)

    more = input("Another? Y:n ").lower()

    if more == "Y".lower():
        continue
    else:
        break




convert()


from datetime import datetime
import json

while True:
    try:
        with open('diary.json', "r") as f:
            entry = json.load(f)
    except FileNotFoundError:
        entry = {}

    command = input("Enter your command: ")
    parts = command.split()

    if parts[0].lower() == "add":
        data = " ".join(parts[1:])
        entry[datetime.now().strftime("%d %b %Y, %I:%M:%S %p")] = data
        with open('diary.json', 'w') as f:
            json.dump(entry, f)
        print("Entry added")

    elif parts[0].lower() == "read":
        if not entry:
            print("No entries yet.")
        else:
            for timestamp, text in entry.items():
                print(f"{timestamp}  —  {text}")

    elif parts[0].lower() == "search":
        data = " ".join(parts[1:])
        if not entry:
            print("No entries yet.")
        else:
            found = False
            for timestamp, text in entry.items():
                if data in text:
                    print(f"{timestamp}  —  {text}")
                    found = True
            if not found:
                print(f"No entries containing '{data}'")

    elif parts[0].lower() == "quit":
        break
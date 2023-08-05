import json
import os
import uuid
from datetime import datetime


def get_value(value):

    if value == '1':
        header = input("Enter header of note: ")
        body = input("Enter body of note: ")
        time = datetime.now().strftime("%D, %H:%M:%S")
        dictionary = {
            "ID": f"{uuid.uuid4()}",
            "Header": header,
            "Body": body,
            "Created time": time
        }
        json_object = json.dumps(dictionary, indent=4)
        with open(f"notes/{header}.json", "w") as f:
            f.write(json_object)

    elif value == '2':
        try:
            name = input("Enter name of note: ")
            with open(f"notes/{name}.json", 'r+') as f:
                header = input("Enter new header of note: ")
                body = input("Enter new body of note: ")
                time = datetime.now().strftime("%D, %H:%M:%S")
                data = json.load(f)
                dictionary = {
                    "ID": data['ID'],
                    "Header": header,
                    "Body": body,
                    "Created time": data['Created time'],
                    "Updated time": time
                }
                f.seek(0)
                json.dump(dictionary, f, indent=4)
                f.truncate()
            os.rename(f"notes/{name}.json", f"notes/{header}.json")
            print('Success!\n')
        except Exception:
            print("There is no such file, please try again!\n")

    elif value == '3':
        name = input("Enter name of note: ")
        try:
            with open(f"notes/{name}.json", 'r') as f:
                data = json.load(f)
                print(' ')
                for i in data:
                    print(f"{i}: {data[i]}")
                print(' ')
        except Exception:
            print("There is no such file, please try again!\n")
            
    elif value == '4':
        name = input("Enter name of note: ")
        try:
            os.remove(f"notes/{name}.json")
            print("Success!\n")
        except Exception:
            print("There is no such file, please try again!\n")

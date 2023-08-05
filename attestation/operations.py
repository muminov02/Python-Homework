from datetime import datetime
import uuid, os

def get_value(value):

    if value == '1':
        header = input("Enter header of note: ")
        body = input("Enter body of note: ")
        time = datetime.now().strftime("%D, %H:%M:%S")
        with open(f"notes/{header}.txt", "w") as file:
            file.writelines(f"ID: {uuid.uuid4()}\n")
            file.writelines(f"Header: {header}\n")
            file.writelines(f"Body: {body}\n")
            file.writelines(f"Created time: {time}\n")

    elif value == '2':
        name = input("Enter name of note: ")
        try:
            with open(f"notes/{name}.txt", "r") as file:
                data = file.readlines()
                print("Old data:\n", data[0], data[1], data[2], data[3])
                header = input("Enter new header of note: ")
                body = input("Enter new body of note: ")
                time = datetime.now().strftime("%D, %H:%M:%S")
            with open(f"notes/{name}.txt", "w") as file:
                file.writelines({data[0]})
                file.writelines(f"Header: {header}\n")
                file.writelines(f"Body: {body}\n")
                file.writelines(data[3])
                file.writelines(f"Updated time: {time}\n")
            os.rename(f"notes/{name}.txt", f"notes/{header}.txt")
        except Exception:
            print("There is no such file, please try again!\n")

    elif value == '3':
        name = input("Enter name of note: ")
        try:
            with open(f"notes/{name}.txt", "r") as file:
                print(file.read())
        except Exception:
            print("There is no such file, please try again!\n")
    elif value == '4':
        name = input("Enter name of note: ")
        try:
            os.remove(f"notes/{name}.txt")
        except Exception:
            print("There is no such file, please try again!\n")

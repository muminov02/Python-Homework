import operations

def main_menu():
    work = True
    while work:
        answer = input(
            "\nNotes\n"
            "1. Create note\n"
            "2. Edit note\n"
            "3. Read note\n"
            "4. Delete note\n"
            "5. Exit\n"
        )
        match answer:
            case "1":
                operations.get_value(answer)
            case "2":
                operations.get_value(answer)
            case "3":
                operations.get_value(answer)
            case "4":
                operations.get_value(answer)
            case "5":
                work = False
            case _:
                print("Try again!\n")


main_menu()

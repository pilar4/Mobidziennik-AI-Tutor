import webscraper
import getpass
import ai

if __name__ == "__main__":

    login = getpass.getpass("Enter login: ")
    password = getpass.getpass("Enter password: ")
    tests = webscraper.scrape_data(login, password)


    counter = 1
    for test in tests:
        print(
            "Test numer ", counter,": "
            "klasa", test["klasa"], "liceum",
            test["sprawdzian_or_kartkowka"],
            test["subject"],
            "na temat:", test["topic"],
        )
        print("---------------------------------------------")
        print()
        counter += 1


    selection = input("Na który test chcesz wygenerować notatkę? Podaj numer: ")
    ai.ai_notes(tests[int(selection) - 1])
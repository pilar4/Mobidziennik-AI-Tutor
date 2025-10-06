import webscraper


if __name__ == "__main__":

    tests = webscraper.scrape_data()

    for test in tests:
        print(
            "klasa", test["klasa"], "liceum",
            test["sprawdzian_or_kartkowka"],
            test["subject"],
            "na temat:", test["topic"],
        )
        print("---------------------------------------------")
        print()

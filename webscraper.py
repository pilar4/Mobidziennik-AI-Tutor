from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import getpass



# settings
login = getpass.getpass("Enter login: ")
password = getpass.getpass("Enter password: ")
url = "https://lo5bielsko.mobidziennik.pl/dziennik/sprawdziany"

test = input("Do you wish to continue? Ctrl+C to quit.")


# headless (may or may not be legal, mobidziennik doesn't give permission
# nor prohibits webscraping afaik also robots.txt only has "User-agent: *"
options = Options()
# makes it not open a browser
options.add_argument("--headless")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; Windows 11) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
print("---(Using headless)---")
driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(1)

print("...Logging...")
# find login and password spaces
driver.find_element(By.ID, "login").send_keys(login)
time.sleep(1)
driver.find_element(By.ID, "haslo").send_keys(password)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "zaloguj").click()

time.sleep(2)

# get html of target page
soup = BeautifulSoup(driver.page_source, "html.parser")
soupString = str(soup).lower()

# check if current page is the target one
target_word = "sprawdziany"
if target_word in soupString:
    print("...Logged in...")

else:
    print("Error has occurred")
    driver.close()
    driver.quit()



target_word = 'title='

# take user's class from soupString
klasa = None
for i in range (11000, len(soupString)): # 11,076 is I, so class is 11,077, but it's better to have slight error margin
    if soupString[i:i+len(target_word)] == target_word:
        klasa = soupString[i + len(target_word) + 1]
        break






# check for all user tests
arr_tests = []
# arr_tests should have:
# bool that tells weather it is a "sprawdzian" (1) or "kartkowka" (0)
# string that tells what subject it is
# string that tells what topic it is

word_s = 'sprawdzian'
word_k = 'kartkówka'

for i in range(11076, len(soupString)):
    sprawdzian_kartkowka = None
    subject = None
    topic = None


    if soupString[i:i+len(word_s)] == word_s:

        for new_pointer in range(i-61, i-200, -1):

            if soupString[new_pointer] == '=':
                j=new_pointer+2

                while soupString[j]!='"':
                    j=j+1

                sprawdzian_kartkowka = "Sprawdzian"
                subject = soupString[new_pointer+2:j]
                break


        for new_pointer in range(i, i+500):

            if soupString[new_pointer: new_pointer+5] == 'width':
                j=new_pointer

                while soupString[j]!='<':
                    j=j+1

                topic = soupString[new_pointer+12:j]
                break
    if sprawdzian_kartkowka and subject and topic:
        arr_tests.append({
            "klasa": klasa,
            "sprawdzian_or_kartkowka": sprawdzian_kartkowka,
            "subject": subject,
            "topic": topic,
        })







for test in arr_tests:
    print(
        "klasa:", test["klasa"],
        test["sprawdzian_or_kartkowka"],
        test["subject"],
        "na temat: ", test["topic"],
    )
    print("---------")












# print(soup.prettify())
# with open("page_source.txt", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())

input("Ctrl+C to exit")
driver.close()
driver.quit()

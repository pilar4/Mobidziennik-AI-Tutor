from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# settings
login = input("Enter username: ")
password = input("Enter password: ")
url = "https://lo5bielsko.mobidziennik.pl/dziennik/sprawdziany"

# headless (may or may not be legal, mobidziennik doesn't give permission
# nor prohibits webscraping afaik also robots.txt has only "User-agent: *"
options = Options()
options.add_argument("--headless")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; Windows 11) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(1)

# find login and password spaces
driver.find_element(By.ID, "login").send_keys(login)
time.sleep(1)
driver.find_element(By.ID, "haslo").send_keys(password)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "zaloguj").click()

time.sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.prettify())

input("Ctrl+C to exit")
driver.close()
driver.quit()

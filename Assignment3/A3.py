from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# Set Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize the WebDriver with incognito mode
driver = webdriver.Chrome(options=chrome_options)

# Open a search engine (e.g., Google)
driver.get("https://www.google.com/")

# Search for a Python tutorial
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python tutorial")
search_box.submit()

# Wait for the search results page to load
driver.implicitly_wait(5)

# Click on a search result related to Python tutorials
first_result = driver.find_element(By.CSS_SELECTOR, ".g a")
first_result.click()

# Wait for the website to load
driver.implicitly_wait(10)

# Wait for the video to play for a 15 seconds
time.sleep(15)

# Close the browser
driver.quit()
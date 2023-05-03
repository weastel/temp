from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--connect-timeout=30')

driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get('https://www.google.com')

# Find an element on the page and interact with it
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')
search_box.submit()

# Wait for the search results to load and print the page title
driver.implicitly_wait(10)
print(driver.title)

# Close the browser window
driver.quit()

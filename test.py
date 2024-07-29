from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the first URL
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
print(driver.title)
driver.implicitly_wait(0.5)

# Interact with the first page
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
print(message.text)

# Open a new tab
driver.execute_script("window.open('https://example.com', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

# Interact with the second page
driver.get("https://example.com")
print(driver.title)

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
print(driver.title)

# Close the browser
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.jcpenney.com/rewards")
wait = WebDriverWait(driver, 30)

input("start: ")


form_fields = {
    "firstName":"John",
    "lastName":"Doe",
    "phone":"2223332424",
    "createAccountEmail":"l6p9u@e-record.com",
    "create-password":"Password@123"
}

button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-automation-id='signup_button']")))
ActionChains(driver).move_to_element(button).click().perform()
# window_handles = driver.window_handles
# driver.switch_to.window(window_handles[-1])

for id, value in form_fields.items():
    element = wait.until(EC.presence_of_element_located((By.ID, id)))
    ActionChains(driver).move_to_element(element).click().perform()
    element.send_keys(value)

input("Press Enter to close the browser...")

submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-automation-id='submit_button']")))
ActionChains(driver).move_to_element(button).click().perform()

input("jjjj")
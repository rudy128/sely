from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://online.citi.com/US/ag/cards/application?app=UNSOL&ID=3001&HKOP=fb5ccc3d99ea10c444492b5f31bd711117f7c2e2c7064add4de754d29ca50215&cmp=knc%7Cacquire%7C2006%7CCARDS%7CGoogle%7CBR&ProspectID=PFQ3cCK5ODflG4nPLAl42EzVfv6N3rHR")
wait = WebDriverWait(driver, 30)

def tick_checkbox(driver, element_name):
    driver.execute_script("""
        const checkbox = document.getElementsByName(arguments[0])
        checkbox[1].click()
""", element_name)
    
def submit(driver):
    driver.execute_script("""
        const submit = document.querySelector("button[cdscta='primary']")
        submit.click()
""")

form_field = {
    "firstName": "John",
    "middleName" : "A",
    "lastName" : "Doe",
    "ssnNo":"051233424",
    "dob":"12/06/2000",
    "streetAddress":"7th Street",
    "zipCode" : "75001",
    # "city":"Dallas",
    "mobileNo":"7283212334",
    "email" : "johndoe@example.com",
    "totalAnnualIncome" : "234999",
    "monthlyRent" : "0",
    "securityWord" : "banana",
    "tNcCheckbox" : "yes",
    "submit" : "yes"
}

for name, value in form_field.items():
    if name == "tNcCheckbox":
        tick_checkbox(driver,name)
    elif name == "submit":
        submit(driver)
    else:
        element = wait.until(EC.presence_of_element_located((By.NAME, name)))
        ActionChains(driver).move_to_element(element).click().perform()
        element.send_keys(value)



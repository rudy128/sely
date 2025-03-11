import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def citi(firstname, lastname,ssn, dob,address,zip,phone,email,income ):
    driver = webdriver.Chrome()
    driver.get("https://online.citi.com/US/ag/cards/application?app=UNSOL&ID=3001&HKOP=fb5ccc3d99ea10c444492b5f31bd711117f7c2e2c7064add4de754d29ca50215&cmp=knc%7Cacquire%7C2006%7CCARDS%7CGoogle%7CBR&ProspectID=PFQ3cCK5ODflG4nPLAl42EzVfv6N3rHR")
    wait = WebDriverWait(driver, 30)

    # input("start: ")

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
        "firstName": firstname,
        # "middleName" : "A",
        "lastName" : lastname,
        "ssnNo":ssn,
        "dob":dob,
        "streetAddress":address,
        "zipCode" : zip,
        # "city":"Dallas",
        "mobileNo":phone,
        "email" : email,
        "totalAnnualIncome" : income,
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

    try:
        # Wait for the page to load
        wait = WebDriverWait(driver, 10)
        
        # Step 1: Wait for and click the dropdown
        dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="securityWordHint"]'))
        )
        dropdown.click()
        time.sleep(1)

        # Step 2: Find and click the desired option
        option_text = "Favorite Hobby"
        option = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cds-option2-1"]'))
        )
        option.click()

    except Exception as e:
        print("An error occurred:")
        print(traceback.format_exc())


    def click_agree_and_submit_button(driver):
        """Clicks on the 'Agree and Submit' button with specific attributes."""
        try:
            # 1. Locate the button using its class and text
            button_locator = (By.XPATH, "//button[contains(@class, 'cds-cta') and contains(text(), 'Agree and Submit')]")
            
            # 2. Wait for it to be clickable
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(button_locator)
            )

            # 3. Click the button
            button.click()
            print("Successfully clicked 'Agree and Submit' button.")

        except Exception as e:
            print(f"Failed to click 'Agree and Submit' button: {e}")
    
    click_agree_and_submit_button(driver)

    h1_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//cds-column[@class="cds-column col-lg-12 col-sm-12"]//h1[@id="title" and @class="page-heading"]'))
    )

    # Extract the span element
    span_element = h1_element.find_element(By.XPATH, ".//span")

    # Extract the text content of the h1 element
    if h1_element:
        print(f"{h1_element.text} {span_element.text}")
    else:
        print("Application status element not found.")

    # input("submit: ")
    time.sleep(2)
    driver.quit()
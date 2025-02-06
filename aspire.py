from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def aspire(firstname, lastname, address, city, state, zip, email, phone, dob, ssn, annual_income, coverage_addendum, credit_protection, consent):
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.get("https://www.aspire.com/cccfui/app?loc=cf&flow=apply&brand=acc&refloc=SEO&lang=en")
    wait = WebDriverWait(driver, 10)

    def interact_with_element(name, value, action='send_keys'):
        element = wait.until(EC.presence_of_element_located((By.NAME, name)))
        ActionChains(driver).move_to_element(element).click().perform()
        if action == 'send_keys':
            element.send_keys(value)
        elif action == 'click':
            element.click()

    form_fields = {
        'ion-input-2': firstname,
        'ion-input-9': lastname,
        'ion-input-3': address,
        'ion-input-4': email,
        'ion-input-5': phone,
        'ion-input-6': dob,
        'ion-input-7': ssn,
        'ion-input-8': annual_income,
        'ion-input-11': city,
        'ion-input-12': zip
    }

    for name, value in form_fields.items():
        interact_with_element(name, value)

    buttons = {
        'coverage_addendum': coverage_addendum,
        'credit_protection': credit_protection,
        'consent': consent
    }

    accept_buttons = driver.find_elements(By.CLASS_NAME, 'accept-button')
    decline_buttons = driver.find_elements(By.XPATH, "//ion-button[.//span[text()='DECLINE']]")

    for i, (key, value) in enumerate(buttons.items()):
        button = accept_buttons[i] if value else decline_buttons[i]
        ActionChains(driver).move_to_element(button).click().perform()

    state_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'mat-select')))
    driver.execute_script("arguments[0].click()", state_field)
    print(state_field)

    # ny_element = driver.find_element(By.XPATH, "//div[contains(@class, 'cdk-overlay-backdrop')]//mat-option/span[text()='NY']")
    # actions = ActionChains(driver)
    # actions.move_to_element(ny_element).click().perform()
    # try:
    #     state_field.click()
    # except Exception as e:
    #     print(f"Error: {e}")
    # # finally:
    #     overlay = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.TAG_NAME, "mat-option")))
    #     print("Options")
    #     print(overlay)
    # state_field.click()
    # state_option = driver.find_element(By.XPATH, "//mat-option/span[text()='Texas']")
    # ActionChains.move_to_element(state_option).click().perform()

    # driver.quit()
    
    # Remove this line before Production
    input("Press Enter to close the browser...")


aspire(
    firstname="John",
    lastname="Doe",
    address="123 Main St",
    city="Houston",
    state="TX",
    zip="77510",
    email="johndoe@example.com",
    phone="1234567890",
    dob="01011990",
    ssn="123456789",
    annual_income="50000",
    coverage_addendum=True,
    credit_protection=False,
    consent=True
)
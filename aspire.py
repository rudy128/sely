from otp import supa
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def aspire(firstname, lastname, address, city, state, zip, email, phone, dob, ssn, annual_income, coverage_addendum, credit_protection, consent):
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.get("https://www.aspire.com/cccfui/app?loc=cf&flow=apply&brand=acc&refloc=SEO&lang=en")
    wait = WebDriverWait(driver, 10)

    def select_state(driver, state_name):
        """
        Selects a state from the state dropdown menu using the provided HTML structure.

        Args:
            driver (webdriver): The Selenium WebDriver instance.
            state_name (str): The name of the state to select (e.g., "Texas").
        """

        wait = WebDriverWait(driver, 10)  # Adjust timeout as needed

        try:
            # 1. Click the state dropdown to open it
            state_dropdown = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'mat-form-field[appearance="outline"] mat-select'))
            )
            driver.execute_script("arguments[0].click();", state_dropdown)

            # 2. Wait for the state options to appear
            state_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//mat-option/span[text()='{state_name}']"))
            )

            # 3. Click the desired state option
            driver.execute_script("arguments[0].click();", state_option)

            print(f"Successfully selected state: {state_name}")

        except Exception as e:
            print(f"Error selecting state: {e}")

    def interact_with_element(name, value, action='send_keys'):
        element = wait.until(EC.presence_of_element_located((By.NAME, name)))
        ActionChains(driver).move_to_element(element).click().perform()
        if action == 'send_keys':
            element.send_keys(value)
        elif action == 'click':
            element.click()

    form_fields = {
        'ion-input-1': firstname,
        'ion-input-8': lastname,
        'ion-input-2': address,
        'ion-input-3': email,
        'ion-input-4': phone,
        'ion-input-5': dob,
        'ion-input-6': ssn,
        'ion-input-7': annual_income,
        'ion-input-10': city,
        'ion-input-11': zip
    }

    # input('Press Enter to continue...')
    for name, value in form_fields.items():
        interact_with_element(name, value)
    select_state(driver, state)

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


    
    # select_state(driver, state)
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
    def click_footer_button_js(driver):
        """
        Finds the ion-button inside the ion-footer and clicks it using JavaScript.
        """
        try:
            # Construct javascript
            js_script = """
                const footer = document.querySelector('ion-footer');
                if (footer) {
                    const button = footer.querySelector('ion-button');
                    if (button) {
                        button.click();
                    } else {
                        console.error("ion-button not found inside ion-footer");
                    }
                } else {
                    console.error("ion-footer not found");
                }
            """
            # Executes the javascript from Selenium
            driver.execute_script(js_script)
            print("Submit button clicked using JavaScript.")

        except Exception as e:
            print(f"Error clicking submit button: {e}")

    click_footer_button_js(driver)
    time.sleep(5)
    click_footer_button_js(driver)
    time.sleep(2)
    def enter_verification_code(driver):
        """
        Enters the verification code into the input field.

        Args:
            driver (webdriver): The Selenium WebDriver instance.
            verification_code (str): The verification code to enter.
        """
        try:
            # Locate the input element by its name. Note: getElementByName returns a list.

            # Enter the verification code
            otp =supa(name=firstname)
            script = """
                const vfs = document.querySelector('app-page-verification')
                const vf = vfs.querySelector('input[name="verificationCode"]')
                vf.value = arguments[0]
                vf.dispatchEvent(new Event('input', {bubbles: true}))
                vf.dispatchEvent(new Event('change', {bubbles: true}))
                vf.dispatchEvent(new Event('ionChange', {bubbles: true}))
                vfs.querySelectorAll('ion-row')[2].querySelectorAll('ion-col')[1].querySelector('ion-button').click()
            """
            driver.execute_script(script, otp)

        except Exception as e:
            print(f"Error entering verification code: {e}")

    enter_verification_code(driver)
    time.sleep(5)
    driver.quit()


# aspire(
#     firstname="John",
#     lastname="Doe",
#     address="123 N MAIN ST",
#     city="Houston",
#     state="TX",
#     zip="77002",
#     email="trythisout4200@outlook.com",
#     phone="4325332349",
#     dob="01011990",
#     ssn="324534292",
#     annual_income="50000",
#     coverage_addendum=True,
#     credit_protection=False,
#     consent=True
# )
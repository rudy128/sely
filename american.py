from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import us

def american_express(firstname,lastname,ssn,source,dob,address,zip,phone,email,income):
    options=Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.delta.com/apac/en/skymiles/overview")
    wait = WebDriverWait(driver, 60)

    apply = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.delta.com/applyplat']//span[text()='APPLY NOW']")))
    js_script = """
            var element = arguments[0];
            var event = new MouseEvent('click', {
                view: window,
                bubbles: true,
                cancelable: true
            });
            element.dispatchEvent(event);
        """
    driver.execute_script(js_script, apply)
    driver.switch_to.window(driver.window_handles[-1])

    data = {
        "personalInfo.fullName.firstName": firstname,
        # "personalInfo.fullName.middleName": "S",
        "personalInfo.fullName.lastName": lastname,
        # "personalInfo.cardEmbossedName.firstName": "John", # or "John M" if you include middle initial
        # "personalInfo.cardEmbossedName.lastName": "Doe", # Leave disabled field as is or copy last name
        "personalInfo.dateOfBirth": dob, #MM/DD/YYYY Format
        "personalInfo.email": email,
        "personalInfo.phoneNumber.number": phone,
        "personalInfo.homeAddress.streetAddress": address,
        # "personalInfo.homeAddress.apartmentNumber": "Apt 4B",
        "personalInfo.homeAddress.zipCode": zip,
        # "personalInfo.homeAddress.city": city,
        # "personalInfo.homeAddress.state": us.states.lookup(state).abbr, # or the value if select isn't working.
        "personalInfo.ssn": ssn,
        "personalInfo.totalAnnualIncome": income,
        "personalInfo.nonTaxableIncome": "0",
        "personalInfo.incomeSource": source, # For dropdowns/select
        "personalInfo.pprInfo.pprEnrolled": "NO", # For dropdowns/select, "YES", or "NO"
        "membershipId-radio-option-no": True,
        # "membershipId-radio-option-yes": False

    }
    # ----------------------------------------------------


    # def fill_form(driver, data):
    #     """Fills form elements based on data and element attributes."""

    #     # Locate all input, select and textarea elements within the provided HTML
    #     elements = driver.find_elements(By.CSS_SELECTOR, 'input, select, textarea')

    #     for element in elements:
    #         # Get the element's ID and name attributes
    #         element_id = element.get_attribute("id")
    #         element_name = element.get_attribute("name")
    #         aria_label = element.get_attribute("aria-label")
    #         element_type = element.get_attribute("type")

    #         # Determine the field type based on element type and attributes
    #         field_key = element_id or element_name or aria_label

    #         if not field_key: # Skip to the next element if a field key can't be determined
    #             continue

    #         # Check if there is data to fill
    #         if field_key in data:

    #             # Input
    #             if element.tag_name == 'input':
    #                 if element_type == "text" or element_type == "email" or element_type == "password" or element_type =="number":
    #                     element.send_keys(data[field_key])
    #                 elif element_type == "radio":
    #                     if data[field_key] == True or data[field_key] == "Yes":
    #                         element.click()
    #                     else:
    #                         continue

    #             # Select
    #             elif element.tag_name == 'select':
    #                 # Create a Select object to interact with the dropdown
    #                 select = Select(element)
    #                 select.select_by_value(data[field_key])

    #             # Textarea
    #             elif element.tag_name == 'textarea':
    #                 element.send_keys(data[field_key])

    # def select_element(driver, element_id, element_name):
    #     """Opens a select element and selects it."""
    #     state_dropdown_id = "countrySubdivisionCode_dropdown"
    #     state_option_xpath = f"//div[@id='countrySubdivisionCode_dropdown']//li[@data-label='{element_id}']"
    #     select_dropdown_option(driver, state_dropdown_id, state_option_xpath)
    #     # try:
    #     #     # 1. Locate and click the dropdown element
    #     #     select_element = WebDriverWait(driver, 10).until(
    #     #         EC.element_to_be_clickable((By.ID, element_id))
    #     #     )
    #     #     select_element.click()
    #     # except Exception as e:
    #     #     print(f"select element not clickable {element_id}")

    #     # try:
    #     #     select = WebDriverWait(driver, 10).until(
    #     #         EC.element_to_be_clickable((By.NAME, element_name))
    #     #     )
    #     #     select.click()
    #     # except Exception as e:
    #     #     print(f"select element not clickable {element_name}")


    try:
        # 3. Fill the form using your function
        for field, value in data.items():
            element = wait.until(EC.presence_of_element_located((By.NAME, field)))
            ActionChains(driver).move_to_element(element).click().perform()
            element.send_keys(value)
        #     if field == "personalInfo.homeAddress.streetAddress":
        #         try:
        #             autofill_list = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='testId-street']//ul[@id='autofillList']")))
        #             autofill_items = autofill_list.find_elements(By.TAG_NAME, "li")
        #             print("Autofill Suggestions:")
        #             for item in autofill_items:
        #                 print(item.text)
        #         except Exception as e:
        #             print("Autofill list not found or error accessing it.")
        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='continueButton']")))
        ActionChains(driver).move_to_element(continue_button).click().perform()

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
        ActionChains(driver).move_to_element(submit_button).click().perform()

        # check_application_pending(driver)

        print("Form filled successfully!")

    except Exception as e:
        print(f"An error occurred during form filling: {e}")

    finally:
        # input("Press Enter to close the browser...")
        driver.quit()
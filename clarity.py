from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clarity(first_name, middle_name, last_name, generation, ssn, dob, email, street_address, street_address_2, city, state, zip_code):
    driver = webdriver.Chrome()  # or webdriver.Firefox()
    driver.get("https://consumers.clarityservices.com/idv?type=REMOVE_PRESCREEN_OPT_OUT")
    wait = WebDriverWait(driver, 10)

    # Dictionary mapping field IDs to their corresponding values
    fields = {
        'firstName': first_name,
        'middleInitial': middle_name,
        'lastName': last_name,
        'ssn-input': ssn,
        'dob': dob,
        'email-input': email,
        'street1': street_address,
        'street2': street_address_2,
        'city': city,
        'postal-code': zip_code
    }

    # Fill in text fields
    for field_id, value in fields.items():
        element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        element.send_keys(value)

    # Handle dropdown selections
    generation_field = wait.until(EC.presence_of_element_located((By.ID, 'generation')))
    Select(generation_field).select_by_visible_text(generation)

    state_field = wait.until(EC.presence_of_element_located((By.ID, 'State *-select')))
    Select(state_field).select_by_value(state)

    # Submit the form
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    # Remove this line before Production
    input("Press Enter to close the browser...")
    driver.quit()

clarity(
    first_name="John",
    middle_name="A",
    last_name="Doe",
    generation="JR",
    ssn="123-45-6789",
    dob="01/01/1990",
    email="johndoe@example.com",
    street_address="123 Main St",
    street_address_2="Apt 4B",
    city="Anytown",
    state="CA",
    zip_code="12345"
)
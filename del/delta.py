from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# from faker import Faker

def delta(first_name, last_name, email,username, password, confirm_password, dob, address, city, state, zip_code, phone_number):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--auto-open-devtools-for-tabs")
    #options.add_argument("--headless=new") #Comment out for debugging if needed
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.delta.com/apac/en/skymiles/overview")
    wait = WebDriverWait(driver, 60)

    def handle_cookie_banner(driver):
        """Handles a cookie banner (if present) by clicking 'I UNDERSTAND'."""
        try:
            # Wait for the banner to appear
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "privBanner"))
            )

            # Find the "I UNDERSTAND" button and click it
            understand_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='close-cookie col-1 pr-0 pl-0']//button[text()='I UNDERSTAND']"))
            )
            understand_button.click()

            print("Cookie banner handled successfully.")

        except Exception as e:
            print(f"Cookie banner not found or could not be handled. Error: {e}")
    
    
    def fill_field(field_id, value):
        element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        element.send_keys(value)

    # -- Join SkyMiles link handling --
    join = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/join-skymiles/']//span[text()='Join SkyMiles Now']")))
    print(join)
    # join.click()
    # ActionChains(driver).move_to_element(join).click().perform()

    js_script = """
        var element = arguments[0];
        var event = new MouseEvent('click', {
            view: window,
            bubbles: true,
            cancelable: true
        });
        element.dispatchEvent(event);
    """
    driver.execute_script(js_script, join)

    driver.switch_to.window(driver.window_handles[-1]) # Switch to new tab

    # -- Filling name fields --
    ele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='First Name']")))
    ActionChains(driver).move_to_element(ele).click().perform()
    ele.send_keys(first_name)

    ele1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Last Name']")))
    ActionChains(driver).move_to_element(ele1).click().perform()
    ele1.send_keys(last_name)

    def set_dob(driver, month, day, year):
        """Sets the date of birth using the custom dropdowns."""

        select_month(driver, month)
        select_day(driver, day)
        select_year(driver, year)

    def select_month(driver, month):
        """Selects the month."""
        month_dropdown_id = "month_dropdown"
        month_option_xpath = f"//div[@id='{month_dropdown_id}']//li[@data-label='{month}']"
        select_dropdown_option(driver, month_dropdown_id, month_option_xpath)

    def select_day(driver, day):
        """Selects the day."""
        date_dropdown_id = "date_dropdown"
        date_option_xpath = f"//div[@id='{date_dropdown_id}']//li[@data-label='{day}']"
        select_dropdown_option(driver, date_dropdown_id, date_option_xpath)

    def select_year(driver, year):
        """Selects the year."""
        year_dropdown_id = "year_dropdown"
        year_option_xpath = f"//div[@id='{year_dropdown_id}']//li[@data-label='{year}']"
        select_dropdown_option(driver, year_dropdown_id, year_option_xpath)

    def select_dropdown_option(driver, dropdown_id, option_xpath):
        """Opens a dropdown and selects a specific option."""

        # Open the dropdown
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, dropdown_id))
        )
        dropdown_element.click()
        time.sleep(0.5)  # Short wait for the list to appear

        # Select the option
        option_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option_element.click()
        time.sleep(0.5)  # Short wait after selection

    def select_gender(driver, gender):
        """Selects a gender option from the dropdown."""

        # 1. Open the dropdown
        dropdown_id = "gender_dropdown"
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, dropdown_id))
        )
        dropdown_element.click()
        time.sleep(0.5)  # Short wait for the list to appear

        # 2. Select the gender option
        gender_option_xpath = f"//div[@id='{dropdown_id}']//li[@data-label='{gender}']"  # Updated xpath for gender
        option_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gender_option_xpath))
        )
        option_element.click()
        time.sleep(0.5)  # Short wait after selection
    time.sleep(1)
    handle_cookie_banner(driver)
    time.sleep(3)
    # input("DOB: ")
    # ActionChains(driver).move_to_element(())
    set_dob(driver, "Nov", "10", "1999")
    select_gender(driver, "Female (F)")

    def click_next_button(driver, next_button_xpath):
        """Clicks the Next button."""
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, next_button_xpath))
        )
        next_button.click()

    click_next_button(driver,next_button_xpath = "//button[@id='basic-info-next']")

    ele2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Address Line 1']")))
    ActionChains(driver).move_to_element(ele2).click().perform()
    ele2.send_keys(address)
    
    ele3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='City']")))
    ActionChains(driver).move_to_element(ele3).click().perform()
    ele3.send_keys(city)
    
    ele4 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Postal Code']")))
    ActionChains(driver).move_to_element(ele4).click().perform()
    ele4.send_keys(zip_code)
    
    ele5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Area Code + Phone #']")))
    ActionChains(driver).move_to_element(ele5).click().perform()
    ele5.send_keys(phone_number)
    
    ele6 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Email Address']")))
    ActionChains(driver).move_to_element(ele6).click().perform()
    ele6.send_keys(email)
    
    ele7 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Confirm Email Address']")))
    ActionChains(driver).move_to_element(ele7).click().perform()
    ele7.send_keys(email)

    def select_state(driver, state_name):
        """Selects the state using Selenium functions only."""

        try:
            # 1. Open the dropdown by clicking the 'selected' area
            dropdown_id = "countrySubdivisionCode_dropdown"
            dropdown_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, dropdown_id))
            )
            selected_div = dropdown_element.find_element(By.CLASS_NAME, "idp-dropdown__selected")
            selected_div.click()

            # 2. Find the state option and click it
            state_option_xpath = f"//div[@id='{dropdown_id}']//li[@data-label='{state_name}']"
            state_option_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, state_option_xpath))
            )
            state_option_element.click()

            print(f"Successfully selected state: {state_name}")

        except Exception as e:
            print(f"Error selecting state: {e}")

    select_state(driver, state)
    click_next_button(driver, next_button_xpath = "//button[@id='contact-info-next']")
    # fill_field("email", email)
    # fill_field("password", password)
    # fill_field("confirmPassword", confirm_password)
    # fill_field("address1", address)
    # fill_field("city", city)
    # fill_field("zipCode", zip_code)

    ele8 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Enter a Username']")))
    ActionChains(driver).move_to_element(ele8).click().perform()
    ele8.send_keys(username)

    ele9 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Enter  a Password']")))
    ActionChains(driver).move_to_element(ele9).click().perform()
    ele9.send_keys(password)

    ele10 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.idp-input[aria-label='Confirm Password']")))
    ActionChains(driver).move_to_element(ele10).click().perform()
    ele10.send_keys(confirm_password)

    click_next_button(driver, next_button_xpath = "//button[@id='login-info-submit']")

    input("Press Enter to close the browser...")
    driver.quit()

# fake = Faker()
# user = fake.user_name() + '1489'


# delta(
#     first_name="Ava",
#     last_name="Brayn",
#     email="pytcli21@gmail.com",
#     username=user,
#     password="Pikachu32",
#     confirm_password="Pikachu32",
#     dob="01/01/1990",
#     address="789 White Pine Cir",
#     city="Lake In The Hills",
#     state="Illinois",
#     zip_code="60156",
#     phone_number="4634567650"
# )

# 789 White Pine Cir, Lake In The Hills,  
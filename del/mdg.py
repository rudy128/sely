import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_div_page_element(driver):
    try:
        # Switch to the iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "blazor-iframe"))
        )
        driver.switch_to.frame(iframe)

        # Wait for the div with class "page" to be present
        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form[@class='editForm']"))
        )

        button = WebDriverWait(driver,10).until(form.find_element(By.XPATH,'//button[@type="submit"]'))
        # Print the WebElement of the div
        print("Found div element:", form)
        return form

    except Exception as e:
        print(f"Error finding div element: {e}")
        return None

    finally:
        # Switch back to the main content
        driver.switch_to.default_content()


# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://secure.mdg.com/ApplyNow.aspx")

# Get the div element
div_element = get_div_page_element(driver)

driver.quit()

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.chase.com/personal/mortgage/campaign/pspurchase?SourceCode=ES434N&jp_cmp=hl/Mortgage+-+General+Terms+-+Low+Funnel_Non+Brand_Exact_MTG_SEM_US_NA_Standard_NA+_AI+Ad+Copy+Test+Q1+2025/sea/p81356891917/Preapproved&gclsrc=aw.ds&gad_source=1&gbraid=0AAAAADseac9moG3J6a8yfUxPT6ZNJzuc4&gclid=CjwKCAiAzvC9BhADEiwAEhtlNy8edsLMk1d4KSHfKw1wZ-yZCSFKRhNu-9JfPV0poWdiJG5Ik5oT9hoCqC4QAvD_BwE")
wait = WebDriverWait(driver, 30)

form_fields = {
    "applicant-firstName": "Alexander",
    "applicant-middleName": "",
    "applicant-lastName": "Castillo",
    "mds-datepicker" : "07/12/2002",
    "applicant-taxIdentifier": "061234036",
    "applicant.address.0-addressLine1": "790 Warburton Ave 2c",
    "applicant.address.0-addressCityName": "Yonkers",
    "applicant.address.0-addressStateCode": "NY",
    "applicant.address.0-addressPostalCode": "10701",
    "applicant-email":"pytcli21@outlook.com",
    "applicant-primaryContactPhoneNumber-0": "4634567650",
}

def set_mds_text_input_secure_value(driver, element_id, value):
    driver.execute_script("""
        const element = document.getElementById(arguments[0]);
        element.shadowRoot.querySelector('input').value = arguments[1];
        element.shadowRoot.querySelector('input').dispatchEvent(new Event('input', { bubbles: true }));
        element.shadowRoot.querySelector('input').dispatchEvent(new Event('change', { bubbles: true }));
    """, element_id, value)

def select_mds_select_option(driver, select_id, option_value):
    driver.execute_script("""
        const select = document.getElementById(arguments[0]);
        const option = Array.from(select.querySelectorAll('mds-select-option'))
                          .find(opt => opt.getAttribute('value') === arguments[1]);
        if (option) {
            option.click();
            select.value = arguments[1];
            select.dispatchEvent(new Event('change', { 'bubbles': true }));
        }
    """, select_id, option_value)

def set_mds_datepicker_date(driver, date_string):
    driver.execute_script("""
        const datepicker = document.querySelector('mds-datepicker');
        const input = datepicker.shadowRoot.querySelector('mds-text-input')
        datepicker.value = arguments[0];
        datepicker.dispatchEvent(new Event('dateChange'));
        input.dispatchEvent(new Event('input', {bubbles: true}))
        input.dispatchEvent(new Event('change', {bubbles: true}))
    """, date_string)

def first_step(driver):
    script = """
    const radioGroup = document.querySelector("mds-radio-group")
    const shadowField = radioGroup.shadowRoot.querySelector("mds-fieldset")
    const noRadio = shadowField.querySelector("input[value='false']")
    noRadio.click()
    const submit = document.querySelectorAll("mds-button")[1]
    submit.click()
    """
    driver.execute_script(script)

def set_mds_text_input_value(driver, element_id, value):
    driver.execute_script("""
        const element = document.getElementById(arguments[0]);
        element.shadowRoot.querySelector('input').value = arguments[1];
        element.shadowRoot.querySelector('input').dispatchEvent(new Event('input', { bubbles: true }));
        element.shadowRoot.querySelector('input').dispatchEvent(new Event('change', { bubbles: true }));
    """, element_id, value)

def submitButton(driver,element_id):
    driver.execute_script("""
        const next = document.querySelectorAll("mds-button")
        next[2].click()
""", element_id)

try:
    apply = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://secure.chase.com/web/oao/application/retail#/origination;cfgCode=502002;sourceCode=ES434N;SourceCode=ES434N/index/index']")))
    ActionChains(driver).move_to_element(apply).click().perform()

    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'mds-radio-group')))
    first_step(driver)

    for element, value in form_fields.items():
        if element == 'mds-datepicker':
            # set_mds_datepicker_date(driver, value)
            driver.find_element(By.TAG_NAME, element).click()
            pyautogui.typewrite(value)
            pyautogui.press('enter')
        elif element == 'applicant-taxIdentifier':
            set_mds_text_input_secure_value(driver, element, value)
        elif element == 'applicant-primaryContactPhoneNumber-0':
            set_mds_text_input_value(driver, element, value)
        elif element == 'applicant.address.0-addressStateCode':
            select_mds_select_option(driver, element, value)
        else:
            element = wait.until(EC.presence_of_element_located((By.ID, element)))
            ActionChains(driver).move_to_element(element).click().perform()
            element.send_keys(value)
        
    # footer = wait.until(EC.shadow_root.find_element(By.TAG_NAME, 'mds-sticky-footer'))
    try:
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//mds-button[@text="Next"]')))
        # dialog_text = wait.until(dialog.shadow_root.find_element(By.CLASS_NAME, 'mds-dialog__heading'))
        # print(dialog_text.text)
        ActionChains(driver).move_to_element(next_button).click().perform()

        script = """
        const dialog = document.querySelector('mds-dialog-modal')
        const footer = dialog.shadowRoot.querySelector('mds-sticky-footer')
        const next = footer.shadowRoot.querySelectorAll('mds-button')[1]
        next.click()
        """
        driver.execute_script(script)


        
    except Exception as e:
        print("Can't ",e)

except Exception as e:
    print(e)





# no_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//mds-radio-group[@id='RadioGroup-skipAppCap.loginRedirect']//input[@value='false']")))
# print(no_radio)
input("Close browser: ")
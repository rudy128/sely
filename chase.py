import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

def chase(firstname,lastname,mother_maiden_name,ssn,dob,address,city,state,zip,email,phone,residence,source,income):
    driver = webdriver.Chrome()
    driver.get("https://secure04ea.chase.com/web/oao/application/card?sourceCode=H6KS&action=guest&flowVersion=REACT&AOC=286&RPC=0508&cfgCode=FULLAPPCONCC&channel=C30#/origination/cardDetails/index/initiateConFullApp")
    wait = WebDriverWait(driver, 30)

    # input("start: ")

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

    def set_mds_text_input_secure_value(driver, element_id, value):
        driver.execute_script("""
            const element = document.getElementById(arguments[0]);
            element.shadowRoot.querySelector('input').value = arguments[1];
            element.shadowRoot.querySelector('input').dispatchEvent(new Event('input', { bubbles: true }));
            element.shadowRoot.querySelector('input').dispatchEvent(new Event('change', { bubbles: true }));
        """, element_id, value)

    def set_mds_text_input_value(driver, element_id, value):
        driver.execute_script("""
            const element = document.getElementById(arguments[0]);
            element.shadowRoot.querySelector('input').value = arguments[1];
            element.shadowRoot.querySelector('input').dispatchEvent(new Event('input', { bubbles: true }));
            element.shadowRoot.querySelector('input').dispatchEvent(new Event('change', { bubbles: true }));
        """, element_id, value)

    def set_mds_checkbox_and_button(driver, element_id):
        driver.execute_script("""
            const checkbox = document.getElementById(arguments[0]);
            checkbox.click();
        """, element_id)

    def submitButton(driver,element_id):
        driver.execute_script("""
            const footer = document.querySelector('mds-sticky-footer')
            const submit = footer.shadowRoot.querySelector(arguments[0])
            submit.click()
    """, element_id)

    form_fields = {
        'applicant.name.firstName': firstname,
        # 'applicant.name.middleName': 'A',
        'applicant.name.lastName': lastname,
        'applicant.identity.motherMaidenName' : mother_maiden_name,
        'applicant.taxInformation.taxIdentifierTypeName':'SSN',
        'applicant-taxIdentifier': ssn,
        # "applicant.name.suffixName" : "JR",
        '-input': dob,
        'applicant.address.0.addressLine1':address,
        "applicant.address.0.addressCityName": city,
        "applicant.address.0.addressPostalCode" : zip,
        'applicant.address.0-addressStateCode': state,
        "applicant.email.0.emailAddressText": email,
        'applicant-primaryContactPhoneNumber-0': phone,
        "ssaDisclosure-checkbox-0":"Yes",
        'applicant-residenceOwnershipSelect': residence,
        'applicant-primaryIncomeSourceSelect' : source,
        "applicant.financialInformation.incomeDetails.0.totalAnnualIncomeAmount-genericmoneyinput":income,
        'skipAppCap.consumerCertificationsAgreement-checkbox-0': "Yes",
        # "mds-button" : "Yes"
    }
    for name, value in form_fields.items():
        if name == '-input':
            driver.find_element(By.TAG_NAME, 'mds-datepicker').click()
            pyautogui.typewrite(value)
            pyautogui.press('enter')
            # input('continue?')
            # set_mds_datepicker_date(driver, value)
        elif name == 'applicant-suffixName' or name == 'applicant-taxIdType' or name == 'applicant-primaryIncomeSourceSelect' or name == 'applicant.address.0-addressStateCode' or name == 'applicant-residenceOwnershipSelect':
            select_mds_select_option(driver, name, value)
        elif name == 'applicant-taxIdentifier':
            set_mds_text_input_secure_value(driver, name, value)
        elif name == 'applicant-primaryContactPhoneNumber-0' or name == 'applicant.financialInformation.incomeDetails.0.totalAnnualIncomeAmount-genericmoneyinput':
            set_mds_text_input_value(driver,name,value)
        elif name == 'skipAppCap.consumerCertificationsAgreement-checkbox-0' or name == "ssaDisclosure-checkbox-0":
            set_mds_checkbox_and_button(driver, name)
        elif name == 'mds-button':
            submitButton(driver,name)
        else:
            element = wait.until(EC.presence_of_element_located((By.NAME, name)))
            ActionChains(driver).move_to_element(element).click().perform()
            element.send_keys(value)
    driver.execute_script("""
        const submit = document.getElementById('primary-nav-button').click()
""")
    time.sleep(5)
    try:
        heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'mds-hero-header')))
        if heading:
            print(heading.get_attribute("heading"))
    except Exception as e:
        print(e)
    driver.quit()
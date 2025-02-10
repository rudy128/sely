from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://secure04ea.chase.com/web/oao/application/card?sourceCode=H6KS&action=guest&flowVersion=REACT&AOC=286&RPC=0508&cfgCode=FULLAPPCONCC&channel=C30#/origination/cardDetails/index/initiateConFullApp")
wait = WebDriverWait(driver, 30)

def set_mds_datepicker_date(driver, date_string):
    driver.execute_script("""
        const datepicker = document.querySelector('mds-datepicker');
        const input = datepicker.shadowRoot.querySelector('mds-text-input')
        datepicker.value = arguments[0];
        datepicker.dispatchEvent(new Event('dateChange'));
        input.dispatchEvent(new Event('input', {bubbles: true}))
        input.dispatchEvent(new Event('change', {bubbles: true}))
    """, date_string)

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
    'applicant.name.firstName': 'John',
    'applicant.name.middleName': 'A',
    'applicant.name.lastName': 'Doe',
    'applicant.identity.motherMaidenName' : 'Doe',
    'applicant-taxIdType':'SSN',
    'applicant-taxIdentifier': '051233424',
    "applicant-suffixName" : "JR",
    '-input': '10/01/2001',
    'applicant.address.0.addressLine1':'7th Street',
    "applicant.address.0.addressCityName": "Houston",
    "applicant.address.0.addressPostalCode" : '77510',
    'applicant.address.0-addressStateCode': 'TX',
    "applicant.email.0.emailAddressText": "johndoe@example.com",
    'applicant-primaryContactPhoneNumber-0': '4634567653',
    "ssaDisclosure-checkbox-0":"Yes",
    'applicant-residenceOwnershipSelect': 'RENT',
    'applicant-primaryIncomeSourceSelect' : "EMPLOYED",
    "applicant.financialInformation.incomeDetails.0.totalAnnualIncomeAmount-genericmoneyinput":"50000",
    'skipAppCap.consumerCertificationsAgreement-checkbox-0': "Yes",
    # "mds-button" : "Yes"
}
for name, value in form_fields.items():
    if name == '-input':
        set_mds_datepicker_date(driver, value)
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


input("Press Enter to close the browser...")
driver.quit()
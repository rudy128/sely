import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchShadowRootException

def salliemae(first_name,last_name,email_address,phone_number,birth_month,birth_day,birth_year,ssn_number,street_address,city_name,state_code_,zip_code_,school_state_,school_name_,graduation_month,graduation_year,financial_aid_amount,loan_asking_amount,username_,password_,year_of_degree,time_attending,degree_type,target_stream,school_time_period,school_zip_code,employement_type,annual_income,office_phone=0,program_type="Undergrad"):
    options=Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.salliemae.com/landing/dp_bdc/?DTD_CELL=SEMGOLNRGSL174X761325_br_730164063511_m_BDC&utm_source=google&utm_medium=sem&utm_campaign=acq_google_u_u_u_u_u_b&utm_term=sallie%20mae&bucket=brcore&gad_source=1&gbraid=0AAAAAD19QGI2ItyXuZ5AmJpYyyhHb44St&gclid=CjwKCAiAzvC9BhADEiwAEhtlNwhlUDtmrU6OeLnp-GJPavQ8y9WCI6HcvbDZBIkdBI8ndbQRr10x0xoCaIUQAvD_BwE")
    wait = WebDriverWait(driver, 60)

    # program_list={"Undergrad":"0","Grad":"1","Bar":"2","Residency":"3"}
    undergrad_degree_list = {"Associate":"AA","Bachelor":"BB","Certificate":"CRT","Other":"OTH"}
    # for key in program_list.keys():
    #     if program_type in key:
    #         program_type = program_list[key]
    #         break
    # if program_type == "0":
    #     for i in undergrad_degree_list:
    #         if degree_type in i:
    #             degree_type = undergrad_degree_list[i]
    #             break
    # elif program_type == "1":
        
    # elif program_type == "3":
    #     if "Dental" in degree_type:
    #         degree_type = '0'
    #     else:
    #         degree_type = '1'
    for i in undergrad_degree_list.keys():
        if degree_type in i:
            degree_type = undergrad_degree_list[i]
            break
    
    # try:
        # 1. Locate the "Apply Now" button using explicit wait
    apply_now_button = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Apply now"))
    )

    # 2. Click the button
    apply_now_button.click()

    print("Successfully clicked the 'Apply Now' button.")

    time.sleep(1)
    student = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[@title="Student"]'))
    )
    student.click()

    time.sleep(1)
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Continue"]'))
    )
    continue_button.click()

    time.sleep(1)
    firstname = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="firstName"]'))
    )
    ActionChains(driver).move_to_element(firstname).click().perform()
    firstname.send_keys(first_name)
    
    time.sleep(1)
    lastname = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="lastName"]'))
    )
    ActionChains(driver).move_to_element(lastname).click().perform()
    lastname.send_keys(last_name)
    time.sleep(1)
    email = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]'))
    )
    ActionChains(driver).move_to_element(email).click().perform()
    email.send_keys(email_address)
    time.sleep(1)
    
    phone = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="phoneNumber"]'))
    )
    ActionChains(driver).move_to_element(phone).click().perform()
    phone.send_keys(phone_number)
    time.sleep(1)

    ActionChains(driver).move_to_element(email).click().perform()

    citizen = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="Citizen"]'))
    )
    ActionChains(driver).move_to_element(citizen).click().perform()
    time.sleep(1)

    month = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="months"]'))
    )
    ActionChains(driver).move_to_element(month).click().perform()
    month.send_keys(birth_month)
    time.sleep(1)

    date = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="dates"]'))
    )
    ActionChains(driver).move_to_element(date).click().perform()
    date.send_keys(birth_day)
    time.sleep(1)

    year = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="years"]'))
    )
    ActionChains(driver).move_to_element(year).click().perform()
    year.send_keys(birth_year)
    time.sleep(1)

    ssn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="sSNNumber"]'))
    )
    ActionChains(driver).move_to_element(ssn).click().perform()
    ssn.send_keys(ssn_number)
    time.sleep(1)

    verifyssn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="sSNVerifyNumber"]'))
    )
    ActionChains(driver).move_to_element(verifyssn).click().perform()
    verifyssn.send_keys(ssn_number)
    time.sleep(1)

    ssn.click()

    address = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="address1"]'))
    )
    ActionChains(driver).move_to_element(address).click().perform()
    address.send_keys(street_address)
    time.sleep(1)

    apt = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="address2"]')))
    ActionChains(driver).move_to_element(apt).click().perform()

    city = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="city"]'))
    )
    ActionChains(driver).move_to_element(city).click().perform()
    city.send_keys(city_name)
    time.sleep(1)

    state_code = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="state"]'))
    )
    ActionChains(driver).move_to_element(state_code).click().perform()
    state_code.send_keys(state_code_)
    time.sleep(1)

    zip_code = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="zip"]'))
    )
    ActionChains(driver).move_to_element(zip_code).click().perform()
    zip_code.send_keys(zip_code_)
    time.sleep(1)

    apt.click()

    # Find the element (button) using the class name or other selector
    chat_button = driver.find_element(By.CLASS_NAME, "embeddedServiceHelpButton")

    # Use JavaScript to hide the element
    driver.execute_script("arguments[0].style.display = 'none';", chat_button)
    time.sleep(1)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Continue"]'))
    )
    # print(continue_button)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(1)
    ActionChains(driver).move_to_element(continue_button).click().perform()
    # continue_button.click()
    program = wait.until(EC.element_to_be_clickable((By.XPATH, f'//input[@id="radio-0-73"]')))
    ActionChains(driver).move_to_element(program).click().perform()
    time.sleep(1)

    degree = wait.until(EC.element_to_be_clickable((By.XPATH, f'//input[@value="{degree_type}"]')))
    ActionChains(driver).move_to_element(degree).click().perform()
    time.sleep(1)

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

    

    school_state = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="input-state"]')))
    # ActionChains(driver).move_to_element(school_state).click().perform()
    school_state.click()
    school_state.send_keys(school_state_)
    time.sleep(1)
    option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//ul[@class="search-results-container custom-scrollbar"]/li[text()="{school_state_}"]')))
    option.click()

    school_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="input-school"]')))
    # ActionChains(driver).move_to_element(school_name).click().perform()
    school_name.click()
    pyautogui.typewrite(school_name_[:-1])
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.press(school_name_[-1])

    # school_name.send_keys('UNIVERSITY OF HOUSTON')
    time.sleep(1)
    university_options = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="search-results-container custom-scrollbar"]/ul/li')))
    # print(university_options)
    option_texts = [option.text for option in university_options]
    print(school_name_+school_zip_code)
    for i in option_texts:
        if school_zip_code in i:
            print("Found it: ",i)
            school_name_=i
    university_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//li[text()="{school_name_}"]')))
    university_option.click()

    time.sleep(1)
    select_engineering_with_pyautogui(driver, target_stream)
    # click_major_combobox(driver)
    # pyautogui.press('down')
    # pyautogui.press('down')
    
    school_year = wait.until(EC.element_to_be_clickable((By.XPATH, f'//input[@value="{year_of_degree}"]')))
    ActionChains(driver).move_to_element(school_year).click().perform()
    # school_year.click()
    # school_subject = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@name='major']")))
    # # ActionChains(driver).move_to_element(school_subject).click().perform()
    # school_subject.click()
    school_timeperiod = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{time_attending}']")))
    ActionChains(driver).move_to_element(school_timeperiod).click().perform()
    click_continue_button(driver)
    
    graduate_month = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="expect-to-graduate-month"]')))
    try:
        start_month = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="loan-period-start-month"]')))
        ActionChains(driver).move_to_element(start_month).click().perform()
        start_month.send_keys("08")
        start_year = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="loan-period-start-year"]')))
        ActionChains(driver).move_to_element(start_year).click().perform()
        start_year.send_keys("2025")
        end_month = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="loan-period-end-month"]')))
        ActionChains(driver).move_to_element(end_month).click().perform()
        end_month.send_keys("08")
        end_year = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="loan-period-end-year"]')))
        ActionChains(driver).move_to_element(end_year).click().perform()
        end_year.send_keys("2026")
    except Exception:
        select_year_with_pyautogui(driver, school_time_period)
        
    # time.sleep(5)
    ActionChains(driver).move_to_element(graduate_month).click().perform()
    graduate_month.send_keys(graduation_month)
    time.sleep(1)
    
    graduate_year = wait.until(EC.element_to_be_clickable((By.XPATH, '//lightning-input[@data-id="expect-to-graduate-year"]')))
    ActionChains(driver).move_to_element(graduate_year).click().perform()
    graduate_year.send_keys(graduation_year)
    time.sleep(1)

    graduate_month.click()
    time.sleep(1)
    try:
        cost_of_attendance = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="attendance-number"]')))
    except Exception as e:
        # cost_of_attendance = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-165"]')))
        print(e)
    # ActionChains(driver).move_to_element(cost_of_attendance).click().perform()
    # send keys if there are any
    # time.sleep(1)
    try:
        financial_aid = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="financial-aid-number"]')))
        ActionChains(driver).move_to_element(financial_aid).click().perform()
        financial_aid.send_keys(financial_aid_amount)
    except Exception as e:
        print(e)        
    time.sleep(1)
    ActionChains(driver).move_to_element(cost_of_attendance).click().perform()

    try:
        calculated_need = wait.until(EC.presence_of_element_located((By.XPATH, '//c-slm-apply-calculated-financial-need/div[2]/div/div/table/tbody/tr[3]/td[2]/lightning-formatted-number'))).text
        if calculated_need<loan_asking_amount:
            calculated_need = loan_asking_amount
        print(loan_asking_amount)
    except Exception as e:
        print(e)

    try:
        loan_amount = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="loanRequestAmount"]')))
        ActionChains(driver).move_to_element(loan_amount).click().perform()
        loan_amount.send_keys(loan_asking_amount)
    except Exception as e:
        print(e)
    time.sleep(1)
    ActionChains(driver).move_to_element(cost_of_attendance).click().perform()

    click_continue_button(driver)

    # cosogner_parent = wait.until(parent.find_element(By.TAG_NAME, "c-slm-apply-add-cosigner"))
    # a = wait.until(cosogner_parent.shadow_root.find_element(By.TAG_NAME, "a[data-id='apply-with-cosigner']"))
    # a.click()
    time.sleep(15)
    print("Waited 15 seconds")

    click_cosigner(driver)
    time.sleep(1)
    click_continue_button(driver)
    print("Going for employement status")

    time.sleep(15)
    
    # employment_status = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='radio-0-218]")))
    # ActionChains(driver).move_to_element(employment_status).click().perform()
    script = f"""document.querySelector("c-slm-apply-parent-container-guest").shadowRoot.querySelector("c-slm-apply-final-details").shadowRoot.querySelector("c-slm-apply-employment-status").shadowRoot.querySelector('c-slm-apply-app-card').querySelector("lightning-radio-group").shadowRoot.querySelector('input[value="{employement_type}"]').click()"""
    driver.execute_script(script)
    time.sleep(5)
    if employement_type == "Employed":    
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.typewrite(annual_income)
        time.sleep(1)
        # annual_income_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='total-annual-income']")))
        # ActionChains(driver).move_to_element(annual_income_input).click().perform()
        # annual_income_input.send_keys(annual_income)
        # time.sleep(1)
        # print(annual_income)

        # work_phone = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='work-phone-number']")))
        # print(work_phone)
        # ActionChains(driver).move_to_element(work_phone).click().perform()
        # work_phone.send_keys(work_phone)
        pyautogui.press("tab")
        pyautogui.typewrite(office_phone)
        time.sleep(1)
        print(f"Completed {employement_type}")
    elif employement_type == "Retired":
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.typewrite(annual_income)
        time.sleep(1)
        print(f"Completed {employement_type}")

        # annual_income_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='total-annual-income']")))
        # ActionChains(driver).move_to_element(annual_income_input).click().perform()
        # annual_income_input.send_keys(annual_income)
        # time.sleep(1)
        # print(annual_income)
    elif employement_type == "Self-Employed":
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.typewrite(annual_income)
        time.sleep(1)
        # annual_income_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='total-annual-income']")))
        # ActionChains(driver).move_to_element(annual_income_input).click().perform()
        # annual_income_input.send_keys(annual_income)
        # time.sleep(1)
        # print(annual_income)
        print(f"Completed {employement_type}")

    elif employement_type == "NotEmployed":
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.typewrite(annual_income)
        time.sleep(1)
        print(f"Completed {employement_type}")

        # annual_income_input = wait.until(EC.element_to_be_clickable((By.XPATH,'//lightning-input[@data-id="total-annual-income"]')))
        # ActionChains(driver).move_to_element(annual_income_input).click().perform()
        # annual_income_input.send_keys(annual_income)
        # time.sleep(1)
        # print(annual_income)
    
        

    # annual_income_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='total-annual-income']")))
    # ActionChains(driver).move_to_element(annual_income_input).click().perform()
    # annual_income_input.send_keys(annual_income)
    # time.sleep(1)
    # print(annual_income)

    # work_phone = wait.until(EC.element_to_be_clickable((By.XPATH,"//lightning-input[@data-id='work-phone-number']")))
    # print(work_phone)
    # ActionChains(driver).move_to_element(work_phone).click().perform()
    # work_phone.send_keys(work_phone)
    print("Going to click continue button now")
    click_continue_button(driver)
    
    time.sleep(20)
    click_continue_button(driver)
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    script = """document.querySelector("c-slm-apply-parent-container-guest").shadowRoot.querySelector("c-slm-apply-disclosure-and-submit").shadowRoot.querySelector("lightning-radio-group").shadowRoot.querySelector('input[value="Yes"]').click()"""
    time.sleep(30)
    driver.execute_script(script)

    script = """document.querySelector("c-slm-apply-parent-container-guest").shadowRoot.querySelector("c-slm-apply-disclosure-and-submit").shadowRoot.querySelector('img[data-id="agree-submit"]').click()"""
    driver.execute_script(script)
    
    esign = wait.until(EC.presence_of_element_located((By.XPATH,'//button[@id="btn_Borrower_Esign"]')))
    esign.click()

    time.sleep(15)
    script = """document.querySelector('button[id="btn_Esign"]').click()"""
    driver.execute_script(script)

    time.sleep(15)
    username = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="userID"]')))
    username.send_keys(username_)
    password = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="password"]')))
    password.send_keys(password_)

    # checkbox = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="checkTermsofUse"]')))
    # checkbox.click()
    time.sleep(1)
    checkbox = """document.querySelector('label.control.control-checkbox').click();"""
    driver.execute_script(checkbox)
    print("Clicked checkbox")
    # time.sleep(1)
    
    final_continue = """document.querySelector('input[id="createAccount"]').click()"""
    driver.execute_script(final_continue)
    print("Clicked Continue button")
    time.sleep(1)

    # finally:
        # Optionally, keep the browser open for a few seconds to observe the result
    driver.implicitly_wait(5) # Close the browser
    # driver.quit()


def click_major_combobox(driver):
    script="""
function clickMajorButton() {
// 1. Start from the root component
const rootComponent = document.querySelector('c-slm-apply-parent-container-guest');
if (!rootComponent) return console.error('Root component not found');

// 2. Traverse through nested components (no class selectors needed)
const path = [
'c-slm-apply-studies-info',
'c-slm-apply-school-search',
'c-slm-apply-eligible-major',
'lightning-combobox',
'lightning-base-combobox'
];

let current = rootComponent.shadowRoot;
for (const selector of path) {
    current = current.querySelector(selector)?.shadowRoot;
    if (!current) return console.error(`Failed at: ${selector}`);
}

// 3. Click the button
const button = current.querySelector('button');
if (button) {
button.click();
console.log('Successfully clicked major combobox!');
} else {
console.error('Final button not found');
}
}


clickMajorButton()
    """
    driver.execute_script(script)


def click_year_combobox(driver):
    script="""
function clickMajorButton() {
// 1. Start from the root component
const rootComponent = document.querySelector('c-slm-apply-parent-container-guest');
if (!rootComponent) return console.error('Root component not found');

// 2. Traverse through nested components (no class selectors needed)
const path = [
// 'c-slm-apply-studies-info',
'c-slm-apply-how-much-you-want-to-borrow',
'c-slm-apply-loan-period-list',
'lightning-combobox',
'lightning-base-combobox'
];

let current = rootComponent.shadowRoot;
for (const selector of path) {
    current = current.querySelector(selector)?.shadowRoot;
    if (!current) return console.error(`Failed at: ${selector}`);
}

// 3. Click the button
const button = current.querySelector('button');
if (button) {
button.click();
console.log('Successfully clicked major combobox!');
} else {
console.error('Final button not found');
}
}


clickMajorButton()
    """
    driver.execute_script(script)


def click_continue_button(driver):
    script="""
    function clickContinueButton() {
    // Start from the body to ensure we cover all elements
    const root = document.body;

    // Recursive function to traverse through all elements and their shadow roots
    function traverse(element) {
        if (element.shadowRoot) {
            const button = element.shadowRoot.querySelector('lightning-button[data-id="continue-button"]');
            if (button) {
                console.log('Continue button found in Shadow Root of:', element.tagName);
                button.click();
                return true;
            }
            // Traverse through children in the Shadow Root
            for (const child of element.shadowRoot.children) {
                if (traverse(child)) return true;
            }
        }

        // Traverse through children
        for (const child of element.children) {
            if (traverse(child)) return true;
        }

        return false;
    }

    // Start traversal
    if (!traverse(root)) {
        console.log('Continue button not found');
    }
}

clickContinueButton();

    """
    driver.execute_script(script)

def click_cosigner(driver):
    script="""
    function clickCosignerButton() {
    // Start from the body to ensure we cover all elements
    const root = document.body;

    // Recursive function to traverse through all elements and their shadow roots
    function traverse(element) {
        if (element.shadowRoot) {
            const button = element.shadowRoot.querySelector('a[data-id="apply-with-cosigner"]');
            // const button = element.shadowRoot.querySelector('C-SLM-APPLY-ADD-COSIGNER');
            if (button) {
                console.log('Continue button found in Shadow Root of:', element.tagName);
                button.click();
                return true;
            }
            // Traverse through children in the Shadow Root
            for (const child of element.shadowRoot.children) {
                if (traverse(child)) return true;
            }
        }

        // Traverse through children
        for (const child of element.children) {
            if (traverse(child)) return true;
        }

        return false;
    }

    // Start traversal
    if (!traverse(root)) {
        console.log('Continue button not found');
    }
}

clickCosignerButton();

    """
    driver.execute_script(script)

def get_dropdown_options(driver):
    return driver.execute_script("""
        const dropdownOptions = document.querySelector('c-slm-apply-parent-container-guest')
        .shadowRoot.querySelector('c-slm-apply-studies-info')
        .shadowRoot.querySelector('c-slm-apply-school-search')
        .shadowRoot.querySelector('c-slm-apply-eligible-major')
        .shadowRoot.querySelector('lightning-combobox')
        .shadowRoot.querySelector('lightning-base-combobox')
        .shadowRoot.querySelectorAll('lightning-base-combobox-item');
        
        let result = [];
        dropdownOptions.forEach((option, index) => {
            const text = option.shadowRoot?.querySelector('.slds-media__body')?.textContent;
            result.push(text)
        });
        return result
    """)


def get_year_options(driver):
    return driver.execute_script("""
        const dropdownOptions = document.querySelector('c-slm-apply-parent-container-guest')
            .shadowRoot.querySelector('c-slm-apply-how-much-you-want-to-borrow')
            .shadowRoot.querySelector('c-slm-apply-loan-period-list')
            .shadowRoot.querySelector('lightning-combobox')
            .shadowRoot.querySelector('lightning-base-combobox')
            .shadowRoot.querySelectorAll('lightning-base-combobox-item');

        let result = [];
        dropdownOptions.forEach((option, index) => {
            const text = option.shadowRoot?.querySelector('.slds-media__body span')?.textContent;
            result.push(text);
        });
        return result
    """)


# Function to click the stream div using pyautogui
def select_engineering_with_pyautogui(driver, target_stream):
    try:
        # 1. Get Selenium to open the dropdown
        click_major_combobox(driver)  # Reuse or adapt your existing function

        # Wait for the dropdown to open (adjust time as needed)
        time.sleep(2)

        # 2. Get dropdown coordinates using Selenium
        dropdown_options = get_dropdown_options(driver)
        
        
        index = 0;
        
        for i in range(len(dropdown_options)):
            print(dropdown_options[i])
            if dropdown_options[i] == target_stream:
                index = i
                pyautogui.press('enter')
                print("FOUND")
                break
            pyautogui.press('down')
        

        # # Scroll with 100 pixel increments
        # for scroll_iteration in range(5):
        #   time.sleep(0.5)
        #   pyautogui.scroll(-100)
        
        # 3.Get location of dropdown option, then click

        # Execute JavaScript to get the button's location
        # button_location = driver.execute_script("""
        #   let dropdownOptions = document.querySelector('c-slm-apply-parent-container-guest')
        #     .shadowRoot.querySelector('c-slm-apply-studies-info')
        #     .shadowRoot.querySelector('c-slm-apply-school-search')
        #     .shadowRoot.querySelector('c-slm-apply-eligible-major')
        #     .shadowRoot.querySelector('lightning-combobox')
        #     .shadowRoot.querySelector('lightning-base-combobox')
        #     .shadowRoot.querySelectorAll('lightning-base-combobox-item')[arguments[0]];

        #     let rect = dropdownOptions.shadowRoot.querySelector('.slds-media__body').getBoundingClientRect()
        #      return {x: rect.x + (rect.width / 2), y: rect.y + (rect.height / 2)};
        #     """, index)

        # x = button_location['x']
        # y = button_location['y']

        # print("Clicking location",x,y)
            
        # # 4. PyAutoGUI click - Robustness through scrolling
        # # action = ActionChains(driver)
        # # action.move_to_element(driver.find_element(By.TAG_NAME, 'body')).perform()
        # # action.move_by_offset(int(x),int(y)).click().perform()
            
        # pyautogui.moveTo(x, y, duration=0.5) # Adjust duration if needed
        # pyautogui.click()
        time.sleep(1)  # Small wait after click
        
    except Exception as e:
        print("Error with pyautogui clicking:", e)


def select_year_with_pyautogui(driver, time_period):
    try:
        # 1. Get Selenium to open the dropdown
        click_year_combobox(driver)  # Reuse or adapt your existing function

        # Wait for the dropdown to open (adjust time as needed)
        time.sleep(2)

        # 2. Get dropdown coordinates using Selenium
        dropdown_options = get_year_options(driver)
        
        index = 0;
        
        for i in range(len(dropdown_options)):
            print(dropdown_options[i])
            if dropdown_options[i] == time_period:
                index = i
                pyautogui.press('enter')
                print("FOUND")
                break
            pyautogui.press('down')
        
        time.sleep(1)  # Small wait after click
        
    except Exception as e:
        print("Error with pyautogui clicking:", e)



# salliemae(
#     first_name="John",
#     last_name="Doe",
#     email_address="johndoe@example.com",
#     phone_number="4325457865",
#     birth_month="01",
#     birth_day="01",
#     birth_year="1990",
#     ssn_number="434325758",
#     street_address="123 N MAIN ST",
#     city_name="Houston",
#     # program_type="Undergrad",
#     degree_type="Certificate",
#     state_code_="TX",
#     zip_code_="77002",
#     school_state_="Texas",
#     school_name_="UNIVERSITY OF HOUSTON - DOWNTOWN CONTINUING EDUCATION, HOUSTON, TX,",
#     school_zip_code="00361298",
#     target_stream="Aviation & Airline Programs",
#     year_of_degree="FifthYearSenior",
#     time_attending="HalfTime",
#     school_time_period="Spring 2025 Only: 01/13/2025 - 05/08/2025",
#     graduation_month="08",
#     graduation_year="2028",
#     financial_aid_amount="0",
#     loan_asking_amount="15000",
#     employement_type="NotEmployed",
#     annual_income="100000",
#     office_phone="4325457865",
#     username_='johnoli21',
#     password_="johnoli2123"
# )
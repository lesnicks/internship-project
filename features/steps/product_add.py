from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CLICK_SETTING = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
EMAIL = (By.ID, "email-2")
PASSWORD = (By.ID, 'field')
CONTINUE = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")
CLICK_ADD_PROJECT = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")
VERIFY_RIGHT_PAGE_OPENS = (By.XPATH, "//div[@class='text-img-block']")

NAME = (By.CSS_SELECTOR, "input.input.book.w-input[name='Your-name']")
COMPANY = (By.CSS_SELECTOR, "input.input.book.w-input[name='Your-company-name']")
ROLE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Role']")
AGE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Age-of-the-company']")
COUNTRY = (By.CSS_SELECTOR, "input.input.book.w-input[name='Country']")
NAME_PROJECT = (By.CSS_SELECTOR, "input.input.book.w-input[name='Name-project']")
PHONE = (By.CSS_SELECTOR, "input.input.book.w-input[name='Phone']")
EMAIL_INPUT = (By.CSS_SELECTOR, "input.input.book.w-input[name='Email-add-project']")

VERIFY_INFO = (By.ID, "wf-form-Add-a-project")

VERIFY_SEND_AN_APPLICATION = (By.CSS_SELECTOR, "#wf-form-Add-a-project > input.purchase-access.w-button")

@given('Open the main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    sleep(5)


@when('Log in to the page')
def log_in(context):

    email_field = context.driver.find_element(*EMAIL)
    email_field.click()
    email_field.send_keys("lesnickolas@gmail.com")
    sleep(6)

    password_field = context.driver.find_element(*PASSWORD)
    password_field.click()
    password_field.send_keys("Nickles*1234")
    sleep(5)

    context.driver.find_element(*CONTINUE).click()
    sleep(6)


@when('Click on settings option')
def Click_on_settings_option(context):
    context.driver.find_element(*CLICK_SETTING).click()
    sleep(5)


@then('Click on Add a project')
def Click_on_Add_project(context):
    context.driver.find_element(*CLICK_ADD_PROJECT).click()
    sleep(5)

@then('Verify the right page opens')
def Verify_page_opens(context):
    context.driver.find_element(*VERIFY_RIGHT_PAGE_OPENS)
    sleep(5)


@then('Add some test information to the input fields')
def input_information(context):

    name = context.driver.find_element(*NAME)
    name.click()
    name.send_keys("John")
    sleep(3)

    company = context.driver.find_element(*COMPANY)
    company.click()
    company.send_keys("Nike")
    sleep(3)

    role = context.driver.find_element(*ROLE)
    role.click()
    role.send_keys("QA")
    sleep(3)

    age = context.driver.find_element(*AGE)
    age.click()
    age.send_keys("20")
    sleep(3)

    country = context.driver.find_element(*COUNTRY)
    country.click()
    country.send_keys("USA")
    sleep(3)

    name_project = context.driver.find_element(*NAME_PROJECT)
    name_project.click()
    name_project.send_keys("TestPass")
    sleep(3)

    phone = context.driver.find_element(*PHONE)
    phone.click()
    phone.send_keys("4153768954")
    sleep(3)

    email_input = context.driver.find_element(*EMAIL_INPUT)
    email_input.click()
    email_input.send_keys("nickles1234@gmail.com")
    sleep(3)

@then('Verify the right information is present in the input fields')
def verify_info(context):
    context.driver.find_element(*VERIFY_INFO)
    sleep(5)

@then('Verify “Send an application” button is available and clickable')
def verify_send_application_available_clickable(context):
    context.driver.find_element(*VERIFY_SEND_AN_APPLICATION)
    sleep(5)



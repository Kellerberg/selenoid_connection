'''import allure
from selene import be, have


@allure.title('Testing search')
def test_search(setup_browser):

    browser = setup_browser

    search = 'dogs'

    with allure.step('Open main page'):
        browser.open('https://www.europeana.eu/en')
    with allure.step('Opening search box'):
        browser.element('[data-qa="show search button"]').should(be.visible).click()
    with allure.step('Input search request'):
        browser.element('[data-qa="search box"]').should(be.visible).type(search).press_enter()
    with allure.step('Checking results'):
        browser.element('[data-qa="search page"]').should(have.text(search))
'''


import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
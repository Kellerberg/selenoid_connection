from selene.support.shared import browser
from selene import be, have


def test_search(driver):
    browser.config.driver = driver
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('cats').press_enter()
    browser.element('[id="search"]').should(have.text('Cat'))

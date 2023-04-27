from selene.support.shared import browser
from selene import be, have


def test_search(setup_browser):
    browser.config.driver = setup_browser
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('cats').press_enter()
    browser.element('[id="search"]').should(have.text('Cat'))

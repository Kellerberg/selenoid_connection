from selene.support.shared import browser
from selene import be, have


def test_search(setup_browser):
    browser.config.driver = setup_browser
    browser.open('https://www.europeana.eu/en')
    browser.element('[data-qa="search box"]').should(be.visible).click().type('cats').press_enter()
    browser.element('[data-qa="search page"]').should(have.text('cats'))

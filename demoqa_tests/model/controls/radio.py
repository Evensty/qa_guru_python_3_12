from selene.support.shared import browser


def select(selector):
    browser.element(selector).click()

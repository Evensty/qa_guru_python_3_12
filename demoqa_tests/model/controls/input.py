from selene.support.shared import browser


def set_value(selector, /, *, value):
    browser.element(selector).type(value)


def select(selector, /, *, value):
    browser.element(selector).type(value).press_enter()




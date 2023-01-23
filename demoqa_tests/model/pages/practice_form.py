from selene.support.shared import browser
from selene import have
from demoqa_tests.model.controls import dropdown, uploader, input, datepicker, radio, checkbox


def set_first_name(value):
    input.set_value('#firstName', value=value)


def set_last_name(value):
    input.set_value('#lastName', value=value)


def set_email(value):
    input.set_value('#userEmail', value=value)


def select_gender(gender):
    radio.select(f'[value={gender}]~[for^=gender-radio]')


def set_mobile_number(value):
    input.set_value('#userNumber[placeholder="Mobile Number"]', value=value)


def set_birthday(month, year, day):
    datepicker.set_date(month=month, year=year, day=day)


def set_subjects(value):
    input.select('#subjectsInput', value=value)


def select_hobbies(value):
    checkbox.select('[for^=hobbies-checkbox]', by_text=value)


def select_picture(file):
    uploader.attach('#uploadPicture', file=file)


def set_current_address(value):
    input.set_value('#currentAddress[placeholder="Current Address"]', value=value)


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def submit():
    browser.element('.form-file').submit()


def check_results(*texts):
    browser.all('.table tr td ~td').should(have.texts(*texts))

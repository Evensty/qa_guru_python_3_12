from selene.support.shared import browser
from demoqa_tests.model.pages import practice_form
import allure
from allure_commons.types import Severity


def test_fill_practice_form():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.story("Проверка формы регистрации")
    with allure.step("Переходим на страницу заполнения формы"):
        browser.open('https://demoqa.com/automation-practice-form')
    with allure.step("Вводим имя"):
        practice_form.set_first_name('Ivan')
    with allure.step("Вводим фамилию"):
        practice_form.set_last_name('Petrov')
    with allure.step("Вводим почту"):
        practice_form.set_email('test_practice_form@mail.ru')
    with allure.step("Указываем пол"):
        practice_form.select_gender('Other')
    with allure.step("Вводим номер телефона"):
        practice_form.set_mobile_number('8999577120')
    with allure.step("Указываем дату рождения"):
        practice_form.set_birthday(5, 1920, 21)
    with allure.step("Указываем предметы"):
        practice_form.set_subjects('Maths')
    with allure.step("Выбираем хобби"):
        practice_form.select_hobbies('Reading')
    with allure.step('Прикладываем картинку'):
        practice_form.select_picture('test_image.png')
    with allure.step("Указываем адрес"):
        practice_form.set_current_address('Starokolpaksky alley')
    with allure.step("Выбираем штат"):
        practice_form.select_state('Uttar Pradesh')
    with allure.step("Выбираем город"):
        practice_form.select_city('Lucknow')
    with allure.step("Подтверждаем регистрацию"):
        practice_form.submit()
    with allure.step("Проверяем форму на корректное заполнение"):
        practice_form.check_results('Ivan Petrov', 'test_practice_form@mail.ru', 'Other', '8999577120',
                                    '21 May,1920', 'Maths', 'Reading', 'test_image.png',
                                    'Starokolpaksky alley', 'Uttar Pradesh Lucknow')

def test_fail():
    with allure.step('этот тест упадет'):
        a = 2
        b = 3
        assert a == b


def test_success():
    with allure.step('этот тест пройдет'):
        d = 9
        f = 3
        assert d/f == 3







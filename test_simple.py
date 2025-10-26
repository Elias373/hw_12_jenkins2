import allure
import os
from selene import browser, be, have, command
from pages.practice_form_page import PracticeFormPage


def test_simple(browser_management):
    page = PracticeFormPage()

    with allure.step("Open practice form"):
        page.open()

    with allure.step("Fill form"):
        page.fill_first_name('Ivan')
        page.fill_last_name('Ivanov')
        page.fill_email('ivanov@example.com')
        page.select_gender()
        page.fill_number('1234567890')
        page.select_date_of_birth()
        page.select_subject('English')
        page.select_hobbies()
        page.import_file()
        page.select_adress('Address1')
        page.select_state('NCR')
        page.select_city('Delhi')

    with allure.step("Submit form"):
        page.submit()

    with allure.step("Verify registration"):
        page.should_have_registered()
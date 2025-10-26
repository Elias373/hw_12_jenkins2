import allure
import os
from selene import browser, be, have, command


class PracticeFormPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').perform(command.js.scroll_into_view)

    @allure.step("Fill first name")
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    @allure.step("Fill last name")
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    @allure.step("Fill email")
    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    @allure.step("Select gender")
    def select_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    @allure.step("Fill number")
    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    @allure.step("Select date of birth")
    def select_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select option[value="1996"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="7"]').click()
        browser.element('.react-datepicker__day--007').click()

    @allure.step("Select subject")
    def select_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.step("Select hobbies")
    def select_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    @allure.step("Import file")
    def import_file(self):
        browser.element('#uploadPicture').set_value(os.path.abspath('test_file.txt'))

    @allure.step("Select address")
    def select_adress(self, value):
        browser.element('#currentAddress').type(value)

    @allure.step("Select state")
    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    @allure.step("Select city")
    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    @allure.step("Submit")
    def submit(self):
        submit_button = browser.element('#submit')
        browser.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button.locate())
        browser.driver.execute_script("arguments[0].click();", submit_button.locate())

    @allure.step("Verify registration")
    def should_have_registered(self):
        browser.element('.modal-content').should(be.visible)
        browser.all('td').should(have.texts([
            'Student Name', 'Ivan Ivanov',
            'Student Email', 'ivanov@example.com',
            'Gender', 'Male',
            'Mobile', '1234567890',
            'Date of Birth', '07 August,1996',
            'Subjects', 'English',
            'Hobbies', 'Sports',
            'Picture', 'test_file.txt',
            'Address', 'Address1',
            'State and City', 'NCR Delhi'
        ]))
import allure

from data.data import User
from pages.practice_form_page import PracticeFormPage


@allure.story("Practice form")
class TestPracticeForm:
    @allure.title("Заполнение формы")
    def test_form(self, driver):
        practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        practice_form_page.open()
        user_info = User()
        practice_form_page.fill_registration_form(user_info)
        practice_form_page.check_result_table(user_info)





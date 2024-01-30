import time

import pytest
from selenium import webdriver

from generator.generator import generated_user_info
from pages.practice_form_page import PracticeFormPage

from pages.base_page import BasePage

class TestPracticeForm:
    def test_form(self, driver):
        practice_form_page = PracticeFormPage(driver,'https://demoqa.com/automation-practice-form')
        practice_form_page.open()
        user_info = next(generated_user_info())
        practice_form_page.fill_registration_form(user_info)
        result = practice_form_page.form_result()
        print(user_info.first_name, user_info.last_name, user_info.email, user_info.mobile)
        print(result[0],result[1], result[3])
        assert [user_info.first_name + " " + user_info.last_name] == [result[0]], 'введенные имя и фамилия в результирующей таблице отображаются неверно'
        assert [user_info.email] == [result[1]], 'введенный e-mail в результирующей таблице отображается неверно'
        assert [user_info.mobile] == [result[3]], 'введенный телефон в результирующей таблице отображается неверно'
        #time.sleep(10)





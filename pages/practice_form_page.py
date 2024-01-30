import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from data.data import User
from pages.base_page import BasePage
from termcolor import colored


class PracticeFormPage(BasePage):
    """Локаторы и методы для заполнения формы регистрации и считывания значений результирующей таблицы."""

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    GENDER = (By.XPATH, "//label[text()='{}']")
    MOBILE = (By.CSS_SELECTOR, "#userNumber")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#dateOfBirthInput")
    MONTH = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    MONTH_SELECTOR = (By.XPATH, "//option[text()='{}']")
    YEAR = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    DAY = (By.XPATH, "//div[text()='{}']")
    SUBJECTS = (By.CSS_SELECTOR, "#subjectsInput")
    SUBJECT = (By.XPATH, "//div[@id='subjectsContainer']//div[text()='{}']")
    HOBBIES = (By.XPATH, "// label[text() = '{}']")
    UPLOAD_PICTURE = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    STATE_INPUT = (By.CSS_SELECTOR, '#react-select-3-input')
    CITY_SELECT = (By.ID, 'city')
    CITY_INPUT = (By.CSS_SELECTOR, '#react-select-4-input')
    SUBMIT_BUTTON = (By.ID, "submit")
    MODAL_WINDOW = (By.XPATH, "//*[@class='table-responsive']//td[2]")
    TEXT_MODAL_WINDOW = (By.XPATH, "// div[text() = 'Thanks for submitting the form']")

    @allure.step("Заполнить поля формы регистрации")
    def fill_registration_form(self, user_info: User):
        self.element_is_visible(self.FIRST_NAME).send_keys(user_info.first_name)
        self.element_is_visible(self.LAST_NAME).send_keys(user_info.last_name)
        self.element_is_visible(self.EMAIL).send_keys(user_info.email)
        self.element_is_clickable(self.change_locator(self.GENDER, user_info.gender)).click()
        self.element_is_visible(self.MOBILE).send_keys(user_info.mobile)
        self.fill_calendar(user_info)
        self.fill_subjects(user_info)
        self.fill_hobbies(user_info)
        self.element_is_visible(self.UPLOAD_PICTURE).send_keys(user_info.path_to_file)
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(user_info.current_address)
        self.fill_state_and_city(user_info)
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step("Заполнить поле датой из выпадающего календарика")
    def fill_calendar(self, user_info: User):
        self.element_is_clickable(self.DATE_OF_BIRTH).click()
        year_select = Select(self.element_is_clickable(self.YEAR))
        year_select.select_by_value(str(user_info.birth_date.year))
        self.element_is_clickable(self.MONTH).click()
        self.element_is_clickable(self.change_locator(self.MONTH_SELECTOR, user_info.birth_date.strftime('%B'))).click()
        self.element_is_clickable(self.change_locator(self.DAY, user_info.birth_date.day)).click()

    @allure.step("Заполнить поле учебными предметами")
    def fill_subjects(self, user_info: User):
        subject = (self.element_is_present(self.SUBJECTS))
        for item in user_info.subject:
            subject.send_keys(item)
            subject.send_keys(Keys.RETURN)
            self.element_is_clickable(self.change_locator(self.SUBJECT, item))
            subject.click()

    @allure.step("Заполнить чекбокс с хобби")
    def fill_hobbies(self, user_info: User):
        for item in user_info.hobbies:
            self.element_is_clickable(self.change_locator(self.HOBBIES, item)).click()

    @allure.step("Заполнить штат и город из раскрывающихся списков")
    def fill_state_and_city(self, user_info: User):
        self.element_is_visible(self.STATE_INPUT).send_keys(user_info.state)
        self.element_is_visible(self.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_clickable(self.CITY_SELECT).click()
        self.element_is_visible(self.CITY_INPUT).send_keys(user_info.city)
        self.element_is_clickable(self.CITY_INPUT).send_keys(Keys.RETURN)

    @allure.step("Считать значения результирующей таблицы после отправки формы")
    def get_result_table_data(self):
        result_list = self.elements_are_visible(self.MODAL_WINDOW)
        result_text = [item.text for item in result_list]
        return result_text

    @allure.step("Проверить полученные значения на соответствие введенным")
    def check_result_table(self, user_info: User):
        result = self.get_result_table_data()
        assert self.element_is_visible(
            self.TEXT_MODAL_WINDOW).text == "Thanks for submitting the form", \
            'Текст заголовка модального окна не соответствует ожидаемому результату'
        print(colored('Заголовок модального окна = "Thanks for submitting the form"', 'blue', None, ['bold']))
        assert user_info.first_name + " " + user_info.last_name == result[0], \
            (f'введенные имя: {user_info.first_name}  и фамилия: {user_info.last_name} '
             f'не соответствуют значению в таблице: {result[0]}')
        assert user_info.email == result[1], \
            f'введенный e-mail: {user_info.email} не соответствует значению в таблице: {result[1]}'
        assert user_info.gender == result[2], \
            f'введенный гендер {user_info.gender} не соответствует значению в таблице: {result[2]}'
        assert user_info.mobile == result[3], \
            f'введенный телефон: {user_info.mobile} не соответствует значению в таблице: {result[3]}'
        input_date = str(user_info.birth_date.strftime('%d %B,%Y'))
        assert input_date == result[4], f"введенная дата: {input_date} не соответствует значению в таблице: {result[4]}"
        assert (', '.join(user_info.subject)) == result[5], (f"введенные предметы: {', '.join(user_info.subject)} "
                                                             f"не соответствуют значению в таблице: {result[5]}")
        assert (', '.join(user_info.hobbies)) == result[6], (f"введенные хобби: {', '.join(user_info.hobbies)} "
                                                             f"не соответствуют значению в таблице: {result[6]}")

        file_name = user_info.path_to_file.split('\\')[-1]
        assert file_name == result[7], f'загруженный файл: {file_name} не соответствует названию в таблице: {result[7]}'
        assert user_info.current_address == result[8], (f"введенный адрес: {user_info.current_address} "
                                                        f"не соответствуют значению в таблице: {result[8]}")
        assert (user_info.state + ' ' + user_info.city) == result[9], (
            f"введенные штат и город: {user_info.state + ' ' + user_info.city} "
            f"не соответствуют значению в таблице: {result[9]}")

        print(colored('\nВсе поля соответствуют введенным значениям :)', 'blue', None, ['bold']))

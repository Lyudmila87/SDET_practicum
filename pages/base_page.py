import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Включает в себя необходимые методы для работы с webdriver"""

    def __init__(self, driver: WebDriver, url: str):
        self._driver = driver
        self.url = url

    @allure.step("Открыть ссылку")
    def open(self):
        self._driver.get(self.url)

    def element_is_visible(self, locator: tuple, timeout=5):
        """Возвращает элемент, если он видим"""

        return wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple, timeout=5):
        """Возвращает список элементов, если они видимы"""

        return wait(self._driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: tuple, timeout=5):
        """Возвращает элемент, если он представлен в DOM"""

        return wait(self._driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator: tuple, timeout=5):
        """Возвращает элемент, если он кликабелен"""

        return wait(self._driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def change_locator(locator_path: tuple, value: str) -> tuple:
        """Принимает кортеж (BY, локатор) для изменения локатора и возвращает обновленный кортеж"""

        new_locator = locator_path[1].format(value)
        return locator_path[0], new_locator

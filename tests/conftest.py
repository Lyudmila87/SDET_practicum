import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@allure.step("Открыть и закрыть браузер")
@pytest.fixture()
def driver():
    options = Options()
    options.page_load_strategy = 'eager'  # позволяет не ждать полной загрузки сайта и сократить время на прогон теста
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()



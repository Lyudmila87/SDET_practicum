# Тестовое задание от SimbirSoft по SDET

На языке Python создан проект UI-автотестов на основе следующих критериев:

- Применяется Selenium Webdriver (браузер Chrome) и  Pytest;
- Для поиска элементов на странице примененяются: css, xpath, id; 
- Используется паттерн проектирования Page Object;
- Реализовано формирование отчетов о пройденных тестах через Allure.
____

Версия Python 3.11.5

Google Chrome: 120.0.6099.217 (Официальная сборка) (64 бит) (cohort: Stable Installs & Version Pins) 

Команда для запуска теста c сохранением отчета: `pytest --alluredir=allure_report -s -v tests\test_practice_form.py`
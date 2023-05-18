from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from typing import List



class SeleniumBase:

    def __init__(self, driver):  # функция для инициализирования нашего браузера ,("self"-функция принимает сама себя) и браузер
        self.driver = driver  # записываем переменную драйвера для передачи в параметры
        self.wait = WebDriverWait(driver, 15, 0.5)  # команда задержки (драйвер, время, задержка)


    def get_selenium_by(self, find_by: str) -> dict:  # функция которая определяет по каким критериям будут находиться элементы (self, find_by: строка),-> dict - переход в повторение
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'tag': By.TAG_NAME,
            'partial': By.PARTIAL_LINK_TEXT }  # здесь мы дали краткие названия методам поиска по различным критериям

        return locating[find_by]  # команда возврата СПИСКА с результатом в зависимости от поиска

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:  # функция для того что бы проверить отображается ли наш элемент СРАЗУ(то что есть в коде) или нет и какие типы данных она принимает и возвращает
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:  # функция для того что бы проверить появляется ли наш элемент(то что отрисовалось на странице) или нет и какие типы данных она принимает и возвращает
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:  # функция для того что бы проверить НЕ появляется ли наш элемент(то что отрисовалось на странице) или нет и какие типы данных она принимает и возвращает
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)),
                               locator_name)

from selenium.webdriver.remote.webelement import WebElement
from typing import List

from selenium_base.base_functions import SeleniumBase


# создаем файл с навигацией главной страницы

class HomepageNav(SeleniumBase):                             # наследуем класс ,что бы класс HomepageNav имел все возможности из класса SeleniumBase

    def __init__(self, driver):                              # вызываем драйвера в парметрах укзываем (что функция принимает саму себя и принимает наш браузер)
        super().__init__(driver)                             # super- метод для обьявления драйвера+вызов(браузера)
        self.driver = driver                                 # в переменную передаем драувер с настройками которые указали в конфтест.пай
        self.nav_links: str = "#mainNavigationFobs>li"       # вызываем функцию которая передает саму себя+создаем переменную в которой будет храниться айди элемента который нам нужен
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'

# создаем функцию где мы получаем nav_links

    def get_nav_links(self) -> List[WebElement]:                   # функция передает саму себя и возвращает список(потому что элементов несколько) WebElement
        return self.are_visible('css', self.nav_links, 'Header Navigation links')  # прописываем команду возврата  указываем по какому принципу она будет возвращать данные с функцией are_visiable из бейс.пай("указали по чему будем искать",локатор self.nav_links, название того что ищем,)

    def get_nav_links_text(self) -> str: # функция для получения тескта
        nav_links = self.get_nav_links() # записываем в переменную nav_links то что получает предидущая функция
        nav_links_text = [link.text for link in nav_links] # создаем цикл для записи в спикок, цикл будет работать по принципу(то что будем записывать "link.text" который будет проходиться по "link" и будет длиться столько сколько существует "nav_links"
        return ",".join(nav_links_text) # возвращает строки(список) которые будут разделяться запятой.(",") и мы их будем присоединять в наш список(метод работы с строковым типом данных .join)

    def find_full_name_field(self) -> WebElement:
        return self.is_visible('css', '#userName', 'Full name field')

    def find_email_field(self) -> WebElement:
        return self.is_visible('css', '#userEmail', 'Email field')

    def find_current_field(self) -> WebElement:
        return self.is_visible('css', '#currentAddress', 'Current Address field')

    def find_permanent_field(self) -> WebElement:
        return self.is_visible('css', '#permanentAddress', 'Permanent Address field')


    def get_find_button(self) -> WebElement:
        return self.is_visible('css', '#submit', 'Knopka')

    def button_use(self):
        button = self.get_find_button()
        return button


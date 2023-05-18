import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from homepage_nav.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup') # обьявляем раннее написанную фикстуру в файле conftest.py с функцией setup
class TestHomePage:

    #def test_nav_links(self):                            # пишем тест1 для того что бы получить фактический результат,полсе получения пишем тест2
        #homepage_nav = HomepageNav(self.driver)          # создаем переменную которая передает все что написано в HomepageNav(логика навигации) и передаем драйвер((self.driver))
        #print(homepage_nav.get_nav_links_text())         # выводим переменную "homepage_nav" в которую записан весь класс "HomepageNav" с функцией "get_nav_links_text()" которая формирует и выводит список значений
        #'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'

    def test_nav_links(self):                             # пишем тест2 для того что бы сравнить фактический результат с ожидаемым
        homepage_nav = HomepageNav(self.driver)           # создаем переменную которая передает все что написано в HomepageNav(логика навигации) и передаем драйвер((self.driver))
        actual_links = homepage_nav.get_nav_links_text()  # создаем переменную которая(как мы выяснили) передает фактический результат
        expected_links = homepage_nav.NAV_LINK_TEXT       # создаем переменную которая передает ожидаемый результат
        assert actual_links == expected_links, 'Validation Nav Links Text'            # сравниваем переменные с помощью комманды "assert"(подтверждение,булевый тип данных)

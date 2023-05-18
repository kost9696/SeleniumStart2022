from selenium import webdriver
from selenium.webdriver.common.by import By
import time



url = "https://www.instagram.com/"  # переменная с путем сайта
driver = webdriver.Chrome(executable_path="../ChromeDriver/chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)

    email_field = driver.find_element(By.NAME, "username")                          # команда для посика поля
    email_field.clear()                                                             # команда для очистки поля
    email_field.send_keys("kostya.testing")                                         # команда для ввода значения
    time.sleep(5)

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("kostya.kostya")
    time.sleep(5)

    enter_button = driver.find_element("_ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm") # переменная кнопки
    enter_button.click()                                                            # команда нажатия кнопки
    time.sleep(5)

    #def test_homepage(self):  пример функции для поиска элемента и ввода значения
        #driver = webdriver.Chrome
        #search_field = driver.find_element(By.ID, '#"globalSearchInputField"')
        #search_field.clear()
        #search_field.send_keys('All Baby')

except Exception as ex:
    print(ex)

finally:
    driver.close() #закрывает вкладку
    driver.quit() # закрывает браузер
    #driver.quite() закрывает браузер,с большим количеством вкладок(полностью)

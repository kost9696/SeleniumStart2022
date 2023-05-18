import pytest                                                                                       # фикстура которая покрывает функции,что бы исползьовать функции во всем проекте
from selenium import webdriver                                                                      # что бы связываться с браузером и передавать команды
from selenium.webdriver.chrome.options import Options as chrome_options                             # записываем опции как chrome_options,что бы передавать настройки браузера


# Здесь мы будем делать все тоже самое что и в файле basicstests.py но отдельными функциями
# Создаем фунцкию с опциями которые нам нужны при запуске браузера
# Создаем функцию где указываем путь к хромдрайверу
# Создаем функцию где запускаем браузер и указываем url для запуска

@pytest.fixture                                                                                     # создаем фикстуру
def get_chrome_options():                                                                           # функция которая получает вебдрайвер
    options = chrome_options()                                                                      # создаем переменную опции
    options.add_argument('chrome')                                                                  # Headless mode - позволяет запсукать тесты без UI,для этого передаем в аргументы название браузера
    options.add_argument('--start-maximized')                                                       # опция запускает в макисмальном разширении
    options.add_argument('--window-size=1280,720')                                                   # уточняем размер окон
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):                                                              # фунцкия которая вызывает вебдрайвер
    options = get_chrome_options
    driver = webdriver.Chrome( options=options)    # создаем переменную driver,после передаем туда значение пути к вебдрайверу и передаем опции котроые прописывали ранее

    return driver


@pytest.fixture(scope='function') # указываем scope='function',это значит то что эта фикстура будет вызываться каждый раз когда мы открываем браузер,если не укзывать она вызовется один раз
def setup(request, get_webdriver):                                                                           # создаем фунцкию дляобьявления url,тоже самое что и driver.get(url=url)
    driver = get_webdriver                                                                          # показываем что будем запускать наш браузер
    url = 'https://demoqa.com/text-box'
    if request.cls is not None:    # если драйвер не был найден
        request.cls.driver = driver           # то в пустоту записываем драйвер
    driver.get(url)                                                                                 # команда которая диктует что открывать нашему браузеру
    yield driver  # yield- команда работает так же как и return нужна для того что бы вернуть(передать в браузер)
    driver.close()
    driver.quit()







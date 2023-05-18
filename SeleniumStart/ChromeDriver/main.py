from selenium import webdriver
import time                                  #библиотека для команды "time.sleep(_)" которая позволит устонавливать задержку между открытием и закрытием
#шпаргалка открытия сайта через селениум

#options

#options = webdriver.ChromeOptions()
#options.add_argument('user-agent=HelloWorld')

url = "https://www.macys.com/"               #переменная с путем сайта
driver = webdriver.Chrome(executable_path="E:\\PycharmProjects\\SeleniumStart\\ChromeDriver\\chromedriver.exe")#,
                          #options=options) #задаем переменную которая открывает наш вебдрайвер + #добавляем опцию

#driver.get() действие которое должен совершить драйвер

try:
    driver.get(url=url)                     #передаем в драйвер наш путь
    time.sleep(5)                           #настраиваем задержку между открытием и закрытием

except Exception as ex:                     #команда которая передает и записывает наши ошибки
    print(ex)

finally:
    driver.close()                          #закрывает вкладку
    driver.quit()                           #закрывает драйвер(браузер)


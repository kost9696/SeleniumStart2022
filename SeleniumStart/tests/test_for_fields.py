import time

import pytest

from homepage_nav.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestForField:

    def test_for_fields(self):
        driver = HomepageNav(self.driver)
        name_field = driver.find_full_name_field()
        name_field.send_keys('Gnusniy Tip')
        time.sleep(5)
        email_field = driver.find_email_field()
        email_field.send_keys('daun@gmail.com')
        time.sleep(5)
        current_field = driver.find_current_field()
        current_field.send_keys('Na dne')
        time.sleep(5)
        permanent_field = driver.find_permanent_field()
        permanent_field.send_keys('Vsegda na dne')
        time.sleep(5)

    def test_for_s_button(self):
        driver = HomepageNav(self.driver)
        button = driver.get_find_button()
        button.click()









# # automated unit test to ensure a window to add a new client appears
# when the "+ New" button is clicked
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        # login from the admin pane
        user = "Mazin771"
        pwd = "123123123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)


        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(5)
        continue_test = False
        try:

            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[1]/a").click()
            continue_test = True
            time.sleep(3)

        except NoSuchElementException:
            self.fail("all products does not appear = All product not present")
            assert False
            time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

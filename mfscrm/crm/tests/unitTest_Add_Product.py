import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "Mazin771"
        pwd = "123123123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")

        time.sleep(3)

        assert "Logged in"
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(5)
        continue_test = False
        try:
            assert "Logged in"
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/a/span").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("View all client does not appear = View All Clients button not present")
            assert False
            time.sleep(3)
        except:
            self.fail("Edit post NOT successful - error occurred: ")
            assert False
            time.sleep(3)
        time.sleep(2)

        if continue_test:
            elem = driver.find_element_by_id("id_product")
            elem.clear()
            elem.send_keys("Test Name")
            elem = driver.find_element_by_id("id_p_description")
            elem.clear()
            elem.send_keys("This is a test note via Selenium testing")
            elem = driver.find_element_by_id("id_charge")
            elem.clear()
            elem.send_keys("123")
            time.sleep(6)
            #click the Update button
            assert "Logged in"
            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
            time.sleep(6)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()

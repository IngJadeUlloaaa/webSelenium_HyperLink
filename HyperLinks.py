import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')
    def test_using_hyperlinks(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/python/default.asp')
        time.sleep(4)
        text_link = driver.find_element(By.LINK_TEXT, 'Python Operators')
        text_link.click()
        time.sleep(2)
    def tearDown(self):
        self.driver.close()
if __name__=='__main__':
    unittest.main()
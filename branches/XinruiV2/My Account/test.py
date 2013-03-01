from selenium import selenium
import unittest, time, re

class test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://www1.moon-ray.com")
        self.selenium.start()
    
    def test_test(self):
        sel = self.selenium
        sel.open("/v2.4/autosauce_pthrough.php?key=ruVerU26")
        sel.click("link=My Account")
        sel.wait_for_page_to_load("30000")
        sel.click("link=(Change Subscription)")
        sel.wait_for_page_to_load("30000")
        sel.click("css=b > a > span")
        sel.click("css=input.btn2")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

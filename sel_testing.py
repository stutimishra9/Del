from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()
browser.get('http://192.168.3.253:8080/login')
user_field=browser.find_element_by_name('uname')
pass_field=browser.find_element_by_name('pw')
user_field.send_keys('abc')
pass_field.send_keys('xyz')
pass_field.send_keys(Keys.RETURN)
try:
    assert 'Log' in browser.title
    print('Test case success')
except AssertionError:
    print('Test Failed')
finally:
    import time
    time.sleep(2)
    browser.close()

import unittest
class MyTests(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        print('In setup..')
    def test_testcase1(self):
        browser=self.browser
#        browser = webdriver.Chrome()
        browser.get('http://192.168.3.253:8080/login')
        user_field=browser.find_element_by_name('uname')
        pass_field=browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test case 1 passed')

    def test_testcase2(self):
        browser=self.browser
 #       browser=webdriver.Chrome()
        browser.get('http://192.168.3.253:8080/login')
        user_field=browser.find_element_by_name('uname')
        pass_field=browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test case 2 passed')

    def test_testcase3(self):
        browser=self.browser
  #      browser=webdriver.Chrome()
        browser.get('http://192.168.3.253:8080/login')
        user_field=browser.find_element_by_name('uname')
        pass_field=browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)
        assert 'log' in browser.title
        print('Test case 3 passed')

    def tearDown(self):
        print('In tearDown..')
        import time
        time.sleep(2)
        self.browser.close()

if __name__=='__main__':
    unittest.main()
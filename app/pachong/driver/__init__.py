import os
from selenium import webdriver


class Driver(webdriver.Chrome):
    def __init__(self, executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super().__init__(executable_path=executable_path, chrome_options=options)


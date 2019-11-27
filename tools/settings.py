import os
from sys import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def get_driver(headless = False):
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		driver_name = "chromedriver"

	else:
		driver_name = 'chromedriver.exe'

	chrome_driver = os.path.join(
			BASE_DIR,
			'assets',
			driver_name
		)

	if headless:
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1920x1080")

		return webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
	
	return webdriver.Chrome(chrome_driver)
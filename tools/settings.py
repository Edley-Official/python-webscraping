from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless = False):

	if headless:
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1920x1080")

		return webdriver.Chrome(options=chrome_options)
	
	return webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def get_driver_from_manager():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def get_driver_from_local():
    return webdriver.Chrome()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse, parse_qs


def get_driver_from_manager():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def get_driver_from_local():
    return webdriver.Chrome()

def get_seller_id(url):
    # 解析URL
    parsed_url = urlparse(url)
    
    # 获取查询参数
    query_params = parse_qs(parsed_url.query)
    
    # 返回seller参数的值，如果存在的话
    return query_params.get('seller', [None])[0]



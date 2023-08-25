from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pprint
from hj import get_product
from save import save_product
from get_products import get_products_urls
options=webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)
urls=get_products_urls(driver)
for url in urls:
    product=get_product(driver,url)
    save_product(product) 
    time.sleep(1)


time.sleep(1)
driver.close()
from selenium.webdriver.common.by import By
def get_products_urls(driver):
    url="https://www.tunisianet.com.tn/596-smartphone-tunisie"
    urls=[]
    driver.get(url)
    titles=driver.find_elements(By.CLASS_NAME,"product-title")
    for title in titles:
        anchor=title.find_element(By.TAG_NAME,"a")
        link=anchor.get_attribute("href")
        urls.append(link)

    return(urls)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
def get_product(driver,url):   
    driver.get(url)

    product = {}

    # get data
    title_element = driver.find_element(By.CLASS_NAME, "h1")
    title = title_element.text
    product["title"] = title

    refference_element = driver.find_element(By.CLASS_NAME, "product-reference")
    reference = refference_element.text
    product["reference"] = reference
    try:
        description_element=driver.find_element(By.ID,"product-description-short-66222")
        description=description_element.text
        product["description"]=description
    except NoSuchElementException:
        description_element=driver.find_element(By.CLASS_NAME,"prodes")
        description=description_element.text
        product["description"]=description

    
    

    prix_element=driver.find_element(By.CLASS_NAME, "product-prices")
    prix=prix_element.text
    product["prix"]=prix
    available_element=driver.find_element(By.ID,"stock_availability")
    available=available_element.text
    product["available"]=available
    all_images=driver.find_elements(By.TAG_NAME,"img")
    """ for image in all_images:
        print(image.get_attribute("src")) """
    image=all_images[1].get_attribute("src")
    im=all_images[3].get_attribute("src")
    product["brand_img"]=im
    product["image"]=image
    return(product)
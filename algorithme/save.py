import json
import os
path = os.getcwd()
pathf = os.path.join(path, "algorithme")
products_folder=os.path.join(pathf,"product")
def save_product(product):
   
    if  not os.path.exists(products_folder):
        os.mkdir(products_folder)
    product_title=product["title"].replace("/","").replace(" ","")
    pathj=os.path.join(products_folder,f"{product_title}.json")
    with open(pathj, "w") as jsonfile:
        content = json.dumps(product)
        jsonfile.write(content)
        print(f"[+]{product['title']} has been added")
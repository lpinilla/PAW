import json
from urllib.request import urlopen, Request



#original: https://www.jumbo.com.ar/api/catalog_system/pub/products/search/?sc=1&_from=0&_to=49
base_url = "https://www.jumbo.com.ar/api/catalog_system/pub/products/search/"
query = ""
    #hay que poner un user-agent para que no lo bloquee la página
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
products = []

# 1000 numero aproximado
for i in range(0,2500,50):
    print("Tanda n°:" + str(i/50))
    ####################
    #  Bajar los Json  #
    ####################
    query = "?sc=1&_from=" + str(i) + "&_to=" + str(i+49)
    print("req:" + base_url + query)
    req = Request(url=base_url + query , headers=headers)
    data = json.loads(urlopen(req).read())
    #####################
    #  Agarrar la data  #
    #####################

    for d in data:
        name = d["productName"]
        brand = d["brand"]
        description = d["description"]
        imageurl = d["items"][0]["images"][0]["imageUrl"]
        price = d["items"][0]["sellers"][0]["commertialOffer"]["Price"]
        newdata = {
        "name": name,
        "brand": brand,
        "description":description,
        "imageurl": imageurl,
        "price": price
        }
        products.append(newdata)

    ########################
    #  Imprimir a archivo  #
    ########################

    with open("output.json", "w+") as write_file:
        json.dump(products, write_file)


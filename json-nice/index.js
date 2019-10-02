let data = require('./jumbo.json')
var util = require('util')

let pid = 1;

let superNames = ["Coto", "Jumbo", "Carrefour", "Disco", "Dia"]
let N = superNames.length

let categories = new Set();

data.forEach((p) => {
    categories.add(p.category.split("/")[1])
})

let catArray = Array.from(categories)

catArray.forEach((c) => {
    console.log(util.format("INSERT INTO categories VALUES (%s)", c))
})
console.log("")
data.forEach((p) => {
    console.log(util.format("INSERT INTO products(name,brand,description, img_url, prod_link, to_cart_link) VALUES ('%s','%s','%s','%s','%s','%s')", p.name, p.brand, p.description.replace("'","\'"), p.image, p.prodPageLink, p.addCartLink))
    console.log(util.format("INSERT INTO categories_products VALUES (%s, %s)", catArray.indexOf(p.category), pid))
    for(let i = 0; i<= N; i++) {
        console.log(util.format("INSERT INTO products_supermarkets VALUES (%s, %s, %s)", pid, i, p.price * Math.random() * (1.10 - 0.9) + 0.9))
    }
    console.log("")
    pid++
})



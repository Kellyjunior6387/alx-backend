const express = require('express');
import { createClient } from 'redis';

const listProducts = [
    {
        "Id": 1,
        "name": "Suitcase 250",
        "rice": 50,
        "stock": 4
    },
    {
        "Id": 2,
        "name": "Suitcase 450",
        "rice": 100,
        "stock": 10
    },
    {
        "Id": 3,
        "name": "Suitcase 650",
        "rice": 350,
        "stock": 2
    },
    {
        "Id": 4,
        "name": "Suitcase 1050",
        "rice": 550,
        "stock": 5
    }
]
const getItemById = (id) => {
    return listProducts.find(item => item.Id === id)
}

const app = express();
const client = createClient()
const port = 1245;

const reserveStockById = async (itemId, stock) => {
    return promisify(client.SET).bind(client)(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
    return promisify(client.GET).bind(client)(`item.${itemId}`);
};


app.get('/list_products', (_, res) => {
    res.json(listProducts)
});

app.get('/list_products/:itemId(\\d+', (req, res) => {
    const id = Number.parseInt(req.params.itemId)
    const item = getItemById(id)

    if (!item) {
        res.json({ "status": "Product not found" })
        return;
    }
    getCurrentReservedStockById(id)
        .then((result) => { Number.parseInt(result) || 0 })
        .then((stock) => {
            item.stock = item.stock - stock
            res.json(item)
        })
});

app.get('/reserve_product/:itemId', (req, res) => {
    const id = Number.parseInt(req.params.itemId)
    const item = getItemById(id)

    if (!item) {
        res.json({ "status": "Product not found" })
        return;
    }
    getCurrentReservedStockById(id)
        .then((number) => {
            if (number => item.stock) {
                res.json({ "status": "Not enough stock available", "itemId": id })
            }
            reserveStockById(itemId, number + 1)
                .then(() => {
                    res.json({ status: 'Reservation confirmed', id });
                });
        })

});
const resetProductsStock = () => {
    return Promise.all(
        listProducts.map(
            item => promisify(client.SET).bind(client)(`item.${item.itemId}`, 0),
        )
    );
};

app.listen(port, () => {
    resetProductsStock()
        .then(() => {
            console.log(`API available on localhost port ${port}`);
        });
});

export default app;

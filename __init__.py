# import json

# import products
# from cart import dao
# from products import Product


# class Cart:
#     def __init__(self, id: int, username: str, contents: list[Product], cost: float):
#         self.id = id
#         self.username = username
#         self.contents = contents
#         self.cost = cost

#     def load(data):
#         return Cart(data['id'], data['username'], data['contents'], data['cost'])


# def get_cart(username: str) -> list:
#     cart_details = dao.get_cart(username)
#     if cart_details is None:
#         return []
    
#     items = []
#     for cart_detail in cart_details:
#         contents = cart_detail['contents']
#         evaluated_contents = eval(contents)  
#         for content in evaluated_contents:
#             items.append(content)
    
#     i2 = []
#     for i in items:
#         temp_product = products.get_product(i)
#         i2.append(temp_product)
#     return i2

    


# def add_to_cart(username: str, product_id: int):
#     dao.add_to_cart(username, product_id)


# def remove_from_cart(username: str, product_id: int):
#     dao.remove_from_cart(username, product_id)

# def delete_cart(username: str):
#     dao.delete_cart(username)

import json
from products import Product, get_product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(
            id=data['id'], 
            username=data['username'], 
            contents=[get_product(prod_id) for prod_id in json.loads(data['contents'])],
            cost=data['cost']
        )


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_list = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail['contents'])
            products_list.extend(get_product(prod_id) for prod_id in contents)
        except (json.JSONDecodeError, KeyError):
            # Handle the error if contents are not valid JSON or the key is missing
            continue

    return products_list


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)


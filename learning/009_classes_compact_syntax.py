# Creating classes in a compact way with not
# needing to write the "__init__" method!
# @dataclass etsii kaikki "field"-kentät ja luo niistä "self."-


from dataclasses import dataclass


@dataclass
class StoreItem:
    name: str
    count: int
    price: int

    def buy_all_price(self):
        return self.count * self.price


store_item = StoreItem(name="Bottle", count=5, price=3.5)
print(store_item.buy_all_price())

store_item = StoreItem("Table", 3, 34)
print(store_item.buy_all_price())


import uuid
import datetime
from uuid import UUID


class Good:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Good[{self._id}]={self._name}, price={self._price}"


class Order:
    def __init__(self, client_id, goods: [Good]):
        self.price = 0
        self.order_id = uuid.uuid1()
        self.order_date = datetime.datetime.now()
        self.client_id = client_id
        self.goods = goods
        for good in goods:
            self.price += good.price

    @property
    def orderId(self):
        return self.order_id

    def __str__(self):
        return f"OrderId:{self.order_id},  Client={self.client_id}, Date: {self.order_date}, Goods{[g.name for g in self.goods]}"


class OrderRepository:
    
    def __init__(self):
        self.orders = dict()
    
    def add(self, order: Order):
        self.orders[order.orderId] = order

    def get(self, order_id: UUID) -> Order:
        return self.orders[order_id]

    def list(self, n_latest: int = None) -> [Order]:
        return list(self.orders.values())[-n_latest:]

    def delete(self, order_id: UUID):
        return self.orders.pop(order_id)


storage = OrderRepository()

milk = Good(1, 'Milk', 2.45)
apples = Good(2, 'Red apple', 3.67)

order1 = Order(11, [milk, apples])
assert order1.price == milk.price + apples.price
print(order1)

order2 = Order(12, [milk])
assert order2.price == milk.price
print(order2)

storage.add(order1)
storage.add(order2)

print("List", *storage.list(2))
assert storage.list(2) == [order1, order2]
print("Delete", storage.delete(order1.orderId))
print("List", *storage.list(1))
assert storage.list(2) == [order2]


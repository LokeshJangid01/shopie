from faker import Faker
import random
OrderItem = []
for i in range(10):
    OrderItem.append(
        {
            "order_id":i,
            "product_id":random.randint(1,10),
            "quantity":random.randint(5,15)
        }
    )
print(OrderItem)
    
    
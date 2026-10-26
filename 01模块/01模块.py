import order
import pay

order.create_order()   # 调用函数
print(order.max_order_amount)

order.cancel_order()
order.show_order()
#Question 2
def add_order(order_id):
    # Check whether the function already has an attribute called 'orders'
    # hasattr() returns False the first time the function is called
    if not hasattr(add_order, "orders"):
        # Create an empty list only once
        # if the list was created then the new order_id is directly added to the list that alredy existed
        # List is mutable,so it can store values across multiple calls
        add_order.orders = []
    # Add the new order_id to the list
    add_order.orders.append(order_id)
    print("Order added:", order_id)
    print("Order history:", add_order.orders)
    return add_order.orders
add_order(101)
add_order(102)
add_order(103)
from .models import Order, OrderLineItem


def create_order_history(user, session):
    order = Order.objects.create(
        customer=user.customer, total_cost=session.get("total", 0)
        )

    cart = session.get("cart")
    for product_id, quantity in cart.items():
        OrderLineItem.objects.create(
            order_history=order, product_id=product_id, quantity=quantity
            )
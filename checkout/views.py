from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Customer
from django.contrib.auth.models import User
from .utils import create_order_history
from .forms import MakePaymentForm, OrderForm
from .models import Order, OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
     

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                create_order_history(request.user, request.session)
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()   
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})

def order_history(request):

    """
    Displays order history to the user listed
    by date of purchase.
    """

    customer = None
    if request.user.is_authenticated():
        customer = Customer.objects.filter(user=request.user).first()
    orders = []
    if customer:
        orders = Order.objects.filter(customer=customer).order_by(
            "-created_at"
        )
    orders_with_items = []
    for order in orders:
        order_items = OrderLineItem.objects.filter(order_history=order)
        orders_with_items.append({"order": order, "items": order_items})
    return render(request, "order_history.html", {"orders": orders_with_items})
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from checkout.models import Order, OrderLineItem
from django.utils import timezone
from products.models import Product


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "You have successfully logged in!"
                    )
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    if request.user:
        orders = Order.objects.filter(
            user=request.user,
            date__lte=timezone.now()
            ).order_by('-date')
        for order in orders:
            order.total = 0
            line_item = OrderLineItem.objects.filter(order=order)
            for item in line_item:
                product = Product.objects.get(id=item.product.id)
                order.total += product.price * item.quantity
        return render(request, "profile.html", {'orders': orders})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "You have successfully registered"
                    )
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request,
                    "Unable to register your account at this time"
                    )
            return redirect(reverse('all_products'))
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form
        })

@login_required
def order_history(request):
    """
    Retrieves the order history of the user.
    """
    if request.user:
        orders = Order.objects.filter(
            user=request.user,
            date__lte=timezone.now()
            ).order_by('-date')

        return render(request, "profile.html", {'orders': orders})


@login_required
def order_info(request, pk):
    """
    This captures order info to then be displayed in profile for user
    """
    order = get_object_or_404(Order, pk=pk)
    order.save()
    order_total = 0
    line_item = OrderLineItem.objects.filter(order=order)
    for item in line_item:
        product = Product.objects.get(id=item.product.id)
        order_total += product.price * item.quantity
    return render(
        request,
        "order-info.html",
        {'order': order,
         'line_item': line_item,
         'order_total': order_total,
         'product': product},
        )

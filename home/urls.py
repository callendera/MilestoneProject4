from django.conf.urls import url, include
from .views import index
from products import views

urlpatterns = [
    url(r'$', all_products, name='index'),
]
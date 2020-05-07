from django.conf.urls import url, include
from .views import registration, profile, logout, login, order_history, order_info
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^profile/$', profile, name='profile'),
    url(r'^order-history$', order_history, name='order-history'),
    url(r'^order-history/(?P<pk>\d+)/order-info', order_info, name='order-info'),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
]

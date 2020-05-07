from django.conf.urls import url, include
from .views import registration, profile, logout, login
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^profile/$', profile, name='profile'),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
]

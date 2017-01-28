from django.conf.urls import url
from .views import IndexView,

from .views import register

urlpatterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'^register/', UserRegister.as_view(), name='register'),

]

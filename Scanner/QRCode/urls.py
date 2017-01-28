from django.conf.urls import url
from .views import IndexView, UserRegister

urlpatterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'^register/', UserRegister.as_view(), name='register'),

]

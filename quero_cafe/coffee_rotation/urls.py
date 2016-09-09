from django.conf.urls import url
from coffee_rotation import views

urlpatterns = [
    url(r'^', views.users_list, name='list'),
]
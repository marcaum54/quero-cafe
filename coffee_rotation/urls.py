from django.conf.urls import url
from coffee_rotation import views

urlpatterns = [
    url(r'^list', views.users_list, name='list'),
    url(r'^set-as-voluntary', views.set_as_voluntary, name='set_as_voluntary'),
]
from django.conf.urls import url
from colaboradores import views

urlpatterns = [
    url(r'^', views.colaborators_list, name='colaboradores_list'),
]
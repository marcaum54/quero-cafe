from django.conf.urls import url
from colaboradores import views

urlpatterns = [
    url(r'^', views.ColaboradoresList, name='colaboradores_list'),
]
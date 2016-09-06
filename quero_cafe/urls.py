from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # COLABORADORES
    url(r'^colaboradores/', include('colaboradores.urls', namespace='colaboradores')),
]
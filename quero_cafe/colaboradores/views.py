from django.shortcuts import render

from colaboradores.models import Colaborador

def ColaboradoresList(request):

    rows = Colaborador.objects.order_by('flag_date', 'name').all()

    return render(request, 'colaboradores/index.html', {
        'rows': rows
    })
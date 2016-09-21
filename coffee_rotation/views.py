from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from datetime import datetime

from django.contrib.auth.models import User
from coffee_rotation.models import Cycle
from coffee_rotation.models import Turn
from django.contrib import messages


def users_list(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (reverse_lazy('admin:login'), request.path))

    cycle = Cycle.objects.last()

    usuarios = User.objects.all()

    return render(request, 'colaboradores/index.html', {
        'usuarios': usuarios
    })


def set_as_voluntary(request):

    try:
        user = request.user
        cycle = Cycle.objects.last()
        voluntary_date = datetime.now()

        Turn.objects.create(user=user, cycle=cycle, voluntary_date=voluntary_date)

        messages.success(request, 'Voluntariou-se com sucesso!')

    except ValueError as error:
        messages.error(request, error)

    return redirect(reverse_lazy('list'))
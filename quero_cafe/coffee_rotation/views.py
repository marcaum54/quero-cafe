from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy


from django.contrib.auth.models import User


def users_list(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (reverse_lazy('admin:login'), request.path))

    usuarios = User.objects.all()

    return render(request, 'colaboradores/index.html', {
        'usuarios': usuarios
    })

# def setAsVoluntary(request):
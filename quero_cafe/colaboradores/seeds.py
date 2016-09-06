from colaboradores.models import Colaborador

colaboradores = [
    {
        'name': 'Marcos Fábio',
        'email': 'marcaum54@gmail.com'
    },
    {
        'name': 'Diego Araújo',
        'email': 'diegoaraujo@gmail.com'
    },
]

for colaborador in colaboradores:
    Colaborador( colaborador ).save()
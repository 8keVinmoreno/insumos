from django.shortcuts import render
from .models import Producto
from django.db.models import Q


def lista_productos(request):

    busqueda = request.GET.get("q", "").strip()

    productos = Producto.objects.all()

    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) | Q(codigo__icontains=busqueda)
        )

    return render(
        request, "catalogo/lista.html", {"productos": productos, "busqueda": busqueda}
    )

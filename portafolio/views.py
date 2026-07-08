from django.shortcuts import render,redirect
from django.urls import reverse

def graficadorView(request):
    if not request.GET:
        url = reverse('graficador')
        return redirect(f"{url}?fecha_inicio=1900-01-01&fecha_fin=2100-01-01&portafolio=Portafolio 1")
    
    return render(request, "graficador.html")


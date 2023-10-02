from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def page(request,slug):

    page=Page.objects.get(slug=slug)
    """
    Esta función es una vista de Django que renderiza una página HTML.

    Parameters:
    - request: objeto HttpRequest que contiene los datos de la solicitud.

    Returns:
    - Un objeto HttpResponse que representa la página renderizada.
    """
    return render(request,"pages/pages.html",{
        "title":page.title,
        "page":page
    })  

 


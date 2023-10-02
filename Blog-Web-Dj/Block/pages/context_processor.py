from pages.models import Page


def get_pages(request):
    pages=Page.objects.filter(public=True).order_by('order').values_list('id','title','slug')

    return{
        'pages':pages
    }
#Diccionario con todas las paginas guardadas 
